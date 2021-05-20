import os
jpg_path = "D:\\data\\data\\2blood1"
jpg_filelist = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
count=0

for jpg_file in jpg_filelist:   #遍历所有文件
    jpg_Olddir=os.path.join(jpg_path,jpg_file)   #原来的文件路径
    if os.path.isdir(jpg_Olddir):   #如果是文件夹则跳过
        continue
    jpg_filename=os.path.splitext(jpg_file)[0]   #文件名
    # jpg_filetype=os.path.splitext(jpg_file)[1]   #文件扩展名
    jpg_filetype=".jpg"
    jpg_Newdir = os.path.join(jpg_path, str(count).zfill(6) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
    os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
    count += 1
print(count)