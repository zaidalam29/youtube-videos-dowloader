from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=t6vm8h5BDxo"

yt = YouTube(video_url, use_oauth=False, allow_oauth_cache=True)
video_stream = yt.streams.get_highest_resolution()
video_stream.download()

print("वीडियो डाउनलोड हो गया!")