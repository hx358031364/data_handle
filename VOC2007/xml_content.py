# coding=utf-8
import os
import xml.dom.minidom
import cv2
import warnings
# warnings.filterwarnings('default')

import shutil
# jpg对应文件夹
jpg_path = r'E:\huangxin\rere_biaozhu_res\dao\dao\dao_all'
# 储存xml文件的文件夹的路径
path = r'E:\huangxin\rere_biaozhu_res\dao\dao_XML'
# 得到文件夹下所有文件名称
jpgs = os.listdir(jpg_path)
i = 1
label = []
for jpg_name in jpgs:  # 遍历文件夹
    # print('修改第' + str(i) + '个xml' + ' 名字是:' + xml_name)
    i = i + 1
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
        f.close()
        # shutil.move(xml_path,r'D:\data\logo\biaozhu\error')
        # shutil.move(os.path.join(jpg_path,xml_name.replace('xml','jpg')),r'D:\data\logo\biaozhu\error')
        print(xml_name, ' is not object')
    else:
        for root_i in range(length):
            now_name = object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue
            if now_name not in label:
                label.append(now_name)
        #     if now_name =='216_49':
        #         object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue='216_48'
        #         i_216+=1
        #     if now_name =='82_138':
        #         object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue='133_3'
        #         i_133+=1
        # # now_box = object_root[root_i].getElementsByTagName('bndbox')
    #获取标签对应的图片信息
    # jpg_name = xml_name.split(".")[0]
    try:
        img = cv2.imread(os.path.join(jpg_path, jpg_name))
        cv2.resize(img, (640, 640))
    except Exception as e:
        print(e)
        print(jpg_path)
    if img is None:
        print(jpg_name, ' is none')
        # shutil.move(os.path.join(jpg_path, jpg_name + '.jpg'),r'D:\data\logo\biaozhu\none')
        # shutil.move(xml_path, r'D:\data\logo\biaozhu\none')
    else:
        h, w, _ = img.shape
        size = old_xml.getElementsByTagName("size")
        if size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue != str(w):
            print('xml_w!=img_w,img:', xml_name)

        if size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue != str(h):
            print('xml_h!=img_h,img:', xml_name)

        # if size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue == str(w) and \
        #         size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue == str(h):
        #     # 获取标签值 ,获得你想要修改的值并修改
        #     size = old_xml.getElementsByTagName("size")
        #     size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = w
        #     size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = h

            # 重命名folder,filename,path
            # if len(old_xml.getElementsByTagName("folder")) != 0:
            #     old_xml.getElementsByTagName("folder")[0].firstChild.data = 'JPEGImages'
            # if len(old_xml.getElementsByTagName("filename")) != 0:
            #     old_xml.getElementsByTagName("filename")[0].firstChild.data =jpg_name + '.jpg'
            # if len( old_xml.getElementsByTagName("path")) != 0:
            #     old_xml.getElementsByTagName("path")[0].firstChild.data = 'JPEGImages/'+jpg_name + '.jpg'


            # 保存修改到xml文件中
            # with open(xml_path, 'w') as f:
            #     dom.writexml(f)
        # else:
        #     print(xml_name)
# print('保存修改成功！！！')
print(label)