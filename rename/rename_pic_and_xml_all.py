import os
from glob import glob
jpg_path = r"E:/20210414_OKR_task/log_result"
# jpg_path = r"D:/data/gz/resize/tttt/*"
# xml_path = "D:\\data\\gz\\xml\\"
# jpg_filelist = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
# xml_filelist = os.listdir(xml_path) #该文件夹下所有的文件（包括文件夹）
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
# jpg_name_list = glob(jpg_path + '/*jpg')


# for jpg_file in jpg_name_list:
#     splitext = os.path.splitext(jpg_file)[0]
#     new_name = splitext+'_'+str(count)
#     # os.rename(splitext+'.jpg', new_name+'.jpg')  # 重命名
#     # os.rename(splitext+'.xml', new_name+'.xml')  # 重命名
#     print(new_name)
#     count +=1
# print(count)
# for jpg_file in jpg_filelist:  # 遍历所有文件
#     jpg_Olddir = os.path.join(jpg_path, jpg_file)  # 原来的文件路径
#     if os.path.isdir(jpg_Olddir):  # 如果是文件夹则跳过
#         continue
#     jpg_filename = os.path.splitext(jpg_file)[0]  # 文件名
#     jpg_filetype = os.path.splitext(jpg_file)[1]  # 文件扩展名
#     for xml_file in xml_filelist:
#         xml_Olddir = os.path.join(xml_path, xml_file)  # 原来的文件路径
#         if os.path.isdir(xml_Olddir):  # 如果是文件夹则跳过
#             continue
#         xml_filename = os.path.splitext(xml_file)[0]  # 文件名
#         xml_filetype = os.path.splitext(xml_file)[1]  # 文件扩展名
#         if jpg_filename == xml_filename:
#             jpg_Newdir = os.path.join(jpg_path, "gz_" + str(count).zfill(7) + jpg_filetype)  # 用字符串函数zfill 以0补全所需位数
#             xml_Newdir = os.path.join(xml_path, "gz_" + str(count).zfill(7) + xml_filetype)  # 用字符串函数zfill 以0补全所需位数
#             os.rename(jpg_Olddir, jpg_Newdir)  # 重命名
#             os.rename(xml_Olddir, xml_Newdir)  # 重命名
#     count += 1
# print(count)
