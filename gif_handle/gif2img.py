from PIL import Image
import os

"""
  将一张GIF动图分解到指定文件夹
  src_path：要分解的gif的路径
  dest_path：保存后的gif路径
"""


def gifSplit(src_path, dest_path, suffix="png"):
    img = Image.open(src_path)
    for i in range(img.n_frames):
        img.seek(i)
        new = Image.new("RGBA", img.size)
        new.paste(img)
        new.save(os.path.join(dest_path, "%d.%s" % (i, suffix)))


gifSplit('aboluo.gif', r'./pics')

# img = Image.open('taga.gif')
# try:
#     while True:
#         current = img.tell()
#
#         im = img.convert('RGB')
#         im.save('./pics/'+str(current)+'.jpg')
#         img.seek(current+1)
# except:
#     pass

# import cv2
#
# cap = cv2.VideoCapture('aboluo.gif')
#
# success = True
# count = 0
# while success:
#     success, image = cap.read()
#     if success:
#         cv2.imwrite('./pics/'+str(count)+'.png', image)
#         count = count + 1