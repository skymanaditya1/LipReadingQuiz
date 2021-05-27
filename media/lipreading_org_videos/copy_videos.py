# Method used to copy non-duplicate content from lipreading videos to different tasks 
import os
from glob import glob 

files = glob('lipreading-missing-words*.txt')
#files.extend(glob('consonants-eyedrills*.txt'))
dir_name = 'lipreading_missing_words'
print(files)

videos = set()
video_lines = list()
duplicate_videos = 0
total_videos = 0
for file in files:
	with open(file, 'r') as f:
		lines = list(filter(None, f.read().split('\n')))
		for line in lines:
			video_file_path = line.split('\t')[0]
			print(video_file_path)
			if video_file_path.split('/')[1] in videos:
				duplicate_videos += 1
				print('Video already exists')
			else:
				videos.add(video_file_path.split('/')[1])
				video_lines.append(line)
			total_videos += 1

print(f'duplicate videos: {duplicate_videos}')
print(f'total videos: {total_videos}')

# write the contents of the list into a file 
with open(dir_name + '.txt', 'w') as f:
	for video_line in video_lines:
		f.write(video_line)
		f.write('\n')

# For the videos in the file, transfer them to the new directory 
if not os.path.exists(dir_name):
	os.mkdir(dir_name)

with open(dir_name + '.txt', 'r') as f:
	lines = list(filter(None, f.read().split('\n')))
	for line in lines:
		os.system('cp {0} {1}'.format(line.split('\t')[0], dir_name))
