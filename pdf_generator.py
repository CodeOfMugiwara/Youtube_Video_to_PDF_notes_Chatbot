from fpdf import FPDF
import re
import openai


def register_poppins_font(pdf):
    # Define paths to the font files
    regular_font_path = "fonts/Poppins-Regular.ttf"
    bold_font_path = "fonts/Poppins-Bold.ttf"

    # Add the Poppins Regular font
    pdf.add_font("Poppins", "", regular_font_path, uni=True)

    # Add the Poppins Bold font
    pdf.add_font("Poppins", "B", bold_font_path, uni=True)


def sanitize_filename(filename):
    # Replace invalid characters with underscores and ensure it does not start with a dot
    filename = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)
    filename = filename.strip()
    if filename.startswith('.'):
        filename = '_' + filename[1:]
    return filename


def generate_title(content):
    prompt = f"Generate a concise 4-5 word title for the following content: {
        content}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=10
    )
    title = response.choices[0].text.strip()
    return title


def generate_pdf(pdf, summary, title, content):
    pdf = FPDF()
    pdf.add_page()

    # Register the Poppins fonts
    register_poppins_font(pdf)

    # Generate a title for the PDF
    title = generate_title(title)

    # Set title with bold font
    pdf.set_font("Poppins", "B", 20)
    pdf.cell(0, 10, title, ln=True, align="C")
    pdf.ln(10)

    # Set content
    pdf.set_font("Poppins", size=12)
    for line in content.split("\n"):
        if line.startswith("1. "):
            pdf.set_font("Poppins", 'B', 14)
            pdf.multi_cell(0, 10, line)
        elif line.startswith("• "):
            pdf.set_font("Poppins", size=12)
            pdf.multi_cell(0, 10, line)
        else:
            pdf.set_font("Poppins", size=12)
            pdf.multi_cell(0, 10, line)
        pdf.ln(5)

    # Sanitize the title to make a valid filename
    sanitized_title = sanitize_filename(title)

    # Save the PDF with the sanitized title
    pdf.output(f"{sanitized_title}_Notes.pdf")
