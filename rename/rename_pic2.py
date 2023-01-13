'''
1.加前缀，不改原来的名字/
2.只在后面加个.jpg后缀
'''
import os
jpg_path = r"C:\Users\rmzk\Desktop\wode"
# jpg_filelist = os.listdir(jpg_path) #该文件夹下所有的文件
# i = 0
# for jpg_file in jpg_filelist:   #遍历所有文件
#     jpg_Olddir = os.path.join(jpg_path, jpg_file)  # 原来的文件路径
#     if os.path.isdir(jpg_Olddir):   #如果是文件夹则跳过
#         continue
#     name = 'RMW_det_' + jpg_file
#     jpg_Newdir = os.path.join(jpg_path, name)  # 用字符串函数zfill 以0补全所需位数
#     os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
#     i +=1



count = 0
def get_all_files(dir):
    files_ = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_


files = get_all_files(jpg_path)
print(files)

for f in files:
    os.rename(f,f+str(count)+".jpg")
    count+=1
