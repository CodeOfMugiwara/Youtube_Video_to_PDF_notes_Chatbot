# Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Demo](#demo)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Configuration](#configuration)
  - [Create a `.env` File](#create-a-env-file)
  - [Obtain API Keys](#obtain-api-keys)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

The **YouTube Video to PDF Notes Chatbot** is a powerful tool that transforms YouTube video content into well-structured, detailed PDF notes. By extracting transcripts, processing the content, and generating customizable PDFs, this chatbot aids in managing and summarizing long video content efficiently. Ideal for students, educators, and professionals seeking to streamline their learning and note-taking processes.

## Features

- **Transcript Extraction**: Automatically extracts transcripts from YouTube videos.
- **Content Processing**: Summarizes and organizes content into coherent notes.
- **Dynamic PDF Generation**: Creates PDFs with advanced formatting and custom fonts (e.g., Poppins).
- **Customizable Titles**: Generates concise 4-5 word titles based on the content.
- **User-Friendly Interface**: Easy to use with clear instructions and prompts.

## Technologies Used

- **Python**: Primary programming language.
- **FPDF**: Library for PDF generation.
- **OpenAI GPT-3.5**: For generating concise titles.
- **YouTube API**: To fetch video transcripts.
- **dotenv**: For managing environment variables.

## Demo

*(Optional: Include screenshots or a GIF demonstrating the application)*

![Demo Screenshot](path/to/screenshot.png)

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- **Python 3.7 or higher**: Ensure Python is installed. [Download Python](https://www.python.org/downloads/)
- **Git**: For version control. [Download Git](https://git-scm.com/downloads)
- **Virtual Environment**: Recommended to manage dependencies.

### Clone the Repository

```bash
git clone https://github.com/CodeOfMugiwara/Youtube_Video_to_PDFnotes_Chatbot.git
cd Youtube_Video_to_PDFnotes_Chatbot
```
### Set Up a Virtual Environment
It's best to use a virtual environment to manage dependencies.

```bash
# On Windows
python -m venv venv
venv\\Scripts\\activate
```
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Install the required Python packages using 'pip'.
```bash
pip install -r requirements.txt
```

## Configuration
### Create a '.env' File

```bash
touch .env
```
### Add the Following Variables to .env

```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Obtain API Keys
### 1. YouTube API Key

To interact with YouTube and fetch video transcripts, you'll need a YouTube Data API key.

# Steps to Obtain:
  1. Go to the Google Cloud Console.
  2. Create a new project or select an existing one.
  3. Navigate to APIs & Services > Library.
  4. Search for YouTube Data API v3 and enable it.
  5. Go to APIs & Services > Credentials.
  6. Click on Create Credentials > API Key.
  7. Copy the generated API key and add it to your .env file as YOUTUBE_API_KEY.

### 2. OpenAI API Key
To generate concise titles using OpenAI's GPT-3.5, you'll need an OpenAI API key.

# Steps to Obtain:
  1. Sign up or log in to your OpenAI account.
  2. Navigate to API Keys in the dashboard.
  3. Click on Create new secret key.
  4. Copy the generated API key and add it to your .env file as OPENAI_API_KEY.

## Usage
After setting up the project and configuring the environment variables, you can use the chatbot to generate PDF notes from YouTube videos.

# Activate the Virtual Environment
```bash
# On Windows
venv\\Scripts\\activate
```
```bash
# On macOS/Linux
source venv/bin/activate
```

# Run the Application
```bash
python main.py
```

# Follow the Prompts
  1. Enter the YouTube video URL or ID.
  2. The chatbot will process the video, extract the transcript, summarize the content, and generate a PDF with a custom title.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
  1. Fork the Repository
  2. Create a New Branch

```bash
git checkout -b feature/YourFeature
```
  3. Make Your Changes
  4. Commit Your Changes

```bash
git commit -m "Add your message here"
```
  5. Push to Your Branch

```bash
git push origin feature/YourFeature
```
  6. Create a Pull Request
       Go to the original repository and click on New Pull Request.
