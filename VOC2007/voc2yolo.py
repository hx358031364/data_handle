import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import numpy as np
import shutil
import cv2

with open('./label', 'r') as f:
    names = f.read().split('\n')
classes = list(filter(None, names))
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


def convert_annotation(image_id):
    # img = cv2.imread(os.path.join(r'E:\huangxin\rere_baizohu_2\yiwancheng\new\dubiji\jpg', image_id + '.jpg'))
    # h, w, _ = img.shape
    in_file = open(r'E:\huangxin\rere_baizohu_2\yiwancheng\new\gangaotaibi\xml/%s.xml' % (image_id))
    out_file = open(r'E:\huangxin\rere_baizohu_2\yiwancheng\new\gangaotaibi\txt/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:
            print(cls)
            print(image_id)
            continue
        cls_id = classes.index(cls)
        try:
            xmlbox = obj.find('bndbox')
            # b = (float(xmlbox.find('xmin').text) if float(xmlbox.find('xmin').text) >= 0 else 0,
            #      float(xmlbox.find('xmax').text) if float(xmlbox.find('xmax').text) <= w else w,
            #      float(xmlbox.find('ymin').text) if float(xmlbox.find('ymin').text) >= 0 else 0,
            #      float(xmlbox.find('ymax').text) if float(xmlbox.find('ymax').text) <= h else h)
            b = (float(xmlbox.find('xmin').text),
                 float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        except Exception as e:
            print(e)
            print(image_id)
            in_file.close()
            # shutil.move(
            #     os.path.join(r'D:\data\logo\shumei\qingxi\img', image_id + '.jpg'),:-4
            #     r'D:\data\logo\shumei\qingxi\error')
            # shutil.move(
            #     os.path.join(r'D:\data\logo\shumei\qingxi\xml', image_id + '.xml'),
            #     r'D:\data\logo\shumei\qingxi\error')
    in_file.close()
    out_file.close()



jpg_path = r'E:\huangxin\rere_baizohu_2\yiwancheng\new\gangaotaibi\xml'
image_ids = os.listdir(jpg_path)

for image in image_ids:
    image_id = image[:-4]
    convert_annotation(image_id)