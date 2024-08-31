import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL."""
    # Handle both standard and short YouTube URLs
    if 'youtube.com' in url:
        video_id_match = re.search(r'[?&]v=([^&]+)', url)
    elif 'youtu.be' in url:
        video_id_match = re.search(r'youtu.be/([^?&]+)', url)
    else:
        return None
    
    if video_id_match:
        video_id = video_id_match.group(1)
        print(f"Extracted Video ID: {video_id}")  # Debugging statement
        return video_id
    else:
        print("Error: Video ID not found in URL.")  # Debugging statement
        return None

def get_transcript(video_id):
    """Retrieve transcript for a given video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([t['text'] for t in transcript])
        return transcript_text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Get YouTube video URL from user
    video_url = input("Enter YouTube video URL: ")
    print(f"Entered URL: {video_url}")  # Debugging statement
    
    # Extract video ID from URL
    video_id = get_video_id(video_url)
    if video_id is None:
        return
    
    # Retrieve transcript for the video ID
    transcript_text = get_transcript(video_id)
    
    # Print the transcript
    print(f"Transcript: {transcript_text}")

if __name__ == "__main__":
    main()
