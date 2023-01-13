import os
import random
import shutil

def cpfile_rand(img, outfile,floder, num):
    list_ = os.listdir(img)
    if num > len(list_):
        print('输出数量必须小于：', len(list_))
        exit()
    numlist = random.sample(range(0, len(list_)), num)  # 生成随机数列表a
    cnt = 0
    for n in numlist:
        filename = list_[n]
        oldpath = os.path.join(img, filename)
        # newname = floder+'_'+filename
        # newpath = os.path.join(outfile, 'guoqi_touxiang_'+filename)
        # print(newpath)
        shutil.copy(oldpath, outfile)
        # shutil.move(oldpath, newpath)
        print('剩余文件：', num - cnt)
        cnt = cnt + 1
    print('==========task OK!==========')

if __name__ == "__main__":
    file_folders = r'E:\huangxin\logo_jiansuo\logos_in_the_wild\data_cleaned\voc_format'
    out_path = r'E:\huangxin\logo_jiansuo\logos_in_the_wild\data_cleaned\single_cls_xml'
    for floder in os.listdir(file_folders):
        file_path = os.path.join(file_folders, floder)
        cpfile_rand(file_path, out_path, floder, 1)  # 操作目录，输出目录，输出数量
