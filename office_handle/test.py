import cv2


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


if __name__ == '__main__':
    img = cv2.imread('./test_file/test1.png', -1)
    img_copy = img.copy()
    # 注意：这里先copy()再传入函数，直接传入img会将原img直接修改掉
    whiteback = alpha2white_opencv2(img_copy)
    # cv2.imshow("after", whiteback)
    cv2.imwrite("test1_after.jpg",whiteback)
    # cv2.waitKey(0)
# haveAlpha.png改成你自己的透明背景图片路径