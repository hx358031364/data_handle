import PIL.Image as Image
'''
指定图片内像素值区域背景为透明
'''

# 以第一个像素为准，相同色改为透明
def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = (255, 255, 0, 255)  # 要替换的颜色
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


if __name__ == '__main__':
    img = Image.open('D:\\data\\mb\\res\\resize512_0_11.png')
    img = transparent_back(img)
    img.save('img2.png')