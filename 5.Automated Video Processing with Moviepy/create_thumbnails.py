from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


source_path = os.path.join(SAMPLE_INPUTS,'sample.mp4')

# directory that stores thumbnails per seconds
thumbnail_per_seconds_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_per_seconds')
os.makedirs(thumbnail_per_seconds_dir,exist_ok=True)

# directory that sores thumbnals per frame 
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_per_frame')
os.makedirs(thumbnail_per_frame_dir,exist_ok=True)

# directory thats stores thumbnails per seconds with filename in milliseconds 
thumbnail_per_seconds_with_millisecfilename_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_with_millisec_name')
os.makedirs(thumbnail_per_seconds_with_millisecfilename_dir,exist_ok=True)


# directory thats stores thumbnails per seconds with filename in milliseconds 
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_per_halfsec')
os.makedirs(thumbnail_per_half_second_dir,exist_ok=True)


# grab the clip 
clip = VideoFileClip(source_path)

# printing certain vital details of the clip 
print(clip.reader.fps) # fps-> Frames per seconds 
print(clip.reader.nframes)
print(clip.duration)


# extracts thumbnail_per_frame
for i,frame in enumerate(clip.iter_frames()):
	# print(frame) 
	new_img_filepath = os.path.join(thumbnail_per_frame_dir,f"{i}.jpg")
	new_img = Image.fromarray(frame)
	new_img.save(new_img_filepath)


duration = clip.reader.duration
max_duration = int(duration) +1 

# extracts thumbnails per seconds 
for i in range(0,max_duration):
	print(f"frame at {i} seconds")
	frame = clip.get_frame(i)
	# print(frame) 
	new_img_filepath = os.path.join(thumbnail_per_seconds_dir,f"{i}.jpg")
	new_img = Image.fromarray(frame)
	new_img.save(new_img_filepath)



fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0)

# another way to extracts thumbnails per seconds
for i, frame in enumerate(clip.iter_frames()):
    if i % fps == 0:
        current_ms = int((i / fps) * 1000)
        print(int((i / fps)))
        new_img_filepath = os.path.join(thumbnail_per_seconds_with_millisecfilename_dir, f"{current_ms}.jpg")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)

# extracts thumbnails per half seconds
for i, frame in enumerate(clip.iter_frames()):
    fphs = int(fps/2.0)
    if i % fphs == 0:
        current_ms = int((i / fps) * 1000)
        new_img_filepath = os.path.join(thumbnail_per_half_second_dir, f"{current_ms}.jpg")
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath) 