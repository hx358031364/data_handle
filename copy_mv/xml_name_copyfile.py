import os
import shutil
listdir = os.listdir(r'E:\huangxin\rere_baizohu_2\yiwancheng\new\shuzhongzhi\jpg')
for file in listdir:
    name = file[:-4]
    file_name = name+'.xml'
    txt_file = os.path.join(r'E:\huangxin\rere_baizohu_2\yiwancheng\new\shuzhongzhi\xml', file_name)
    shutil.move(txt_file, r'E:\huangxin\rere_baizohu_2\yiwancheng\new\shuzhongzhi\new_xml')
