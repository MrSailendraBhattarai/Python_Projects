
# pip install pytube
from pytube import YouTube

try:
    url=input("Enter YouTube Url : ")

    yt=YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")
except Exception as e:
    print(f"An error occurred: {e}")

