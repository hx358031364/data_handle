import os
import random
import shutil


def cpfile_rand(img, outfile, num):
    list_ = os.listdir(img)
    if num > len(list_):
        print('输出数量必须小于：', len(list_))
        exit()
    numlist = random.sample(range(0, len(list_)), num)  # 生成随机数列表a
    cnt = 0
    xml_path = "D:\\data\\logo_yolo\\gz_mb\\1rotatexml\\"
    new_xml_path = "D:\\data\\1a\\"
    for n in numlist:
        filename = list_[n]
        name = filename.split(".")[0]
        oldpath = os.path.join(img, filename)
        newpath = os.path.join(outfile, filename)
        xml_oldpath = os.path.join(xml_path, name+".xml")
        new_xml_oldpath = os.path.join(new_xml_path, name+".xml")
        shutil.copy(oldpath, newpath)
        shutil.copy(xml_oldpath, new_xml_oldpath)
        print('剩余文件：', num - cnt)
        cnt = cnt + 1
    print('==========task OK!==========')


if __name__ == "__main__":
    file_path = "D:\\data\\logo_yolo\\gz_mb\\1rotate\\"
    out_path = "D:\\data\\1\\"
    cpfile_rand(file_path, out_path, 5000)  # 操作目录，输出目录，输出数量