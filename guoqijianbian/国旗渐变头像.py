from PIL import Image
import os
import numpy as np
import shutil
"""
注意：
1、运行前请确保安装了python3环境
2、请先安装PIL库，命令是： pip install PIL
3、遇到任何问题可通过关注公众号【Python之禅】获得作者的帮助
"""

def convert(size, box):
    l =  []
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
    l = [x, y, w, h]
    l = np.array(l, dtype=np.float32)
    assert (l > 0).all(), 'negative labels'
    assert (l < 1).all(), 'non-normalized or out of bounds coordinate labels'
    return (x, y, w, h)

def main(header_img):
    avatar = Image.open(header_img)  # 加载头像
    flag = Image.open("a.png")  # 加载国旗
    sx2, sy2 = 501, 446
    width = min(flag.size)  # 取长宽比较小的那个
    flag = flag.crop((0, 0, width, width))  # 裁剪图片成正方形
    avatar_width, avatar_height = avatar.size  # 获取头像宽高
    # 计算resize后的右下角坐标
    h_r = avatar_height/width
    w_r = avatar_width/width
    x2 = sx2 * w_r
    y2 = sy2 * h_r
    flag = flag.resize(avatar.size)  # 将国旗缩放成头像大小比例

    weight = 2  # 透明度

    for w in range(avatar_width):
        for h in range(avatar_height):
            rgba = flag.getpixel((w, h))
            alpha = 255 - w // weight
            if alpha < 0:
                alpha = 0
            new_rgba = rgba[:-1] + (alpha,)
            flag.putpixel((w, h), new_rgba)
    try:
        avatar.paste(flag, (0, 0), mask=flag)
        # avatar.show()
        name = img_path.split("\\")[-1]
        avatar.save("./touxiang/"+name)  # 保存新头像
        out_file = open(r'./txt/%s.txt' % (name[0:-4]), 'w')
        w_a,h_a = avatar.size
        b = (float(1), float(x2),
             float(1),
             float(y2))
        bb = convert((w_a, h_a), b)
        out_file.write(str(52) + " " + " ".join([str(a) for a in bb]) + '\n')
    except Exception as e:
        print(e)
        # shutil.move(header_img,'./error/')
imgs = os.listdir(r'E:\huangxin\data\logo_det\guoqi_touxiang\touxiang')

if __name__ == '__main__':
    for i in imgs:
        img_path = os.path.join(r'E:\huangxin\data\logo_det\guoqi_touxiang\touxiang',i)
        main(img_path)
