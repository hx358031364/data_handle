import os
import cv2
import random
import numpy as np
from subprocess import check_call
import subprocess
from multiprocessing import Pool, cpu_count
from functools import partial

'''
台标算法的贴图代码 by zhangchao
feature：
限制了在图像四个角位置贴图，1/4范围内
右侧台标可能有少量的超出图片位置
一张背景图贴4个相同的台标
每个类别的图片放在一个单独的文件夹内
台标的长宽有20%的概率在0.9-1.1倍内的范围浮动

贴图过程：
从背景图中随机获取一张图片，获取完logo后根据背景图大小resize logo的大小，
以满足1/4的需求，在1/4范围内进行logo贴图，保存贴图后图片和yolov3所需的标
注文件（相对坐标） 

当前代码问题，暂未解决：
宽较大，高较小的长logo贴到图片上可能会出现logo较小的情况
'''

# 获取背景图列表，back_img_path为背景图位置
back_img_path = '/mnt/storage/TRAIN_DATA/paste_logo_background/place365_6k'
back_names = os.listdir(back_img_path)

# 类别名称，用于标签文件生成
classes = [str(i).zfill(3) for i in range(1, 203)] + ['999']


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


def random_bk_img():
    '''随机获取背景图片并读取返回'''
    indx = random.randint(0, len(back_names) - 1)
    img_path = back_img_path + "/" + back_names[indx]
    img = cv2.imread(img_path)
    while img is None:
        indx = random.randint(0, len(back_names) - 1)
        img_path = back_img_path + "/" + back_names[indx]
        img = cv2.imread(img_path)
        h, w, _ = img.shape
        if h > 4 * w or w > 4 * h:
            img = None
    return img, back_names[indx]


def mergeImg_mask(bk_img, flag_img, boxes, label, idimg, flag_name):
    '''贴图代码'''
    bk_h, bk_w, _ = bk_img.shape
    flag_h, flag_w, _ = flag_img.shape

    img_name = flag_name[:-4] + '_' + str(idimg)

    paste_box = []
    # 按照标志绘图
    for i, (x, y) in enumerate(boxes):
        # TB大小增加0.9-1.1之间的动态变化
        if random.random() > 0.8 and flag_h > 20 and flag_w > 20:
            flag_h = round(flag_h * (0.2 * random.random() + 0.9))
            flag_w = round(flag_w * (0.2 * random.random() + 0.9))

            paste_img = cv2.resize(flag_img, (flag_w, flag_h))
        else:
            paste_img = flag_img
            flag_h, flag_w, _ = flag_img.shape

        if paste_img.shape[2] == 3:
            b_channel, _, _ = cv2.split(paste_img)
            mask = np.ones(b_channel.shape, dtype=b_channel.dtype)
            # print(label)
        else:
            mask = paste_img[:, :, 3] / 255

        # 判断要贴图的logo是否超出图片边界
        dw = [1, bk_w - x - flag_w][x + flag_w > bk_w]
        dh = [1, bk_h - y - flag_h][y + flag_h > bk_h]
        cor_w = [flag_w, bk_w - x][x + flag_w > bk_w]
        cor_h = [flag_h, bk_h - y][y + flag_h > bk_h]

        try:  # 主要处理台标超出图片边界的情况
            if dw == 1 and dh == 1:
                bk_img[y:y + flag_h, x:x + flag_w, :] = bk_img[y:y + flag_h, x:x + flag_w,
                                                        :] * (1 - mask)[:, :, None] + paste_img[:,
                                                                                      :, :3] * mask[
                                                                                               :, :,
                                                                                               None]
            elif dw < 0:  # 宽度超出边界
                bk_img[y:y + flag_h, x:x + flag_w, :] = bk_img[y:y + flag_h, x:x + flag_w, :] * \
                                                        (1 - mask)[:, :dw, None] + \
                                                        paste_img[:, :dw, :3] * mask[:, :dw, None]
            elif dh < 0:  # 高度超出边界
                bk_img[y:y + flag_h, x:x + flag_w, :] = bk_img[y:y + flag_h, x:x + flag_w, :] * \
                                                        (1 - mask)[:dh, :, None] + \
                                                        paste_img[:dh, :, :3] * mask[:dh, :, None]
            elif dw < 0 and dh < 0:  # 高度宽度均超出边界
                bk_img[y:y + flag_h, x:x + flag_w, :] = bk_img[y:y + flag_h, x:x + flag_w, :] * \
                                                        (1 - mask)[:dh, :dw, None] + \
                                                        paste_img[:dh, :dw, :3] * mask[:dh, :dw,
                                                                                  None]

            paste_box.append((x, y, cor_w, cor_h))
        except:
            print(f'{flag_name} error')
            return

    # 生成当前图片的标签文件
    cls_id = classes.index(label)  # cls 标签名，必须在classes数组中
    out_file = open('%s/labels/%s.txt' % (dic_path, img_name), 'w')  # 输出路径
    for (x, y, cor_w, cor_h) in paste_box:
        b = (float(x), float(x + cor_w), float(y), float(y + cor_h))  # xml中坐标信息
        bb = convert((bk_w, bk_h), b)  # 图片的w,h,dtype=int
        out_file.write(str(cls_id) + " " +
                       " ".join([str(a) for a in bb]) + '\n')
    out_file.close()
    # + '_'+ bk_name
    # 保存
    dst_dir = os.path.join(dic_path, 'images', label)
    os.makedirs(dst_dir, exist_ok=True)
    cv2.imwrite(os.path.join(dst_dir, img_name + ".jpg"), bk_img)


