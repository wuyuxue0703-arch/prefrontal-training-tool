from moviepy.editor import ImageClip, CompositeVideoClip, VideoClip
from moviepy.editor import ImageClip, VideoClip
from PIL import Image, ImageDraw
import numpy as np

TOTAL_SEC = 120
bg_clip = ImageClip("train.png").set_duration(TOTAL_SEC)
W, H = bg_clip.size

def make_frame(t):
    remain = max(TOTAL_SEC - t, 0)
    m = int(remain // 60)
    s = int(remain % 60)
    timestr = f"{m:02d}:{s:02d}"

    frame = bg_clip.get_frame(t)
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img)

    draw.text((W*0.5, H*0.08), timestr, fill = "black", font_size = 60, anchor = "mm")

    return np.array(img)


countdown_clip = VideoClip(make_frame, duration = TOTAL_SEC)
countdown_clip.write_videofile("train_countdown.mp4", fps = 10)
