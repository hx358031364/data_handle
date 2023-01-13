from  PIL  import Image
import os
from multiprocessing import Pool, cpu_count
# import subprocess
import shutil
# import cv2
# from PIL import Image
# import warnings
threads = 10

file_path = '/data2/huangxin/yolov5_logodet/datasets/labels/train'
images = os.listdir(file_path)

def check_image_opencv(file):
    try:
        name = file.replace(".txt", '.jpg')
        file_jpg = os.path.join('/data2/huangxin/yolov5_logodet/datasets/images/train', name)
        shutil.move(file_jpg, '/data2/huangxin/yolov5_logodet/datasets/images_train')
    except Exception as e:
        print(e)
        print(file)


if __name__ == "__main__":

    with Pool(processes=threads) as p:
        p.map(check_image_opencv, images)
    # check_image_opencv()