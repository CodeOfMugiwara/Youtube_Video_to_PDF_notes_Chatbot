def get_video_id(url):
    if "youtube.com" in url:
        return url.split("v=")[1]
    elif "youtu.be" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")
