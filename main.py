from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os 

load_dotenv()
apiKey = os.getenv('YOUTUBE_API_KEY')


def getDuration(apiKey):
    try: 
        playlistIdRaw = input("Enter Playlist URL or Playlist ID: ")
        playlistId = playlistIdRaw.split("list=")[1] if "list=" in playlistIdRaw else playlistIdRaw
        youtube = build("youtube", "v3", developerKey=apiKey)

        playlistRequest = youtube.playlistItems().list(
        part="snippet,contentDetails", playlistId=playlistId, maxResults=100 )

        playlistResponse = playlistRequest.execute()

        totalSeconds = 0  # Initialize total duration in seconds

        for item in playlistResponse["items"]:
            videoId = item["contentDetails"]["videoId"]

        # Fetch video statistics for each video ID
            videoRequest = youtube.videos().list(part="contentDetails", id=videoId)
            videoResponse = videoRequest.execute()

            duration = videoResponse["items"][0]["contentDetails"]["duration"]
            duration = duration.replace("PT", "")
            hours, minutes, seconds = 0, 0, 0

            if "H" in duration:
                hours = int(duration.split("H")[0])
                duration = duration.split("H")[1]
                totalSeconds += hours * 3600
            if "M" in duration:
                minutes = int(duration.split("M")[0])
                duration = duration.split("M")[1]
                totalSeconds += minutes * 60
            if "S" in duration:
                seconds = int(duration.split("S")[0])
                totalSeconds += seconds

        days = totalSeconds // 86400
        hours = (totalSeconds % 86400) // 3600
        minutes = (totalSeconds % 3600) // 60
        seconds = (totalSeconds % 3600) % 60
        print(
        f"Duration of playlist:\n{days} Days \n{hours} Hours\n{minutes} Minutes\n{seconds} Seconds")
        
    except HttpError:
        print("Incorrect Url, try again")
        getDuration(apiKey)

getDuration(apiKey)