def create_img(img_path, idimg):
    # 随机获取背景图

    bk_img, bk_name = random_bk_img()
    bk_h, bk_w, _ = bk_img.shape

    # 获取当前贴图TB
    flag_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    flag_h, flag_w, _ = flag_img.shape
    # print(f'目录：{root.split("/")[-1]} 宽高比：{}')

    '''
    logo图与背景图的比例，需要自己根据需求调节，这里采用的逻辑比较简单
    logo宽大于高1.1，采用logo宽度对logo进行比例缩放
    此外，采用logo高度对logo进行比例缩放
    '''
    if flag_w / flag_h > 1.1:  # bk_w bk_h
        scale = 0.14 * random.random() + 0.1
        # scale=0.16 * random.random()+0.08
        scale_w = round(scale * bk_w)
        scale_size = (scale_w, round(scale_w * flag_h / flag_w))
    else:
        scale = 0.16 * random.random() + 0.08
        # scale = 0.14 * random.random()+0.1
        scale_h = round(scale * bk_h)
        scale_size = (round(scale_h * flag_w / flag_h), scale_h)

    flag_img = cv2.resize(flag_img, scale_size)
    flag_h, flag_w, _ = flag_img.shape

    flag_img_name = img_path.split('/')[-1]
    flag_label = flag_img_name.split('-')[0].rstrip('.png').rstrip('.jpg')

    try:
        # 构造贴图四个角位置
        attempt = 0
        success_flag = False
        while attempt < 5 and success_flag == False:
            try:
                boxes = []
                # 左上角
                x = random.randint(0, int(bk_w * 0.25 - flag_w))
                y = random.randint(0, int(bk_h * 0.25 - flag_h))
                boxes.append([x, y])
                # 左下角
                x = random.randint(0, int(bk_w * 0.25 - flag_w))
                y = random.randint(int(bk_h * 0.75), int(bk_h - flag_h))
                boxes.append([x, y])
                # 右上角
                x = random.randint(int(bk_w * 0.75), int(bk_w - flag_w))
                y = random.randint(0, int(bk_h * 0.25 - flag_h))
                boxes.append([x, y])
                # 右下角
                x = random.randint(int(bk_w * 0.75), int(bk_w - flag_w))
                y = random.randint(int(bk_h * 0.75), int(bk_h - flag_h))
                boxes.append([x, y])

                success_flag = True
            except:
                attempt += 1

        if success_flag:  # 贴图
            mergeImg_mask(bk_img, flag_img, boxes,
                          flag_label, idimg, flag_img_name)
    except:
        # print(idimg)
        print(img_path)


if __name__ == '__main__':
    '''贴图参数配置'''
    # 进程数控制
    threads = cpu_count() - 10
    # 生成的数据集和标签文件保存路径
    dic_path = "/home/zhangchao/data2/tb_dataset_0730"
    # 每个logo要制造的图片数量，logo总样本数位img_len*4 (4个角)
    imgs_len = 400
    # logo图路径
    flag_dic_path = "tb_db/20210730_new/tmp"

    os.makedirs(dic_path, exist_ok=True)
    os.makedirs(os.path.join(dic_path, 'labels'), exist_ok=True)

    im_list = []
    if flag_dic_path.endswith('.png') or flag_dic_path.endswith('.jpg'):
        item = [(flag_dic_path, i) for i in range(imgs_len)]
        im_list.extend(item)
    else:
        for root, dirs, files in os.walk(flag_dic_path, topdown=False):
            for flag_img_name in files:
                item = [(os.path.join(root, flag_img_name), i)
                        for i in range(4000, 4000 + imgs_len)]
                im_list.extend(item)

    # pfunc = partial(create_img, idimg)
    # 多进程贴图
    with Pool(processes=threads) as p:
        p.starmap(create_img, im_list)
