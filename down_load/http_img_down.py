# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
import json
from multiprocessing import Pool
from urllib.request import urlopen
from tqdm import tqdm

# URL到图片
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    print(url)
    resp = urlopen(url)
    # bytearray将数据转换成（返回）一个新的字节数组
    # asarray 复制数据，将结构化数据转换成ndarray
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # cv2.imdecode()函数将数据解码成Opencv图像格式
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

data_path = r'D:\data\SZK_data\zhuaqu\all_img'
listdir = os.listdir(data_path)
threads = 1
save_path = r'E:\huangxin\SZK\baidu_360_sougou'

def down_img(folder_list):
    for folder in folder_list:
        # pathOut = os.path.join(save_path, folder)
        # try:
        #     os.mkdir(pathOut)
        # except OSError:
        #     pass
        txt_files = os.listdir(os.path.join(data_path, folder))
        for file in txt_files:
            pathOut = os.path.join(save_path, folder, file[:-4])
            try:
                os.makedirs(pathOut)
            except OSError:
                pass
            txt = open(os.path.join(data_path, folder, file), encoding='utf-8')
            for i, (line) in tqdm(enumerate(txt)):
                try:
                    url = line.strip('\n')
                    image = url_to_image(url)
                    # jpg_name = file[:-4]+'_'+ str(i) + '.jpg'
                    jpg_name = str(i) + '.jpg'
                    cv2.imwrite(os.path.join(pathOut,jpg_name), image)
                except Exception as e:
                    pass

# down_img('qinghai')

if __name__ == "__main__":
    # with Pool(processes=threads) as p:
    #     p.map(down_img, listdir)
    down_img(listdir)