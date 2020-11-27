import os
import random
import cv2
import numpy as np



gz_root = "D:\\data\\yolo_data_gan\\gz\\"
bk_root = "D:\\data\\yolo_data_gan\\HPSCANS\\"
save_root = "D:\\data\\yolo_data_gan\\img\\"
save_txt = "D:\\data\\yolo_data_gan\\txt\\"
data_cnt = 7000


# f = open(save_txt,mode="a",encoding="utf-8")

gz_names = os.listdir(gz_root)
bk_names = os.listdir(bk_root)

for i in range(data_cnt):
    gz_name = gz_names[random.randint(0,len(gz_names)-1)]
    bk_name = bk_names[random.randint(0,len(bk_names)-1)]
    gz_img = cv2.imread(gz_root + gz_name)
    bk_img = cv2.imread(bk_root + bk_name)

    gz_h,gz_w,_ = gz_img.shape
    bk_h,bk_w,_ = bk_img.shape

    x = random.randint(0,bk_w-gz_w)
    y = random.randint(0,bk_h-gz_h)

    part_img = bk_img[y:y+gz_h,x:x+gz_w,:]
    # ------------------------------------------------------
    hsv = cv2.cvtColor(gz_img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    red_mask = mask0 + mask1
    # --------------------------------------
    part_gray = cv2.cvtColor(part_img,cv2.COLOR_BGR2GRAY)

    _,part_th = cv2.threshold(part_gray,125,255,cv2.THRESH_BINARY)
    # cv2.imshow("part_th",part_th)
    mask = (red_mask>0) & (part_th==255)
    part_img[mask] = gz_img[mask]
    # ----------------------------------------------------

    point1 = np.array([[0.2*bk_w, 0.2*bk_h],
                       [0.8*bk_w, 0.2*bk_h],
                       [0.8*bk_w, 0.8*bk_h],
                       [0.2*bk_w, 0.8*bk_h]
                       ], dtype="float32")

    dx0 = random.randint(-int(0.03 * bk_w), int(0.03 * bk_w))
    dy0 = random.randint(-int(0.03 * bk_h), int(0.03 * bk_h))

    dx1 = random.randint(-int(0.03 * bk_w), int(0.03 * bk_w))
    dy1 = random.randint(-int(0.03 * bk_h), int(0.03 * bk_h))

    dx2 = random.randint(-int(0.03 * bk_w), int(0.03 * bk_w))
    dy2 = random.randint(-int(0.03 * bk_h), int(0.03 * bk_h))

    dx3 = random.randint(-int(0.1 * bk_w), int(0.1 * bk_w))
    dy3 = random.randint(-int(0.1 * bk_h), int(0.1 * bk_h))

    point2 = np.array([[0.2*bk_w+dx0, 0.2*bk_h+dy0],
                       [0.8*bk_w+dx1, 0.2*bk_h+dy1],
                       [0.8*bk_w+dx2, 0.8*bk_h+dy2],
                       [0.2*bk_w+dx3, 0.8*bk_h+dy3]
                       ], dtype="float32")

    M = cv2.getPerspectiveTransform(point1,point2)
    # out_img = cv2.warpPerspective(bk_img, M, (bk_w, bk_h),borderValue=0)

    # out_img = cv2.resize(out_img,dsize=None,fx=0.3,fy=0.3)
    # cv2.imshow("out_img",out_img)
    # cv2.waitKey(0)
    cv2.imwrite(save_root+'gz_'+str(i)+".jpg",bk_img)
    out_file = open(save_txt + '/%s.txt' % ('gz_'+ str(i)), 'w')
    out_file.write('gz' + '\n' + str(x) + '\n' + str(y) + '\n' + str(x+gz_w) + '\n' + str(y+gz_h) + '\n')
    out_file.close()
    # line = str(i) + ".jpg "+str((y,y+gz_h,x,x+gz_w))
    # f.write(line+"\n")
    # f.flush()








