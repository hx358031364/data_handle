'''
仿射变换
'''

import  random
import numpy as np
import cv2
import math

def random_affine(img, degrees=10, translate=.1, scale=.1, shear=10, border=0):
    # torchvision.transforms.RandomAffine(degrees=(-10, 10), translate=(.1, .1), scale=(.9, 1.1), shear=(-10, 10))
    # https://medium.com/uruvideo/dataset-augmentation-with-random-homographies-a8f4b44830d4
    # targets = [cls, xyxy]

    imgInfo = img.shape
    height_on_half = imgInfo[0]//2
    width_on_half = imgInfo[1]//2
    # mode = imgInfo[2]
    #
    # dst = np.zeros(imgInfo, np.uint8)
    #
    # for i in range(height_on_half):
    #     for j in range(width_on_half):
    #         dst[i+height_on_half, j + width_on_half] = img[i, j]
    # img = dst


    height = img.shape[0] + border * 2
    width = img.shape[1] + border * 2

    mat_translation = np.float32([[1, 0, width_on_half], [0, 1, height_on_half]])
    dst = cv2.warpAffine(img, mat_translation, (width, height), borderValue=(250, 255, 255))
    img = dst
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    # Rotation and Scale
    R = np.eye(3)
    a = random.uniform(-degrees, degrees)
    # a += random.choice([-180, -90, 0, 90])  # add 90deg rotations to small rotations
    s = random.uniform(1 - scale, 1 + scale)
    # s = 2 ** random.uniform(-scale, scale)
    # R[:2] = cv2.getRotationMatrix2D(angle=a, center=(img.shape[1] / 2, img.shape[0] / 2), scale=s)
    R[:2] = cv2.getRotationMatrix2D(angle=a, center=(img.shape[1] * 0.04 + width_on_half, img.shape[0] * 0.16 + height_on_half), scale=s)

    # Translation
    T = np.eye(3)
    T[0, 2] = random.uniform(-translate, translate) * img.shape[0] + border  # x translation (pixels)
    T[1, 2] = random.uniform(-translate, translate) * img.shape[1] + border  # y translation (pixels)

    # Shear
    S = np.eye(3)
    S[0, 1] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # y shear (deg)

    # Combined rotation matrix
    M = S @ T @ R  # ORDER IS IMPORTANT HERE!!
    if (border != 0) or (M != np.eye(3)).any():  # image changed
        img = cv2.warpAffine(img, M[:2], dsize=(width, height), flags=cv2.INTER_LINEAR, borderValue=(250, 255, 255))

    return img

if __name__ == '__main__':
    img = cv2.imread('D:\\data\\mb\\te\\resize512_0_11.jpg')
    # cv2.imwrite('D:\\data\\mb\\te\\0_000001.png', img)
    for i in range(0,5):
        img_file = random_affine(img)
        cv2.imwrite('D:\\data\\mb\\te\\yelo\\{}.png'.format(str(i)),img_file)
