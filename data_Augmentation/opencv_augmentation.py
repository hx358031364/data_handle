import cv2
import numpy as np
import random
import os

# 图像旋转
def rotate(img, angle): # 对图片执行旋转操作
    imgInfo = img.shape
    height= imgInfo[0]
    width = imgInfo[1]
    matRotate = cv2.getRotationMatrix2D((width*0.5,height*0.5), angle, 1)
    dst = cv2.warpAffine(img, matRotate, (width,height))
    return dst

# 图像缩放
def resize_pic(img, scale): # 对图片执行resize操作
    shape_img = img.shape
    dstHeight = int(shape_img[0] * scale)
    dstWeight = int(shape_img[1] * scale)

    dst = cv2.resize(img, (dstWeight, dstHeight))
    return dst

# 图像裁剪剪切
def cut(img, val): # 对图片执行剪切操作
    shape_img = img.shape
    dst = img[int(shape_img[0]*val):shape_img[0] - int(shape_img[0]*val), int(shape_img[1]*val*2):int(shape_img[1] - shape_img[1]*val*2)]
    return dst

#图像平移
def shift(img, val):  # 对图片执行平移操作
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.zeros(imgInfo, np.uint8)
    for i in range(height):
        for j in range(width - val):
            dst[i, j + val] = img[i, j]

    return dst

def gasuss_noise(image, mean=0, var=0.002): #  对图片添加高斯噪声
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    #cv.imshow("gasuss", out)
    return out

def sp_noise(image,prob):  #对图片添加椒盐噪声
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape,np.uint8)
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
def img_flip(image):
    # 0以X轴为对称轴翻转,>0以Y轴为对称轴翻转, <0X轴Y轴翻转
    horizontally = cv2.flip(image, 0)  # 水平镜像
    vertically = cv2.flip(image, 1)  # 垂直镜像
    hv = cv2.flip(image, -1)  # 水平垂直镜像
    return horizontally, vertically, hv

# 图像亮度调节
def img_brightness(image):

    contrast = 1  # 对比度
    # contrast = np.random.randint(1, 3)  # 对比度
    # brightness = 100  # 亮度
    brightness = np.random.randint(20, 80)
    pic_turn = cv2.addWeighted(image, contrast, image, 0, brightness)   # cv2.addWeighted(对象,对比度,对象,亮度)
    return pic_turn

def warp_affine(img):
    rows, cols = img.shape[:2]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    # 第三个参数：变换后的图像大小
    res = cv2.warpAffine(img, M, (rows, cols), borderValue=(0, 255, 255))
    # res = cv2.warpAffine(img, M, (rows, cols))
    return res
    # cv2.imwrite(os.path.join(bright_path, img_name),res)

def batch_augment(img_path, save_path):
    img_names = os.listdir(img_path)
    for img_name in img_names:
        name = img_name[0:-4]
        png_name = 'rotate_'+name+'.jpg'
        tmp_img_name = os.path.join(img_path, img_name)
        img = cv2.imread(tmp_img_name)
        ang = [90, 180, 270]
        res = rotate(img, random.choice(ang))
        cv2.imwrite(os.path.join(save_path, png_name), res)
        # sp_noise_img = sp_noise(img, 0.01)
        # cv2.imwrite(os.path.join(save_path, img_name), sp_noise_img)
        # brightness = img_brightness(img)
        # bright_path = "./liangdu"
        # cv2.imwrite(os.path.join(bright_path, img_name), brightness)

def blur_demo(image):
    """
    均值模糊：去随机噪声
    blur只能定义卷积核大小
    """
    dst_y = cv2.blur(image, (1, 10))  # Y方向模糊，1X10卷积核
    dst_x = cv2.blur(image, (10, 1))  # X方向模糊，10X1卷积核
    dst_xy = cv2.blur(image, (5, 5))  # 块模糊，5X5卷积核
    cv2.imshow("blurY demo", dst_y)
    cv2.imshow("blurX demo", dst_x)
    cv2.imshow("blurXY demo", dst_xy)
    cv2.imwrite('D:/data/cctv5+/dst_y.png', dst_y)
    cv2.imwrite('D:/data/cctv5+/dst_x.png', dst_x)
    cv2.imwrite('D:/data/cctv5+/dst_xy.png', dst_xy)







if __name__ == "__main__":
    img_path = r"C:\Users\rmzk\Downloads\data"
    save_path = r"C:\Users\rmzk\Downloads\data"
    batch_augment(img_path, save_path)

# src = cv2.imread('D:/data/cctv5+/src.png',-1)

# blur_demo(src)
# median_blur_demo(src)
# blur_demo(src)
#
# cv2.imshow("src demo", src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



    # img = cv2.imread('/home/yasin/cat.jpg')
    #
    # new_rotated45 = rotate(img, 45)
    # resize_img = resize_pic(img, 0.5)
    # cut_img = cut(img, 0.1)
    # shift_img = shift(img, 100)
    # gasuss_noised_img = gasuss_noise(img)
    # sp_noise_img = sp_noise(img,0.01)
    #
    # cv2.imshow('new_rotated45', new_rotated45)
    # cv2.waitKey()
    #
    # cv2.imshow('resize_img',resize_img)
    # cv2.waitKey()
    #
    # cv2.imshow('cut_img', cut_img)
    # cv2.waitKey()
    #
    # cv2.imshow('shift_img', shift_img)
    # cv2.waitKey()
    #
    # cv2.imshow('gasuss_noised_img', gasuss_noised_img)
    # cv2.waitKey()
    #
    # cv2.imshow('sp_noise_img', sp_noise_img)
    # cv2.waitKey()
