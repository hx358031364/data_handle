import os
import shutil
import tqdm

# 将所有图片移动到一个文件内
i = 0
dire = 'D:\\data\\sk_png\\BK_sign'
for curdir, subdirs, files in os.walk(dire):
     for file in tqdm.tqdm(files):
         path=os.path.join(curdir, file)
         shutil.copyfile(path, 'D:\\data\\tv_source_data\\jpg/{}'.format(file))
