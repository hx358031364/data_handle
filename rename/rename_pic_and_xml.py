import os

jpg_path = r"E:\huangxin\rere_baizohu_2\yiwancheng\pijiu\jpg"
xml_path = r"E:\huangxin\rere_baizohu_2\yiwancheng\pijiu\xml"
jpg_filelist = os.listdir(jpg_path)  # 该文件夹下所有的文件（包括文件夹）
xml_filelist = os.listdir(xml_path)  # 该文件夹下所有的文件（包括文件夹）
count = 632640

for jpg_file in jpg_filelist:  # 遍历所有文件
    jpg_Olddir = os.path.join(jpg_path, jpg_file)  # 原来的文件路径
    if os.path.isdir(jpg_Olddir):  # 如果是文件夹则跳过
        continue
    jpg_filename = jpg_file[:-4]  # 文件名
    jpg_filetype = '.jpg'  # 文件扩展名
    xml_Olddir = os.path.join(xml_path, jpg_filename+'.xml')  # 原来的文件路径
    jpg_Newdir = os.path.join(jpg_path, 'waibi_' + str(count).zfill(6) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
    xml_Newdir = os.path.join(xml_path, 'waibi_'+str(count).zfill(6) + '.xml')  # 用字符串函数zfill 以0补全所需位数
    os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
    os.rename(xml_Olddir, xml_Newdir)  # 重命名
    count += 1
    # for xml_file in xml_filelist:
    #     xml_Olddir = os.path.join(xml_path, xml_file)  # 原来的文件路径
    #     if os.path.isdir(xml_Olddir):  # 如果是文件夹则跳过
    #         continue
    #     xml_filename = os.path.splitext(xml_file)[0]  # 文件名
    #     xml_filetype = os.path.splitext(xml_file)[1]  # 文件扩展名
    #     if jpg_filename == xml_filename:
    #         jpg_Newdir = os.path.join(jpg_path,
    #                                   'bg_'+str(count) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
    #         xml_Newdir = os.path.join(xml_path,
    #                                   'bg_'+str(count) + xml_filetype)  # 用字符串函数zfill 以0补全所需位数
    #         os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
    #         os.rename(xml_Olddir, xml_Newdir)  # 重命名
    # count += 1