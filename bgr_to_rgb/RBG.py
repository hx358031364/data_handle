import cv2
import os
from PIL import Image
from tqdm import tqdm
jpg_path = "D:\\data\\zk\\1\\"
file_folders = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
num=0
for jpg_files in file_folders:
    jpg_filelist ="D:/data/zk/1/"+jpg_files
    img = cv2.imread(jpg_filelist)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([b, g, r])
    im = Image.fromarray(img2)
    im.save(jpg_path+str(num)+".jpg")
    num+=1