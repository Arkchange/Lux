import yt_dlp

url = "https://www.youtube.com/watch?v=u7kdVe8q5zs&t=19s"

ydl_opts = {
    'format': 'bv[ext=mp4]',  # bv = best video only
    'outtmpl': '%(title)s_video_only.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
