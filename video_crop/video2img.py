# -*- coding: utf-8 -*-
import os
import cv2  ##加载OpenCV模块
from multiprocessing import Pool
from tqdm.std import tqdm
def video2frames(pathIn='',
                 pathOut='',
                 only_output_video_info=False,
                 extract_time_points=None,
                 initial_extract_time=0,
                 end_extract_time=None,
                 extract_time_interval=-1,
                 output_prefix='frame',
                 jpg_quality=100,
                 isColor=True):
    '''
    pathIn：视频的路径，比如：F:\python_tutorials\test.mp4
    pathOut：设定提取的图片保存在哪个文件夹下，比如：F:\python_tutorials\frames1\。如果该文件夹不存在，函数将自动创建它
    only_output_video_info：如果为True，只输出视频信息（长度、帧数和帧率），不提取图片
    extract_time_points：提取的时间点，单位为秒，为元组数据，比如，(2, 3, 5)表示只提取视频第2秒， 第3秒，第5秒图片
    initial_extract_time：提取的起始时刻，单位为秒，默认为0（即从视频最开始提取）
    end_extract_time：提取的终止时刻，单位为秒，默认为None（即视频终点）
    extract_time_interval：提取的时间间隔，单位为秒，默认为-1（即输出时间范围内的所有帧）
    output_prefix：图片的前缀名，默认为frame，图片的名称将为frame_000001.jpg、frame_000002.jpg、frame_000003.jpg......
    jpg_quality：设置图片质量，范围为0到100，默认为100（质量最佳）
    isColor：如果为False，输出的将是黑白图片
    '''

    cap = cv2.VideoCapture(pathIn)  ##打开视频文件
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  ##视频的帧数
    fps = cap.get(cv2.CAP_PROP_FPS)  ##视频的帧率
    dur = n_frames / fps  ##视频的时间

    ##如果only_output_video_info=True, 只输出视频信息，不提取图片
    if only_output_video_info:
        print('only output the video information (without extract frames)::::::')
        print("Duration of the video: {} seconds".format(dur))
        print("Number of frames: {}".format(n_frames))
        print("Frames per second (FPS): {}".format(fps))

        ##提取特定时间点图片
    elif extract_time_points is not None:
        if max(extract_time_points) > dur:  ##判断时间点是否符合要求
            raise NameError('the max time point is larger than the video duration....')
        try:
            os.mkdir(pathOut)
        except OSError:
            pass
        success = True
        count = 0
        while success and count < len(extract_time_points):
            cap.set(cv2.CAP_PROP_POS_MSEC, (1000 * extract_time_points[count]))
            success, image = cap.read()
            if success:
                if not isColor:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  ##转化为黑白图片
                print('Write a new frame: {}, {}th'.format(success, count + 1))
                cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count + 1)), image,
                            [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])  # save frame as JPEG file
                count = count + 1

    else:
        ##判断起始时间、终止时间参数是否符合要求
        if initial_extract_time > dur:
            raise NameError('initial extract time is larger than the video duration....')
        if end_extract_time is not None:
            if end_extract_time > dur:
                raise NameError('end extract time is larger than the video duration....')
            if initial_extract_time > end_extract_time:
                raise NameError('end extract time is less than the initial extract time....')

        ##时间范围内的每帧图片都输出
        if extract_time_interval == -1:
            if initial_extract_time > 0:
                cap.set(cv2.CAP_PROP_POS_MSEC, (1000 * initial_extract_time))
            try:
                os.mkdir(pathOut)
            except OSError:
                pass
            print('Converting a video into frames......')
            if end_extract_time is not None:
                N = (end_extract_time - initial_extract_time) * fps + 1
                success = True
                count = 0
                while success and count < N:
                    success, image = cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        print('Write a new frame: {}, {}/{}'.format(success, count + 1, n_frames))
                        cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count + 1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])  # save frame as JPEG file
                        count = count + 1
            else:
                success = True
                count = 0
                while success:
                    success, image = cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        print('Write a new frame: {}, {}/{}'.format(success, count + 1, n_frames))
                        cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count + 1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])  # save frame as JPEG file
                        count = count + 1

        ##判断提取时间间隔设置是否符合要求
        elif extract_time_interval > 0 and extract_time_interval < 1 / fps:
            raise NameError('extract_time_interval is less than the frame time interval....')
        elif extract_time_interval > (n_frames / fps):
            raise NameError('extract_time_interval is larger than the duration of the video....')

        ##时间范围内每隔一段时间输出一张图片
        else:
            try:
                os.mkdir(pathOut)
            except OSError:
                pass
            # print('Converting a video into frames......')
            if end_extract_time is not None:
                N = (end_extract_time - initial_extract_time) / extract_time_interval + 1
                success = True
                count = 0
                while success and count < N:
                    cap.set(cv2.CAP_PROP_POS_MSEC, (1000 * initial_extract_time + count * 1000 * extract_time_interval))
                    success, image = cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        print('Write a new frame: {}, {}th'.format(success, count + 1))
                        cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count + 1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])  # save frame as JPEG file
                        count = count + 1
            else:
                success = True
                count = 0
                while success and count <= dur:
                    cap.set(cv2.CAP_PROP_POS_MSEC, (1000 * initial_extract_time + count * 1000 * extract_time_interval))
                    success, image = cap.read()
                    if success:
                        if not isColor:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        # print('Write a new frame: {}, {}th'.format(success, count + 1))
                        cv2.imwrite(os.path.join(pathOut, "{}_{:06d}.jpg".format(output_prefix, count + 1)), image,
                                    [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])  # save frame as JPEG file
                        count = count + 1


