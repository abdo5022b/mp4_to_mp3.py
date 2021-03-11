import os
base_dir = str(input("Path of file >>"))
video = str(input("Video name >>"))
mp4_file = base_dir+"/"+video
mp3_file = base_dir +"/audio.mp3"
cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
os.system(cmd)
#By Abdo5022b
