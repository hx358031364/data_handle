"""
对图片和标注文件xml缩放
"""

# -*-coding: UTF -8-*-
###############################
# 按照图片最短边缩放到512的比例对图片进行缩小或者放大
# 同时对XML进行更改
###############################
import cv2
import sys
import os
import xml.dom.minidom as minidom


def resize_xml(xmlname, xml_path, result_path):
    # print(xmlname)
    try:
        jpgname = xmlname.split(".")[0]
        file_path = "D:\\data\\logo_yolo\\mb_augment\\jpg\\{}.jpg".format(jpgname)

        pre_image = cv2.imread(file_path)
        pre_height = pre_image.shape[0]  # 垂直像素
        pre_width = pre_image.shape[1]  # 水平像素

        annotation = minidom.parse(xml_path)
        size = annotation.getElementsByTagName("size")
        # width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
        # height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
        width = int(str(pre_height))
        height = int(str(pre_width))

        size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = str(pre_width)
        size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = str(pre_height)

        f = open(os.path.join(result_path, xmlname), 'w')
        annotation.writexml(f, encoding='utf-8')
        f.close()
    except:
        print(xmlname)


if __name__ == "__main__":
    XML_path = 'D:\\data\\logo_yolo\\mb_augment\\xml\\'
    XML_out = './resize_xml/'


    print("xml started")
    for xml_file in os.listdir(XML_path):
        xmlname = xml_file
        xml = os.path.join(XML_path, xmlname)
        resize_xml(xmlname, xml, XML_out)
    print("process finish\n")