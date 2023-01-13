import time

import cv2

# 通过cv2中的类获取视频流操作对象cap
cap = cv2.VideoCapture('http://alimov2.a.kwimgs.com/upic/2020/07/20/06/BMjAyMDA3MjAwNjAxMDBfMjU5ODU0NzI0XzMyNzA2NTEyMzM3XzJfMw==_b_Bdfc4d3bc0ff4e06a3966bdad3c9657cc.mp4')
# 调用cv2方法获取cap的视频帧（帧：每秒多少张图片）
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 获取cap视频流的每帧大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

# 定义编码格式mpge-4
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
# 定义视频文件输入对象
outVideo = cv2.VideoWriter('saveDir.avi', fourcc, fps, size)

# 获取视频流打开状态
if cap.isOpened():
    rval, frame = cap.read()
    print('ture')
else:
    rval = False
    print('False')

tot = 1
c = 1
# 循环使用cv2的read()方法读取视频帧
while rval:
    # rval 标志位, frame 每一帧图像
    print(rval)
    rval, frame = cap.read()
    # cv2.imshow('test',frame)
    # 每间隔20帧保存一张图像帧
    # if tot % 250 ==0 :
    cv2.imwrite('./output_jpg/'+'cut_'+str(c)+'.jpg',frame)
    c+=1
    tot += 1
    print('tot=', tot)
    # 使用VideoWriter类中的write(frame)方法，将图像帧写入视频文件
    outVideo.write(frame)
    cv2.waitKey(1)
    time.sleep(1)
cap.release()
outVideo.release()
cv2.destroyAllWindows()