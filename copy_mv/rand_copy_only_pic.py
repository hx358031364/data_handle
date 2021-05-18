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
        newpath = os.path.join(outfile,floder, filename)
        print(newpath)
        # shutil.copy(oldpath, newpath)
        shutil.move(oldpath, newpath)
        print('剩余文件：', num - cnt)
        cnt = cnt + 1
    print('==========task OK!==========')

if __name__ == "__main__":
    file_folders = "/home/huangxin/work/testcode/all_train_data/zhongfu_datasets/train"
    out_path = "/home/huangxin/work/testcode/all_train_data/zhongfu_datasets/validation"
    for floder in os.listdir(file_folders):
        file_path = os.path.join(file_folders, floder)
        cpfile_rand(file_path, out_path, floder, 500)  # 操作目录，输出目录，输出数量