##### 测试
# pathIn = 'http://alimov2.a.kwimgs.com/upic/2020/07/20/06/BMjAyMDA3MjAwNjAxMDBfMjU5ODU0NzI0XzMyNzA2NTEyMzM3XzJfMw==_b_Bdfc4d3bc0ff4e06a3966bdad3c9657cc.mp4'
# pathIn = r'C:\Users\rmzk\Desktop\video\8197621776384493827.mp4'
# # listdir = os.listdir(data_path)
# sava_path = r'C:\Users\rmzk\Desktop\video_crop'
#
# video2frames(pathIn, sava_path, extract_time_interval=1)

# pathOut = r'C:\Users\rmzk\Desktop\video_crop'
# video2frames(r'D:\code\data_handle\gif_handle\taga.gif', pathOut)
#
# pathOut = './frames2'
# video2frames(pathIn, pathOut, extract_time_points=(1, 2, 5))
#
# pathOut = './frames3'
# video2frames(pathIn, pathOut,
#              initial_extract_time=1,
#              end_extract_time=3,
#              extract_time_interval=0.5)
#
# pathOut = './frames4/'
# video2frames(pathIn, pathOut, extract_time_points=(0.3, 2), isColor=False)
#
# pathOut = './frames5/'
# video2frames(pathIn, pathOut, extract_time_points=(0.3, 2), jpg_quality=50)


# data_path = r'D:\data\SZK_data\zhuaqu_douyin'
# listdir = os.listdir(data_path)
# threads = 1
#
# def down_img(path_in):
#     try:
#         json_file = open(os.path.join(r'D:\data\SZK_data\zhuaqu_douyin', path_in))
#         sava_path = os.path.join(r'E:\huangxin\SZK\JC', path_in[:-4])
#         for i,(line) in tqdm(enumerate(json_file)):
#             url = line.strip('\n')
#             output_prefix = path_in[:-4]+'_'+str(i)
#             video2frames(url, sava_path, output_prefix=output_prefix, extract_time_interval=2)
#     except Exception as e:
#         print(e)
#         print(path_in, line)
#
#
# if __name__ == "__main__":
#     with Pool(processes=threads) as p:
#         p.map(down_img, listdir)

data_path = r'/mnt/storage/TRAIN_DATA/zhangchao/test_copy/video/加边框/有边框'
listdir = os.listdir(data_path)
sava_path = r'/workspace/testcode/yolov5-6.1/video_crop_test/'
for vi in listdir:
    name = vi[:-4]
    path_in = os.path.join(r'/mnt/storage/TRAIN_DATA/zhangchao/test_copy/video/加边框/有边框', vi)
    video2frames(path_in, sava_path, output_prefix=name, extract_time_interval=2)
