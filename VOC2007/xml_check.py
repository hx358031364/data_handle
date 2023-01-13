# coding=utf-8
import os
import xml.dom.minidom
import cv2
from collections import Counter
import shutil
# jpg对应文件夹
jpg_path = r'/mnt/storage/customize_logo/mm2021_openbrands_datasets/open_brand_voc_label_source/annotations'
# xml文件路径
path = r'/mnt/storage/customize_logo/mm2021_openbrands_datasets/open_brand_voc_label_source/annotations'
jpgs = os.listdir(jpg_path)

xmls = os.listdir(path)
if len(jpgs) != len(xmls):
    print('jpg与xml不对应')


label = []

with open('./unknown_200', 'r') as f:
    names = f.read().split('\n')
names_list = list(filter(None, names))

for jpg_name in jpgs:  # 遍历文件夹
    img_bool = False
    xml_bool = False
    # 得到一个xml完整的路径
    xml_name = jpg_name.split(".")[0]
    xml_name = xml_name+'.xml'
    xml_path = os.path.join(path, xml_name)
    # 读取xml
    # dom = xml.dom.minidom.parse(xml_path)
    f = open(xml_path, "r", encoding='utf-8')
    r = f.read()
    text = str(r.encode('utf-8'), encoding="utf-8")
    # print(text)
    # 使用minidom解析器打开 XML 文档
    dom = xml.dom.minidom.parseString(text)
    old_xml = dom.documentElement
    root = dom.documentElement
    object_root = root.getElementsByTagName('object')
    length = len(object_root)
    # print(length)
    if length == 0:
        print(xml_name, ' is not object')
        xml_bool = True
    else:
        for root_i in range(length):
            now_name_list = object_root[root_i].getElementsByTagName('name')[0].childNodes
            if len(now_name_list) == 0:
                print(xml_name, 'name is none')
                xml_bool = True
            # 如果name没在预设标签中，保存错误label名称
            elif now_name_list[0].nodeValue not in names_list:
                try:
                    print('not the name')
                    label.append(now_name_list[0].nodeValue)
                except Exception as e :
                    print(e)
                    print(jpg_name)
                xml_bool = True
            # 查看坐标是否有问题
            xmlbox = object_root[root_i].getElementsByTagName('bndbox')
            xmin = float(xmlbox[0].getElementsByTagName('xmin')[0].childNodes[0].nodeValue)
            xmax = float(xmlbox[0].getElementsByTagName('xmax')[0].childNodes[0].nodeValue)
            ymin = float(xmlbox[0].getElementsByTagName('ymin')[0].childNodes[0].nodeValue)
            ymax = float(xmlbox[0].getElementsByTagName('ymax')[0].childNodes[0].nodeValue)
            if xmax - xmin < 10 or ymax - ymin < 10:
                print(xml_name, 'box error')
                xml_bool = True
    try:
        img = cv2.imread(os.path.join(jpg_path, jpg_name))
        h, w, _ = img.shape
        cv2.resize(img, (640, 640))
    except Exception as e:
        print(e)
        print(jpg_path)
        img_bool = True
    if img is None:
        img_bool = True
        print(jpg_name, ' is none')
    else:
        h, w, _ = img.shape
        size = old_xml.getElementsByTagName("size")
        if size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue != str(w):
            print('xml_w!=img_w,img:', xml_name)
            xml_bool = True
        if size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue != str(h):
            print('xml_h!=img_h,img:', xml_name)
            xml_bool = True
    if img_bool or xml_bool:
        f.close()
        # shutil.move(xml_path, r'E:\huangxin\rere_baizohu_2\yiwancheng\new\shuzhongzhi\error')
        # shutil.move(os.path.join(jpg_path, jpg_name), r'E:\huangxin\rere_baizohu_2\yiwancheng\new\shuzhongzhi\error')

print(label)


# 统计标签数量
# count = Counter(label)
# print(count)
# 输出元素3的个数
# print(count[3])
