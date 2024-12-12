import os
import cv2
import time
import shutil
import pandas as pd
from PIL import Image


def check_create_dir(dir_path):
    if os.path.exists(dir_path):
        # removing the file using the os.remove() method
        #os.rmdir(dir_path) #cannot rmdir not empty
        shutil.rmtree(dir_path) # DIRECTLY REMOVE DIR !!
        os.mkdir(dir_path)
    else:
        os.mkdir(dir_path)

def check_dir_not_rm(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)



fps = 2
mode = 'video_to_frame'#'filter_anterior&oct_frame'# None #
video_filename ='CATARACTS_train01'
path = '/home/jovyan/dinov2/eye_datasets_preparing'#/train
output_dir = f'{path}/{video_filename}_original_frames_fps{fps}'
log_dir = f'{path}/{video_filename}_original_logs'


files_video = list(os.listdir( path ))
print(files_video)

if mode == 'video_to_frame':
    check_create_dir(output_dir)
    check_create_dir(log_dir)


    for f_v in files_video:
        # if '.mp4' in f_v:
        if '.mp4' in f_v and video_filename in f_v:
            print(f_v)
            # ori video to img
            file_path = path + '/'+f_v
            out_frame_path = output_dir +'/'+f_v[:-4]
            log_filename = log_dir +'/log_'+f_v[:-4]+'.txt'
            print(file_path)
            print(out_frame_path)
            check_create_dir(out_frame_path)
            frame_name=out_frame_path+'/'+f_v[:-4]+'_'
            cmd_frame = "ffmpeg -i %s -vf fps=%i %s"%(file_path,fps,frame_name)+"%d.jpg"
            print('\n',cmd_frame)
            os.system(cmd_frame)

            #output ori video info. as log file
            cmd_log = "ffmpeg -i %s 2> %s"%(file_path,log_filename)
            print('\n',cmd_log)
            os.system(cmd_log)

