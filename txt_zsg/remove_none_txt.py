import os
import shutil

files = "/data2/yolov5_logodet/datasets/labels/val"
file_list = os .listdir(files)
for file in file_list:
    file_path = os.path.join(files, file)
    if not os.path.getsize(file_path):
        try:
            shutil.move(file_path,'none')
            name_jpg = file.replace('.txt','.jpg')
            shutil.move(os.path.join('yolov5_logodet/datasets/images/val', name_jpg), 'none')
        except Exception as e:
            print(file)
        # os.remove(file