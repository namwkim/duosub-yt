import sys
from pytube import YouTube

if __name__ == "__main__":
    if len(sys.argv)>0:
        print("Download URL:", sys.argv[1])
        # YouTube('https://youtu.be/IApo5TBR7jc').streams.first().download()
        yt = YouTube(sys.argv[1])
        yt.streams.filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download()
