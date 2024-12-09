#!/usr/bin/python3


# importing packages 
from pytube import YouTube
from moviepy.editor import *
import os 

list_of_videos = []
video_number = 0
with open(input("file_of_videos: ")) as file_with_videos:
    for link in file_with_videos:
        list_of_videos.append(link.strip())

# check for destination to save file 
print("Enter the destination (leave blank for current directory)") 
destination = str(input(">> ")) or '.'


for link in list_of_videos:
    # url input from user 
    yt = YouTube(link) 
    
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
    
    # download the file 
    out_file = video.download(output_path=destination) 
    print(out_file)
    # save the file 
    base, ext = os.path.splitext(out_file)

    wd_list = base.split("/")
    wd = "/"
    for i in range(1, len(wd_list) - 1):
        wd = wd + wd_list[i] + "/"

    new_file = wd + str(video_number) + " " + yt.title + '.mp3'
    video_number += 1
    os.rename(out_file, new_file)

    vid = VideoFileClip(new_file);

    vid.audio.write_audiofile("example.mp3")
    
    # result of success 
    print(yt.title + " has been successfully downloaded.")

