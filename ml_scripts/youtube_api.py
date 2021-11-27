from googleapiclient.discovery import build

api_key = "AIzaSyD5-rQrP9eUTa4vP5N1d587mlR1B2XUGPk"

youtube = build('youtube', 'v3', developerKey=api_key)


request = youtube.search().list(
    part="snippet",
    q="Recipe with Banana and apple as ingridents",
    maxResults="5").execute()

videos = request['items']

for video in videos:
    final = video['snippet']['title']
    videoid = video['id']['videoId']
    print(final)
    link = "LINK: https://www.youtube.com/watch?v=" + videoid
    print(link)
    print("\n")
    print("___________________________________________________________________________")
    print("\n")
