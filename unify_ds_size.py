import os
import cv2
import time
import shutil
import pandas as pd
from PIL import Image
import math

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

def extend_img(input_dir,im_file,target_ratio):#output_dir
    # 打開原始圖片
    image = Image.open(os.path.join(input_dir,im_file))

    # 獲取圖片的寬度和高度
    original_width, original_height = image.size

    # 計算目標寬度 
    target_width = math.floor(original_height * target_ratio) 

    # 提取最左側和最右側的整列像素
    left_column = [image.getpixel((0, y)) for y in range(original_height)]  # 左邊最左列
    right_column = [image.getpixel((original_width - 1, y)) for y in range(original_height)]  # 右邊最右列

    # 創建一個新的空白圖片，寬度為目標寬度
    new_image = Image.new("RGB", (target_width, original_height))

    # 計算每邊需要填充的寬度
    left_fill_width = (target_width - original_width) // 2
    right_fill_width = target_width - original_width - left_fill_width

    # 填充左右兩側的顏色
    for x in range(left_fill_width):
        # 填充左側：使用左側整列的顏色
        for y in range(original_height):
            #print('x: ',x,'y: ',y)
            new_image.putpixel((x, y), left_column[y])

    for x in range(original_width + left_fill_width, target_width):
        # 填充右側：使用右側整列的顏色
        for y in range(original_height):
            new_image.putpixel((x, y), right_column[y])

    # 將原圖片貼到新圖片的中間
    new_image.paste(image, (left_fill_width, 0))

    # 保存或顯示新圖片
    #new_image.save(os.path.join(output_dir,im_file[:-4])+"_extended.jpg")
    return new_image


def extend_img_frompath(im_path,target_ratio):#output_dir
    # 打開原始圖片
    image = Image.open(im_path)

    # 獲取圖片的寬度和高度
    original_width, original_height = image.size

    # 計算目標寬度 
    target_width = math.floor(original_height * target_ratio) 

    # 提取最左側和最右側的整列像素
    left_column = [image.getpixel((0, y)) for y in range(original_height)]  # 左邊最左列
    right_column = [image.getpixel((original_width - 1, y)) for y in range(original_height)]  # 右邊最右列

    # 創建一個新的空白圖片，寬度為目標寬度
    new_image = Image.new("RGB", (target_width, original_height))

    # 計算每邊需要填充的寬度
    left_fill_width = (target_width - original_width) // 2
    right_fill_width = target_width - original_width - left_fill_width

    # 填充左右兩側的顏色
    for x in range(left_fill_width):
        # 填充左側：使用左側整列的顏色
        for y in range(original_height):
            #print('x: ',x,'y: ',y)
            new_image.putpixel((x, y), left_column[y])

    for x in range(original_width + left_fill_width, target_width):
        # 填充右側：使用右側整列的顏色
        for y in range(original_height):
            new_image.putpixel((x, y), right_column[y])

    # 將原圖片貼到新圖片的中間
    new_image.paste(image, (left_fill_width, 0))


    return new_image


def resize_img_frompath(input_dir,im_file,new_width, new_height,output_dir):
    # Open the original image
    image = Image.open(os.path.join(input_dir,im_file))

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save or show the resized image
    resized_image.save(os.path.join(output_dir,im_file[:-4])+"_resized.jpg")
   
def resize_img(im_file,image,new_width, new_height,output_dir):
    # Get the original dimensions
    original_width, original_height = image.size

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save or show the resized image
    resized_image.save(os.path.join(output_dir,im_file[:-4])+"_resized.jpg")

def resize_img_tofile(image,new_width, new_height,output_path):
    # Get the original dimensions
    original_width, original_height = image.size

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save or show the resized image
    resized_image.save(output_path)

# def resize_img_frompath(output_dir,im_file,target_ratio):
#     # Open the original image
#     image = Image.open(os.path.join(output_dir,im_file))

#     # Get the original dimensions
#     original_width, original_height = image.size

#     # Calculate the new dimensions
#     # Option 1: Resize based on original height (W = 0.2 * H)
#     new_height = original_height
#     new_width = int(target_ratio * new_height)

#     # Option 2: Alternatively, resize based on original width (H = W / 0.2)
#     # new_width = original_width
#     # new_height = int(original_width / 0.2)

#     # Resize the image
#     resized_image = image.resize((new_width, new_height))

#     # Save or show the resized image
#     resized_image.save(os.path.join(output_dir,im_file[:-4])+"_resized.jpg")
   
# def resize_img(output_dir,im_file,image,target_ratio):
#     # Get the original dimensions
#     original_width, original_height = image.size

#     # Calculate the new dimensions
#     # Option 1: Resize based on original height (W = 0.2 * H)
#     new_height = original_height
#     new_width = int(target_ratio * new_height)

#     # Option 2: Alternatively, resize based on original width (H = W / 0.2)
#     # new_width = original_width
#     # new_height = int(original_width / 0.2)

#     # Resize the image
#     resized_image = image.resize((new_width, new_height))

#     # Save or show the resized image
#     resized_image.save(os.path.join(output_dir,im_file[:-4])+"_resized.jpg")

path = '/home/jovyan/dinov2/eye_datasets_preparing/train_ori'
output_path='/home/jovyan/dinov2/eye_datasets_preparing/train20241112'
ratio_standard_img = '/home/jovyan/dinov2/eye_datasets_preparing/train_ori/cut_stream1_20220727_172431_1241.jpg'
im = Image.open(ratio_standard_img)
w, h = im.size
print('width: ', w)
print('height:', h)

w_min,h_min=1000000,100000
for f in os.listdir(path):
    if '.ipynb_checkpoints' not in f:
        if '.jpg' or '.jpeg' in f:
            print(os.path.join(path,f))
            im_check = Image.open(os.path.join(path,f))        
            w_check, h_check = im_check.size
            #print(w_check, h_check)
            if w_check<w_min:
                w_min=w_check
            if h_check<h_min:
                h_min=h_check    
        
ratio_standard= w/h
print('w/h ratio_standard :',ratio_standard)
print('w_min: ',w_min,' h_min: ',h_min)
target_w = w_min
target_h = math.floor(w_min/ratio_standard)
print('target_w: ',target_w,'   target_h: ',target_h)
#print('os.listdir(path):',os.listdir(path))

#for test 
# for f in os.listdir(path):
#     if '.ipynb_checkpoints' not in f:
#         if '.jpg' or '.jpeg' in f:
#             print(os.path.join(path,f))
#             if 'REFUGE' in f: 
#                 e_img = extend_img(path,f,ratio_standard)
#                 resize_img(f,e_img,target_w,target_h,output_path)
#             else:
#                 resize_img_frompath(path,f,target_w,target_h,output_path)

# for REFUGE
output_dir= '/home/jovyan/dinov2/eye_datasets_preparing/REFUGE2_extended_resized'
for root,dirs,files in os.walk('/home/jovyan/dinov2/eye_datasets_preparing/REFUGE2'):

    for f in files:
        if 'mask' in root:
            pass
        else:
            input_path = os.path.join(root,f)
            print(os.path.join(root,f))
            if 'train' in input_path:
                tag='train'
            elif 'val' in input_path:
                tag='val'
            elif 'test' in input_path:
                tag='test'     

            output_path = os.path.join(output_dir,'REFUGE2_extended_resized_'+tag+'_'+f)   
            print(output_path)   

            if '.ipynb_checkpoints' not in f:
                if '.jpg' or '.jpeg' in f:
                    # print(f)
                    e_img = extend_img_frompath(input_path,ratio_standard)
                    resize_img_tofile(e_img,target_w,target_h,output_path)

            
