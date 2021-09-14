from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_per_halfsec')

thumb_per_sec_with_millisecfname_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_with_millisec_name')

thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS,'thumbnail_per_frame')
output_video = os.path.join(SAMPLE_OUTPUTS,'thumbs.mp4')


# V1.0 of making a video out of images 
''' 
pros: Easy 
cons: images are not in order
'''
this_dir = os.listdir(thumb_per_sec_with_millisecfname_dir)
filepaths = [os.path.join( thumb_per_sec_with_millisecfname_dir ,fname) for fname in this_dir if fname.endswith("jpg")]
print(filepaths)
clip = ImageSequenceClip(filepaths,fps=5)
clip.write_videofile(output_video)  




# V2.0 of making a vidoe out of the thumbnails 

''' 
pros: Files are ordered and the video will be in sequence
cons: need to sort the data by grabing thr filrnames 
'''
directory = {} 
for root,dirs,files in os.walk( thumb_per_sec_with_millisecfname_dir):
	for fname in files:
		filepath = os.path.join(root,fname)
		try:
			key = float(fname.replace(".jpg",""))
		except:
			key = None 
		if key != None:
			directory[key] = filepath 

new_paths = []
for k in sorted(directory.keys()):
	# print(k) 
	filepath = directory[k]
	new_paths.append(filepath)
 
clip = ImageSequenceClip(new_paths,fps=5)
clip.write_videofile(output_video) 



