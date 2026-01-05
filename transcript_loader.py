from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    else:
        return None

def load_transcript(youtube_url):
    video_id = get_video_id(youtube_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    full_text = ""
    for item in transcript:
        full_text += item["text"] + " "

    return [Document(page_content=full_text)]
