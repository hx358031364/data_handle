import os
jpg_path = "C:\\Users\\DELL\\Desktop\\luoding"
xml_path = "C:\\Users\\DELL\\Desktop\\label"
jpg_filelist = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
xml_filelist = os.listdir(xml_path) #该文件夹下所有的文件（包括文件夹）
count=1

for jpg_file in jpg_filelist:   #遍历所有文件
    jpg_Olddir=os.path.join(jpg_path,jpg_file)   #原来的文件路径
    if os.path.isdir(jpg_Olddir):   #如果是文件夹则跳过
        continue
    jpg_filename=os.path.splitext(jpg_file)[0]   #文件名
    jpg_filetype=os.path.splitext(jpg_file)[1]   #文件扩展名
    for xml_file in xml_filelist:
        xml_Olddir = os.path.join(xml_path, xml_file)  # 原来的文件路径
        if os.path.isdir(xml_Olddir):  # 如果是文件夹则跳过
            continue
        xml_filename = os.path.splitext(xml_file)[0]  # 文件名
        xml_filetype = os.path.splitext(xml_file)[1]  # 文件扩展名
        if jpg_filename == xml_filename:
            jpg_Newdir = os.path.join(jpg_path, str(count).zfill(6) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
            xml_Newdir = os.path.join(xml_path, str(count).zfill(6) + xml_filetype)  # 用字符串函数zfill 以0补全所需位数
            os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
            os.rename(xml_Olddir, xml_Newdir)  # 重命名
    count += 1