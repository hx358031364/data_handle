import os
jpg_path = r"E:\huangxin\logo_jiansuo\logodet_3k\LogoDet-3K\Transportation"
file_folders = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
for jpg_floder in file_folders:
    jpg_filelist = os.listdir(os.path.join(jpg_path,jpg_floder))
    # count=0
    qianzhui = jpg_floder
    if ' ' in jpg_floder:
        qianzhui = jpg_floder.replace(' ','_')
    for jpg_file in jpg_filelist:   #遍历所有文件
        jpg_Olddir = os.path.join(jpg_path, jpg_floder, jpg_file)  # 原来的文件路径
        if os.path.isdir(jpg_Olddir):   #如果是文件夹则跳过
            continue
    #     jpg_filename = os.path.splitext(jpg_file)[0]  # 文件名
    #     # jpg_filetype=os.path.splitext(jpg_file)[1]   #文件扩展名
    #     jpg_filetype=".jpg"
    #     jpg_Newdir = os.path.join(jpg_path+jpg_floder, str(count).zfill(8) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
    #     os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
    #     count += 1
    # print(count)
        new_name = qianzhui + '_' + jpg_file
        jpg_new = os.path.join(jpg_path, jpg_floder, new_name)
        os.rename(jpg_Olddir, jpg_new)
