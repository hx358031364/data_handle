import PIL.Image as Image
import os
'''
指定图片内像素值区域背景为透明
'''

# 以第一个像素为准，相同色改为透明
def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = (255, 255, 250, 255)  # 要替换的颜色
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


if __name__ == '__main__':
    listdir = os.listdir('D:\\data\\mb\\te\\yelo\\')
    for files in listdir:
        if files.endswith('.png'):
            png_file = os.path.join('D:\\data\\mb\\te\\yelo\\', files)
            img = Image.open(png_file)
            img = transparent_back(img)
            name = files[0:-4]
            img.save('D:\\data\\mb\\res\\{}.png'.format(name))