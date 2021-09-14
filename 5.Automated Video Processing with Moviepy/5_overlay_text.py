from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


# grab the source video and audio path 
source_audio_path = os.path.join(SAMPLE_INPUTS,'audio.mp3')
source_video_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')

# directory that stores all the files related to the program
overlay_video_dir = os.path.join(SAMPLE_OUTPUTS,'video-with-overlay')
os.makedirs(overlay_video_dir,exist_ok=True)
og_audio_path = os.path.join(overlay_video_dir,'og.mp3')

# path that stores the original audio,composite audio,final video respectively.
final_video_path = os.path.join(overlay_video_dir,'overlay-video.mp4')

video_clip = VideoFileClip(source_video_path)
background_audio_clip = AudioFileClip(source_audio_path)
 
# Extracting the original audio out of the video 
original_audio = video_clip.audio 
original_audio.write_audiofile(og_audio_path)


intro_duration = 5
intro_text = TextClip("Hello World!", fontsize= 70, color='white',size = video_clip.size) #video_clip.size gives the height and width of the orignal video
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_fps(video_clip.fps)
intro_text = intro_text.set_pos("center")
# cliping the background_music audio to the duration of the intro_text 
bg_music = background_audio_clip.subclip(0, intro_duration)
bg_music = bg_music.volumex(0.25)
intro_text = intro_text.set_audio(bg_music)
# concatenate the intro_text and video_clip and make a final video  
# final_clip = concatenate_videoclips([intro_text,video_clip])
# final_clip.write_videofile(final_video_path)

# Building the watermark_text
w,_ = video_clip.size
watermark_text = TextClip("CSELonewolf", fontsize=40,color='white',align='West',size=(w,40))
watermark_text = watermark_text.set_fps(video_clip.fps)
watermark_text = watermark_text.set_duration(video_clip.duration)
watermark_text = watermark_text.set_position(('bottom'))
watermark_text = watermark_text.margin(left=10, right=10, bottom=2, opacity=0)

# video with the watermark
overlay_clip = CompositeVideoClip([video_clip, watermark_text], size=video_clip.size)
overlay_clip = overlay_clip.set_duration(video_clip.reader.duration)
overlay_clip = overlay_clip.set_fps(video_clip.fps)

# set the audio to the CompositeVideo
og_audio = AudioFileClip(og_audio_path)
overlay_clip = overlay_clip.set_audio(og_audio)


# concatenate the intro_text and overlay_clip and make a final video  
final_clip = concatenate_videoclips([intro_text,overlay_clip])
final_clip.write_videofile(final_video_path)