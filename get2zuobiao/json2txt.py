# coding: utf-8
import os
import pandas as pd
import json

def urllib_download(IMAGE_URL,save_path):
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, save_path)
with open("1.txt") as f:
    line_list = f.readlines()
    for line in line_list:
        data = json.loads(line)
        content = data["content"]
        taskName = data["taskName"] #公章
        name = data["name"] #图片名
        path = data["path"] #图片地址
        for i in content:
            labelName =  i["labelName"]
            if labelName == '公章':
                file_name = name.split(".")
                area = i["area"]
                try:
                   x1 = area['x']
                   y1 = area['y']
                   x2 = x1 + area['xlen']
                   y2 = y1 + area['ylen']
                except:
                   print(file_name)
                out_file = open('D:\\data\\logo\\gongzhang\\txt/%s.txt' % (file_name[0]), 'w')
                out_file.write(str(102) + '\n' + str(x1) + '\n' + str(y1) + '\n' + str(x2) + '\n' + str(y2) + '\n')
                out_file.close()
                urllib_download(path,'D:\\data\\logo\\gongzhang\\img\\{}'.format(name))

