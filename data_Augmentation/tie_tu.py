'''
PNG贴图
'''
import cv2
import os
import random
# img1 = cv2.imread('D:\\data\\mb\\bg\\img\\0_000001.jpg')
# img2 = cv2.imread('D:\\data\\mb\\res\\mb_pdf0000000_0.png', -1)
# img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]),interpolation=cv2.INTER_CUBIC)
# b, g, r, a = cv2.split(img2)
# sign1 = cv2.merge([b, g, r])
# alpha1 = cv2.merge([a, a, a])
# img2gray1 = cv2.cvtColor(alpha1, cv2.COLOR_BGR2GRAY)
# ret1, mask_not1 = cv2.threshold(img2gray1, 175, 255, cv2.THRESH_BINARY)
# mask1 = cv2.bitwise_not(mask_not1)
#
# img1_bg1 = cv2.bitwise_or(img1, img1, mask=mask1)
# img2_fg1 = cv2.bitwise_and(sign1, sign1, mask=mask_not1)
# dst1 = cv2.add(img1_bg1, img2_fg1)
# # img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)
# # print(img2.shape)
# # img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]),interpolation=cv2.INTER_CUBIC)
# # print(img1.shape)
# # img_mix = cv2.addWeighted(img1, 0, img2, 0, 3)
# Alpha1_sign = cv2.addWeighted(img2_fg1, 0.8, img1_bg1, 1, 0)
# # cv2.imshow('img1', img1)
# cv2.imshow('img2', dst1)
# cv2.imwrite('./newimg.jpg',dst1)
# cv2.imshow('img_mix', Alpha1_sign)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


bg_path = 'D:/data/cctv5+/bj/'
object_path = 'D:/data/cctv5+/resize_src/'
# 背景
bg_list = os.listdir(bg_path)
# 目标图片
objects = os.listdir(object_path)
# img2 = cv2.imread('D:\\data\\mb\\res\\0.png', -1)

for i, file in objects:
    # 读取目标图片
    obj_file_path = os.path.join(object_path, file)
    obj_file = cv2.imread(obj_file_path, -1)
    # 随机选取一张背景图
    bg_index = random.randint(0, len(bg_list)-1)
    bg_file = bg_list[bg_index]
    bg_file_path = os.path.join(bg_path, bg_file)
    bg_file_content = cv2.imread(bg_file_path)

    img1 = cv2.resize(bg_file_content, (obj_file.shape[1],obj_file.shape[0]),interpolation=cv2.INTER_CUBIC)
    b, g, r, a = cv2.split(obj_file)
    sign1 = cv2.merge([b, g, r])
    alpha1 = cv2.merge([a, a, a])
    img2gray1 = cv2.cvtColor(alpha1, cv2.COLOR_BGR2GRAY)
    ret1, mask_not1 = cv2.threshold(img2gray1, 175, 255, cv2.THRESH_BINARY)
    mask1 = cv2.bitwise_not(mask_not1)

    img1_bg1 = cv2.bitwise_or(img1, img1, mask=mask1)
    img2_fg1 = cv2.bitwise_and(sign1, sign1, mask=mask_not1)
    dst1 = cv2.add(img1_bg1, img2_fg1)
    # img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)
    # print(img2.shape)
    # img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]),interpolation=cv2.INTER_CUBIC)
    # print(img1.shape)
    # img_mix = cv2.addWeighted(img1, 0, img2, 0, 3)
    # Alpha1_sign = cv2.addWeighted(img2_fg1, 0.8, img1_bg1, 1, 0)
    # # cv2.imshow('img1', img1)
    # cv2.imshow('img2', dst1)
    cv2.imwrite('D:\\data\\mb\\mb_tietu_res\\05_{}.jpg'.format(str(i)), dst1)
    # cv2.imshow('img_mix', Alpha1_sign)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

