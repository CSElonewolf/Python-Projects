from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image  
from moviepy.video.fx.all import crop 



source_path = os.path.join(SAMPLE_INPUTS,"sample.mp4")

GIF_DIR  = os.path.join(SAMPLE_OUTPUTS,"gif")
os.makedirs(GIF_DIR,exist_ok=True)

output_paths = os.path.join(GIF_DIR,"sample.gif")


# By Default it uses imageio Program to make gifs 
clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10,20)
subclip = subclip.resize(width = 400)
# subclip.write_gif(output_paths)


# Here we are using 'ffmpeg' program 
clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10,20)
subclip = subclip.resize(width = 720)
# subclip.write_gif(output_paths, fps = 20, program = "ffmpeg") 