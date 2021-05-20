import os
from glob import glob
"""
xml,jpg在同一个文件下，修改jpg的同时修改xml
"""
jpg_path = r"E:/20210414_OKR_task/log_result"

count = 0
for root,dirs_name,files_name in os.walk(jpg_path):
    for i in glob(root+'/*.jpg'):
        splitext = os.path.splitext(i)[0]
        name = splitext.split("\\")[-1]
        new_name = str(count).zfill(8)
        os.rename(splitext+'.jpg', root+"\\"+new_name+'.jpg')  # 重命名
        os.rename(splitext+'.xml', root+"\\"+new_name+'.xml')  # 重命名
        print(i)
        count +=1
print(count)
