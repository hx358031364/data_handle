import cv2
import xml.dom.minidom
import os

img_list = os.listdir(r'D:\data\xiaoyun\tubiao\tubiao\img')
path = r'D:\data\xiaoyun\tubiao\tubiao\xml'
outdir = r'D:\data\xiaoyun\tubiao\tubiao\crop'
i = 0
for jpg_name in img_list:
    im = cv2.imread(os.path.join(r'D:\data\xiaoyun\tubiao\tubiao\img', jpg_name))
    xml_name = jpg_name.split(".")[0] + '.xml'
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
    else:
        for root_i in range(length):
            now_name_list = object_root[root_i].getElementsByTagName('name')[0].childNodes
            if len(now_name_list) == 0:
                print(xml_name, 'name is none')
            label_name = now_name_list[0].nodeValue
            save_dir = os.path.join(outdir, label_name)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            # 查看坐标是否有问题
            xmlbox = object_root[root_i].getElementsByTagName('bndbox')
            xmin = float(xmlbox[0].getElementsByTagName('xmin')[0].childNodes[0].nodeValue)
            xmax = float(xmlbox[0].getElementsByTagName('xmax')[0].childNodes[0].nodeValue)
            ymin = float(xmlbox[0].getElementsByTagName('ymin')[0].childNodes[0].nodeValue)
            ymax = float(xmlbox[0].getElementsByTagName('ymax')[0].childNodes[0].nodeValue)

            # xyxy = [[int(xmin), int(ymin), int(xmax), int(ymax)]]

            crop = im[int(ymin):int(ymax), int(xmin):int(xmax), ::(1 if True else -1)]
            # cv2.imwrite(os.path.join(save_dir,'label_name_'+str(i)+'.jpg'), crop)
            cv2.imencode('.jpg', crop)[1].tofile(
                os.path.join(save_dir, 'label_name_' + str(i) + '.jpg'))
            i += 1
