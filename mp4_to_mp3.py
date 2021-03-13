import os
base_dir = str(input("Path of file >>"))
video = str(input("input video name >>"))
mp4_file = base_dir+"/"+video
mp3_file = base_dir +"/audio.mp3"
cmd = "ffmpeg -i {} -vn {}".format(mp4_file, mp3_file)
try :
	os.system(cmd)
except :
	print("ffmpeg not installed ")
	os.system("pkg install ffmpeg")
	
#By Abdo5022b
