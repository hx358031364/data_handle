'''
获取图片任意位置框的坐标
'''
from PIL import Image
import os.path

def get_bounding_box(jpgfile):
    # img_pillow = Image.open(jpgfile)
    # img_width = img_pillow.width  # 图片宽度
    # img_height = img_pillow.height  # 图片高度

    # 640*360
    # x1 = int(img_width * 0.042)
    # y1 = int(img_height * 0.044)
    # x2 = int(img_width * 0.2)
    # y2 = int(img_height * 0.18)

    # weishi
    # x1 = int(img_width * 0.0453125)
    # y1 = int(img_height * 0.052778)
    # x2 = int(img_width * 0.2296875)
    # y2 = int(img_height * 0.1666667)
    x1 = 50
    y1 = 34
    x2 = 171
    y2 = 89

    # 852*480
    # x1 = int(img_width * 0.061)
    # y1 = int(img_height * 0.0625)
    # x2 = int(img_width * 0.203)
    # y2 = int(img_height * 0.175)
    return x1, y1, x2, y2


jpg_files = 'D:\\data\\tv_source_data\\test\\cctv5+\\'
# jpg_files = 'D:\\data\\tv_source_data\\weishi\\zhejiang,ok\\'
listdir = os.listdir(jpg_files)

for jpe_file in listdir:
    file_path = os.path.join(jpg_files,jpe_file)
    x1, y1, x2, y2 = get_bounding_box(file_path)
    file_name = jpe_file.split(".")
    print(file_name[0])
    out_file = open('D:\\data\\tv_source_data\\txt/%s.txt' % (file_name[0]), 'w')
    out_file.write(str(5) + '\n' + str(x1) + '\n' + str(y1) + '\n' + str(x2) + '\n' + str(y2) + '\n')
    out_file.close()