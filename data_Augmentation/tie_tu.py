
import cv2
import numpy as np
from PIL import Image

img1 = cv2.imread('D:\\data\\mb\\bg\\img\\0_000001.jpg')
img2 = cv2.imread('D:\\data\\mb\\res\\0.png', -1)
img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]),interpolation=cv2.INTER_CUBIC)
b, g, r, a = cv2.split(img2)
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
Alpha1_sign = cv2.addWeighted(img2_fg1, 0.8, img1_bg1, 1, 0)
# cv2.imshow('img1', img1)
cv2.imshow('img2', dst1)
cv2.imwrite('./newimg.jpg',dst1)
cv2.imshow('img_mix', Alpha1_sign)

cv2.waitKey(0)
cv2.destroyAllWindows()

