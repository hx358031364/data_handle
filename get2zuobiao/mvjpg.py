from PIL import Image
import os,shutil


def move_file():
    jpg_files = 'D:\\data\\tv_source_data\\weishi\\hebei,ok\\'
    listdir = os.listdir(jpg_files)

    out_path = 'D:\\data\\tv_source_data\\test\\hebei_oth\\'

    for jpe_file in listdir:
        file_path = os.path.join(jpg_files, jpe_file)
        img_pillow = Image.open(file_path)
        img_width = img_pillow.width  # 图片宽度
        img_height = img_pillow.height  # 图片高度

        print(img_width,img_height)
        if img_width == 960 and img_height == 540:
            shutil.copyfile(file_path, os.path.join(out_path, jpe_file))
if __name__ == '__main__':
    move_file()