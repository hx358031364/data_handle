import os
import cv2
import random
import numpy as np
'''
png透明图贴图
'''
png_root = "D:/data/cctv5+/resize_src/"
bk_root = "D:/data/cctv5+/bg/"
save_root = "D:/data/cctv5+/tietu_jpg/"
save_txt = "D:/data/cctv5+/txt/"
data_cnt = 7000

png_names = os.listdir(png_root)
bk_names = os.listdir(bk_root)

# bk_img = cv2.imread("C://Users/Administrator/Desktop/bk.jpg")
# tb_img = cv2.imread("C://Users/Administrator/Desktop/resize_src/src.png",cv2.IMREAD_UNCHANGED)
# bk_h,bk_w,_ = bk_img.shape
# tb_h,tb_w,_ = tb_img.shape
#
# ratio = tb_img[:,:,3]/255

for i in range(data_cnt):

    png_name = png_names[random.randint(0,len(png_names)-1)]
    bk_name = bk_names[random.randint(0, len(bk_names) - 1)]
    png_img = cv2.imread(png_root + png_name, cv2.IMREAD_UNCHANGED)
    bk_img = cv2.imread(bk_root + bk_name)

    bk_h, bk_w, _ = bk_img.shape
    tb_h, tb_w, _ = png_img.shape

    ratio = png_img[:, :, 3] / 255

    bk_img2 = np.copy(bk_img)
    x = 37
    y = 27
    part_img = bk_img2[y:y+tb_h,x:x+tb_w,:]
    part_img[:,:,0] = (1-ratio) * part_img[:,:,0] + ratio*png_img[:,:,0]
    part_img[:,:,1] = (1-ratio) * part_img[:,:,1] + ratio*png_img[:,:,1]
    part_img[:,:,2] = (1-ratio) * part_img[:,:,2] + ratio*png_img[:,:,2]

    cv2.imwrite(save_root+'05_'+str(i)+".jpg",bk_img2)
    out_file = open(save_txt + '/%s.txt' % ('05_'+ str(i)), 'w')
    out_file.write('5' + '\n' + str(x) + '\n' + str(y) + '\n' + str(x+tb_w) + '\n' + str(y+tb_h) + '\n')
    out_file.close()

    # cv2.imshow("bk_img2",bk_img2)
    # cv2.waitKey(0)
