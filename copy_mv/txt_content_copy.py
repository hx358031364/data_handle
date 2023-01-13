import shutil
with open("/data2/tb_dataset/train.txt") as f:
# f = open("/home/huangxin/work/voc2007/val.txt")
    line_list = f.readlines()
    for line in line_list:
        name = line.split("/")[-1].replace("\n", "")
        print(name)
        shutil.copy("/data2/JPEGImages/{}".format(name),
                    "/data5/cnc_data_TB_yolov5/images/train/{}".format(name))
        shutil.copy("/data2/labels/{}".format(name.replace('jpg', 'txt')),
                    "/data5/cnc_data_TB_yolov5/labels/train/{}".format(
                        name.replace('jpg', 'txt')))
