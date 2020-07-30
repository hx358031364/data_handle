import cv2
import numpy as np
import random
import os
import threading
import logging
import time

logger = logging.getLogger(__name__)


class DataAugmentation:

    def __init__(self):
        pass

    @staticmethod
    def openImage(image):
        return cv2.imread(image)

    # 图像旋转
    @staticmethod
    def rotate(img, angle=45):  # 对图片执行旋转操作
        imgInfo = img.shape
        height = imgInfo[0]
        width = imgInfo[1]
        matRotate = cv2.getRotationMatrix2D((width * 0.5, height * 0.5), angle, 1)
        dst = cv2.warpAffine(img, matRotate, (width, height))
        return dst

    # 图像缩放
    @staticmethod
    def resize_pic(img, scale=0.5):  # 对图片执行resize操作
        shape_img = img.shape
        dstHeight = int(shape_img[0] * scale)
        dstWeight = int(shape_img[1] * scale)

        dst = cv2.resize(img, (dstWeight, dstHeight))
        return dst

    # 图像裁剪剪切
    @staticmethod
    def cut(img, val=0.1):  # 对图片执行剪切操作
        shape_img = img.shape
        dst = img[int(shape_img[0] * val):shape_img[0] - int(shape_img[0] * val),
              int(shape_img[1] * val * 2):int(shape_img[1] - shape_img[1] * val * 2)]
        return dst

    # 图像平移
    @staticmethod
    def shift(img, val=100):  # 对图片执行平移操作
        imgInfo = img.shape
        height = imgInfo[0]
        width = imgInfo[1]
        dst = np.zeros(imgInfo, np.uint8)
        for i in range(height):
            for j in range(width - val):
                dst[i, j + val] = img[i, j]

        return dst

    @staticmethod
    def gasuss_noise(image, mean=0, var=0.002):  # 对图片添加高斯噪声
        '''
            添加高斯噪声
            mean : 均值
            var : 方差
        '''
        image = np.array(image / 255, dtype=float)
        noise = np.random.normal(mean, var ** 0.5, image.shape)
        out = image + noise
        if out.min() < 0:
            low_clip = -1.
        else:
            low_clip = 0.
        out = np.clip(out, low_clip, 1.0)
        out = np.uint8(out * 255)
        # cv.imshow("gasuss", out)
        return out

    @staticmethod
    def sp_noise(image, prob=0.01):  # 对图片添加椒盐噪声
        '''
        添加椒盐噪声
        prob:噪声比例
        '''
        output = np.zeros(image.shape, np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
        return output

    # 图像翻转
    @staticmethod
    def img_flip(image):
        # 0以X轴为对称轴翻转,>0以Y轴为对称轴翻转, <0X轴Y轴翻转
        horizontally = cv2.flip(image, 0)  # 水平镜像
        vertically = cv2.flip(image, 1)  # 垂直镜像
        hv = cv2.flip(image, -1)  # 水平垂直镜像
        return horizontally, vertically, hv

    # 图像亮度调节
    @staticmethod
    def img_brightness(image):

        contrast = 1  # 对比度
        brightness = 100  # 亮度
        # brightness = np.random.randint(20, 80)
        pic_turn = cv2.addWeighted(image, contrast, image, 0, brightness)  # cv2.addWeighted(对象,对比度,对象,亮度)
        return pic_turn

    @staticmethod
    def saveImage(image, path):
        cv2.imwrite(path, image)


def makeDir(path):
    try:
        if not os.path.exists(path):
            if not os.path.isfile(path):
                # os.mkdir(path)
                os.makedirs(path)
            return 0
        else:
            return 1
    except Exception as e:
        print(str(e))
        return -2


def imageOps(func_name, image, des_path, file_name, times=1):
    funcMap = {
        "rotate": DataAugmentation.rotate,  # 旋转
        "resize_pic": DataAugmentation.resize_pic,  # 缩放
        "cut": DataAugmentation.cut,  # 裁剪
        "shift": DataAugmentation.shift,  # 平移
        "gasuss_noise": DataAugmentation.gasuss_noise,  # 高斯噪声
        "sp_noise": DataAugmentation.sp_noise,  # 椒盐噪声
        "img_flip": DataAugmentation.img_flip,  # 图像翻转
        "img_brightness": DataAugmentation.img_brightness  # 亮度
    }
    if funcMap.get(func_name) is None:
        logger.error("%s is not exist", func_name)
        return -1

    for _i in range(0, times, 1):
        new_image = funcMap[func_name](image)
        DataAugmentation.saveImage(new_image, os.path.join(des_path, func_name + str(_i) + file_name))


opsList = {"rotate", "resize_pic", "cut", "shift", "gasuss_noise", "sp_noise", "img_brightness"}


def threadOPS(path, new_path):
    """
    多线程处理事务
    :param src_path: 资源文件
    :param des_path: 目的地文件
    :return:
    """
    if os.path.isdir(path):
        img_names = os.listdir(path)
    else:
        img_names = [path]
    for img_name in img_names:
        print(img_name)
        tmp_img_name = os.path.join(path, img_name)
        if os.path.isdir(tmp_img_name):
            if makeDir(os.path.join(new_path, img_name)) != -1:
                threadOPS(tmp_img_name, os.path.join(new_path, img_name))
            else:
                print('create new dir failure')
                return -1
                # os.removedirs(tmp_img_name)
        elif tmp_img_name.split('.')[1] != "DS_Store":
            # 读取文件并进行操作
            image = DataAugmentation.openImage(tmp_img_name)
            threadImage = [0] * 7
            _index = 0
            for ops_name in opsList:
                threadImage[_index] = threading.Thread(target=imageOps,
                                                       args=(ops_name, image, new_path, img_name,))
                threadImage[_index].start()
                _index += 1
                time.sleep(0.2)


if __name__ == '__main__':
    threadOPS("./test/",
              "./result/")
