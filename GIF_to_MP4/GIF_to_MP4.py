import moviepy as mp
import os
import sys

clip = mp.VideoFileClip("tenor.gif")

mp4_path = os.path.splitext("tenor.gif")[0] + ".mp4"

clip.write_videofile(mp4_path, codec="libx264")


