from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

# grab the source video and audio path 
source_video_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS,'audio.mp3')

# directory that stores all the files related to the program
mix_audio_dir = os.path.join(SAMPLE_OUTPUTS,'mixed-audio')
os.makedirs(mix_audio_dir,exist_ok=True)

# path that stores the original audio,composite audio,final video respectively.
og_audio_path = os.path.join(mix_audio_dir,'og.mp3')
final_audio_path = os.path.join(mix_audio_dir,'final-audio.mp3')
final_video_path = os.path.join(mix_audio_dir,'final-video.mp4')


video_clip = VideoFileClip(source_video_path)

# Extracting the original audio out of the video 
original_audio = video_clip.audio 
original_audio.write_audiofile(og_audio_path)
 
# cliping the background_music audio to the duration of the original audio 
background_audio_clip = AudioFileClip(source_audio_path)
bg_music = background_audio_clip.subclip(0, original_audio.duration)
 
 # changing the volume of the bg_music 
bg_music = bg_music.volumex(0.10)

# composition of the original_audio and bg_music
final_audio = CompositeAudioClip([original_audio,bg_music])
final_audio.write_audiofile(final_audio_path,fps= original_audio.fps)

# we set the final_audio to the video and save it 
final_clip = video_clip.set_audio(final_audio)
final_clip.write_videofile(final_video_path)
