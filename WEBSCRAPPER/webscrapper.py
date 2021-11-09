from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import urllib.parse as p
import re
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_authenticate():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    
    return build(api_service_name, api_version, credentials=creds)

youtube = youtube_authenticate()

def get_video_id_by_url(url):

    parsed_url = p.urlparse(url)
    
    video_id = p.parse_qs(parsed_url.query).get("v")
    if video_id:
        return video_id[0]
    else:
        raise Exception(f"Wasn't able to parse video URL: {url}")

def get_video_details(youtube, **kwargs):
    return youtube.videos().list(
        part="snippet,contentDetails,statistics",
        **kwargs
    ).execute()

def print_video_infos(video_response):
    items = video_response.get("items")[0]
    
    snippet         = items["snippet"]
    statistics      = items["statistics"]
    content_details = items["contentDetails"]
    
    channel_title = snippet["channelTitle"]
    title         = snippet["title"]
    publish_time  = snippet["publishedAt"]
    
    comment_count = statistics["commentCount"]
    like_count    = statistics["likeCount"]
    dislike_count = statistics["dislikeCount"]
    view_count    = statistics["viewCount"]
    
    duration = content_details["duration"]
    
    parsed_duration = re.search(f"PT(\d+H)?(\d+M)?(\d+S)", duration).groups()
    duration_str = ""
    for d in parsed_duration:
        if d:
            duration_str += f"{d[:-1]}:"
    duration_str = duration_str.strip(":")
    print(f"""\
    Title: {title}
    Channel Title: {channel_title}
    Publish time: {publish_time}
    Duration: {duration_str}
    Number of comments: {comment_count}
    Number of likes: {like_count}
    Number of dislikes: {dislike_count}
    Number of views: {view_count}
    """)
    
video_url = "https://www.youtube.com/watch?v=sugvnHA7ElY"

video_id = get_video_id_by_url(video_url)

response = get_video_details(youtube, id=video_id)

print_video_infos(response)