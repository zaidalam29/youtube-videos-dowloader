from yt_dlp import YoutubeDL

url = input("Enter YouTube video URL: ")

ydl_opts = {}
with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    print(f"Title: {info_dict.get('title', None)}")
    print("Download complete!")