import os
import cv2
import random
import numpy as np
import albumentations as A
from subprocess import check_call
import subprocess
from multiprocessing import Pool, cpu_count
from functools import partial


# 目标图标
obj_root = "D:\\data\\logo\\tb\\"
# 背景图片
bk_root = "D:\\data\\logo\\oss_url_result\\no_objects\\jpg\\"
# 保存路径
save_root = "D:\\data\\logo\\genrata_data\\img\\"
save_txt = "D:\\data\\logo\\genrata_data\\txt\\"

obj_names = os.listdir(obj_root)
bk_names = os.listdir(bk_root)

def convert(size, box):  # size的图片大小(w*h)
    '''坐标转化函数'''
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def create_img(obj_name):
    # 随机获取目标图
    # obj_name = obj_names[random.randint(0,len(obj_names)-1)]
    obj_img = cv2.imread(obj_root + obj_name,cv2.IMREAD_UNCHANGED)
    # 随机选取背景图
    bk_name = bk_names[random.randint(0,len(bk_names)-1)]
    bk_img = cv2.imread(bk_root + bk_name)

    obj_h, obj_w, _ = obj_img.shape

    # 按照背景图的比例缩放logo
    p_list = [0.1, 0.1, 0.1, 0.1, 0.2, 0.25, 0.3]
    scale = random.sample(p_list, 1)[0]
    bk_h, bk_w, _ = bk_img.shape

    # if bk_h > bk_w:
    obj_rez_w = int(bk_w*scale)
    obj_rez_h = int(obj_rez_w/obj_w*obj_h)
    resize_obj = cv2.resize(obj_img, (obj_rez_w, obj_rez_h))

    x = random.randint(0, bk_w - obj_rez_w)
    y = random.randint(0, bk_h - obj_rez_h)

    if resize_obj.shape[2] == 3:
        b_channel, _, _ = cv2.split(resize_obj)
        mask = np.ones(b_channel.shape, dtype=b_channel.dtype)
    else:
        mask = resize_obj[:, :, 3] / 255

    bk_img[y:y + obj_rez_h, x:x + obj_rez_w, :] = bk_img[y:y + obj_rez_h, x:x + obj_rez_w,:] * (1 - mask)[:, :, None] + resize_obj[:,:, :3] * mask[:, :,None]

    # obj_img = bk_img[y:y + obj_rez_h, x:x + obj_rez_w].copy()

    cv2.imwrite(os.path.join(save_root, 'qinghai_' + str(i) + ".jpg"), bk_img)

    #
    out_file = open('%s/%s.txt' % (save_txt, 'qinghai_'+str(i)), 'w')  # 输出路径
    # for (x, y, cor_w, cor_h) in paste_box:
    b = (float(x), float(x + obj_rez_w), float(y), float(y + obj_rez_h))  # xml中坐标信息
    bb = convert((bk_w, bk_h), b)  # 图片的w,h,dtype=int
    out_file.write(str(40) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == '__main__':
    for i in obj_names:
        create_img(i)
