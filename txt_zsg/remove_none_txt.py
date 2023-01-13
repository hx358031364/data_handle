import os
import shutil

# files = r"E:\huangxin\data\logo_det\RMB\labels"
files = r"E:\huangxin\xiaoyun\unique_uis\txt"
file_list = os .listdir(files)
for file in file_list:
    file_path = os.path.join(files, file)
    if not os.path.getsize(file_path):
        try:
            shutil.move(file_path,r'E:\huangxin\xiaoyun\unique_uis\error')
            # name_jpg = file.replace('.txt','.jpg')
            # shutil.move(os.path.join(r'E:\huangxin\rere_fanxiu\result\huozai-ok\rewrite', name_jpg), r'E:\huangxin\rere_fanxiu\result\huozai-ok\none')
        except Exception as e:
            print(file)
        # os.remove(file