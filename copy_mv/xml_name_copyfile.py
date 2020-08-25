import os
import shutil
listdir = os.listdir('D:\\data\\新logo增加数据\\xml')
for file in listdir:
    name = file.split(".")[0]
    file_name = name+'.jpg'
    jpg_file = os.path.join('D:\\data\\新logo增加数据\\jpg', file_name)
    shutil.copyfile(os.path.join('D:\\data\\resulet\\103类\\best_1\\no_object',file_name), jpg_file)
