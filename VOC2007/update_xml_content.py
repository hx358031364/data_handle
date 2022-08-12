# coding=utf-8
import os
import xml.dom.minidom
import cv2
import warnings
# warnings.filterwarnings('default')

import shutil
# jpg对应文件夹
jpg_path = r'E:\huangxin\rere_fanxiu\result\jinghui\riwirte'
# 储存xml文件的文件夹的路径
path = r'E:\huangxin\rere_fanxiu\result\jinghui\xml'
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
    # 使用minidom解析器打开 XML 文档
    dom = xml.dom.minidom.parseString(text)
    old_xml = dom.documentElement

    # 重命名folder,filename,path
    if len(old_xml.getElementsByTagName("folder")) != 0:
        old_xml.getElementsByTagName("folder")[0].firstChild.data = 'JPEGImages'
    if len(old_xml.getElementsByTagName("filename")) != 0:
        old_xml.getElementsByTagName("filename")[0].firstChild.data =jpg_name + '.jpg'
    if len( old_xml.getElementsByTagName("path")) != 0:
        old_xml.getElementsByTagName("path")[0].firstChild.data = 'JPEGImages/'+jpg_name + '.jpg'

    # 图片宽高修改
    img = cv2.imread(os.path.join(jpg_path, jpg_name))
    h, w, _ = img.shape
    size = old_xml.getElementsByTagName("size")
    size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = w
    size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = h

    # 修改object内容
    root = dom.documentElement
    object_root = root.getElementsByTagName('object')
    length = len(object_root)
    # print(length)
    if length == 0:
        f.close()
        print(xml_name, ' is not object')
    else:
        for root_i in range(length):
            object_root[root_i].getElementsByTagName('name')[0].childNodes[0].nodeValue = 'name'



    # 保存修改到xml文件中
    with open(xml_path, 'w') as f:
        dom.writexml(f)
# print('保存修改成功！！！')