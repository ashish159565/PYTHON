from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import urllib.parse as p
import re
import os
import pickle
import mysql.connector

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtube_authenticate():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle","rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open("token.pickle","wb") as token:
            pickle.dump(creds, token)
        
    return build(api_service_name, api_version, credentials=creds)
youtube = youtube_authenticate()
 
def get_video_id(url):
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

def store_video_infos(video_response):
    items = video_response.get("items")[0]
    snippet = items["snippet"]
    statistics = items["statistics"]
    content_details = items["contentDetails"]
    channel_title = snippet["channelTitle"]
    title = snippet["title"]
    description = snippet["description"]
    publish_time = snippet["publishedAt"]
    comment_count = statistics["commentCount"]
    like_count = statistics["likeCount"]
    lc = like_count
    view_count = statistics["viewCount"]
    vc = view_count
    like_percentage = (lc*100)/vc
    duration = content_details["duration"]
    parsed_duration = re.serach(f"PT(\d+H)?(\d+M)?(\d+S)",duration).groups()
    duration_str = ""
    for d in parsed_duration:
        if d:
            duration_str += f"{d[:-1]}:"
    duration_str = duration+str.strip(":")
    mydb = mysql.connector.connect(host="localhost",user="root",password="Z/NL3ivh#7KA",database="java")
    
    mycursor = mydb.cursor()
    
    sql = "INSERT INTO data VALUES(%s, %s, %s, %s, %d, %d, %d, %s, %f)"
    vals = (channel_title,title,description,publish_time,comment_count,like_count,view_count,like_percentage)
    mycursor.execute(sql,vals)
    mydb.commit()

def search(youtube, **kwargs):
    return youtube.search().list(
        part="snippet",
        **kwargs
        ).execute()


q = input("Enter the programming language you want to learn:")
response = search(youtube,q,maxResults=10)
items = response.get("items")
for item in items:
    video_id = item["id"]["videoId"]
    video_response = get_video_details(youtube, id=video_id)
    store_video_infos(video_response)    