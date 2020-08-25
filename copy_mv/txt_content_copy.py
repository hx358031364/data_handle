import shutil
with open("/home/huangxin/work/voc2007/val.txt") as f:
# f = open("/home/huangxin/work/voc2007/val.txt")
    line_list = f.readlines()
    for line in line_list:
        name = line.split("/")[-1].replace("\n", "")
        print(name)
        shutil.copy("/home/huangxin/work/voc2007/JPEGImages/{}".format(name), "./val_jpg/{}".format(name))


