# pip install pytube
# i keep running into SSL Certificate issues when I try this or youtube-dl


from pytube import YouTube
import sys

videoURL = ""
if (len(sys.argv) > 1):
    videoURL = sys.argv[1]
if ("youtube.com" not in videoURL):
    videoURL = input("Enter YouTube URL: ")
yt = YouTube(videoURL)
# yt = YouTube(videoURL,use_oauth=True,allow_oauth_cache=True)
filename = yt.title.replace(" ","_")
print("Downloading YouTube File: " + yt.title)
yt.streams.first().download(filename=filename + ".mp4")