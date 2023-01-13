# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
import json
from multiprocessing import Pool
from urllib.request import urlopen
import pandas as pd
# # URL到图片
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
def convert(size, box):
    l =  []
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    l = [x, y, w, h]
    l = np.array(l, dtype=np.float32)
    assert (l >= 0).all(), 'negative labels'
    assert (l <= 1).all(), 'non-normalized or out of bounds coordinate labels'
    return (x, y, w, h)


def down_img(sheet_name):
    i = 0
    df = pd.read_excel(data_xls, sheet_name=sheet_name, header=None)
    datas = df[1:].values
    # if sheet_name=='2022-03-29':
    # 	datas = df[30006:].values
    for data in datas:
        jpg_url = data[2]
        # b = (data[5], data[7], data[6], data[8])
        # label_name = data[2]
        # score = data[3]
        # img_name = str(score) + '_' + jpg_url.split('/')[-3] + '_' + jpg_url.split('/')[-1]
        # img_name = jpg_url.split('/')[-2] + '_' + jpg_url.split('/')[-1]
        # save_path = os.path.join(save_root, sheet_name, label_name)
        # # 判断是否已经存在该目录
        # if not os.path.exists(save_path):
        # 	# 目录不存在，进行创建操作
        # 	os.makedirs(save_path)  # 使用os.makedirs()方法创建多层目录
        try:
            # i += 1
            jpg_name = jpg_url.split('/')[-2]+'_'+jpg_url.split('/')[-1]
            image = url_to_image(jpg_url)
            # h, w, _ = image.shape
            cv2.imwrite(os.path.join(save_root, jpg_name), image)

            # out_file = open(r'C:\Users\rmzk\Desktop\weini\txt/%s.txt' % (str(i)), 'w')
            # bb = convert((w, h), b)
            # out_file.write(str(240) + " " + " ".join([str(a) for a in bb]) + '\n')


        except Exception as e:
            print(e)
            print(jpg_url)


save_root = r'/mnt/storage/TEST_DATA/shenhe_fankui/20220921'
data_xls = pd.io.excel.ExcelFile(r'shenhe.xlsx')
sheets = data_xls.sheet_names
print(sheets)
if __name__ == "__main__":
	# with Pool(processes=6) as p:
	#     p.map(down_img, sheets)
	# for sheet in sheets:
		down_img('shenhe')
