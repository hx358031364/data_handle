# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
import json
from multiprocessing import Pool
from urllib.request import urlopen
# URL到图片
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    # bytearray将数据转换成（返回）一个新的字节数组
    # asarray 复制数据，将结构化数据转换成ndarray
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # cv2.imdecode()函数将数据解码成Opencv图像格式
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

data_path = r'D:\data\logo\qingxi\爬取\logo'
listdir = os.listdir(data_path)
threads = 4


def down_img(label_file):
        txt = open(os.path.join(data_path, label_file), encoding='utf-8')
        json_txt = json.load(txt)
        for file_path in json_txt:
            path_list = file_path['pic_list'].split('|')
            for i in range(1,int(path_list[1])):
                url = 'http://oss-saas-1.oss-cn-beijing.aliyuncs.com/saas/'+path_list[0]+'/thumb/'+str(i)+'.jpg'
                print(url)
                try:
                    image = url_to_image(url)
                    sava_path = os.path.join(r'E:\huangxin\oss',label_file,
                                             path_list[0].split('/')[-1] + '_' + str(i) + '.jpg')
                    cv2.imwrite(sava_path,image)
                except Exception as e:
                    print(e)
                    print(url)

# down_img('qinghai')

if __name__ == "__main__":
    with Pool(processes=threads) as p:
        p.map(down_img, listdir)
    # check_image_opencv()