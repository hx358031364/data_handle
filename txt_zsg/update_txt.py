import os
import re

path = '/data4/huangxin/chenwenjing_tietu/txt/'
files = os.listdir(path)
# files = []
# for file in os.listdir(path):
#     if file.endswith(".txt"):
#         files.append(path+file)
for file in files:
    with open(path+file, 'r') as f:
        new_data = re.sub('^0', '162', f.read(), flags=re.MULTILINE)    # 将列中的0替换为1
        print("转化成功")
    with open(file, 'w') as f:
        f.write(new_data)