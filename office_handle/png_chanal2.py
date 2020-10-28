'''
png透明图转白色背景
'''
import cv2
import os

def alpha2white_opencv2(img):
    sp = img.shape
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]
            if (color_d[3] == 0):
                img[xw, yh] = [255, 255, 255, 255]
    return img


listdir = os.listdir('D:\\data\\hongtou')

if __name__ == '__main__':
    for files in listdir:
        if files.endswith('.png'):
            png_file = os.path.join('D:\\data\\hongtou', files)
            img = cv2.imread(png_file, -1)
            img_copy = img.copy()
            # 注意：这里先copy()再传入函数，直接传入img会将原img直接修改掉
            whiteback = alpha2white_opencv2(img_copy)
            # cv2.imshow("after", whiteback)
            cv2.imwrite("{}.jpg".format(png_file[0:-4]),whiteback)
            # cv2.waitKey(0)