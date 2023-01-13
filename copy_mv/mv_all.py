import os
import shutil
import tqdm
i = 0
# 将所有图片移动到一个文件内
dire = r'E:\huangxin\logo_jiansuo\logodet_3k\LogoDet-3K'
for curdir, subdirs, files in os.walk(dire):
    for file in tqdm.tqdm(files):
        if file.endswith('xml'):
            path = os.path.join(curdir, file)
            shutil.move(path, r'E:\huangxin\logo_jiansuo\logodet_3k\all_xml')
            # shutil.copy(path,os.path.join(r'D:\data\xiaoyun\xiaoyun_ceshi',str(i)+'.jpg'))
            # i +=1
