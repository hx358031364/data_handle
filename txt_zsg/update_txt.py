import os
import re

path = './txt/'
files = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path+file)
for file in files:
    with open(file, 'r') as f:
        new_data = re.sub('^124', '63', f.read(), flags=re.MULTILINE)    # 将列中的0替换为1
        print("转化成功")
    with open(file, 'w') as f:
        f.write(new_data)