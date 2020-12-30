import os
import shutil
import tqdm
'''
拷贝符合开头字符的文件
'''
# for i in range(0,53):
#     a = str(i).zfill(2)
#     os.makedirs(a)
start = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
         '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
         '44', '45', '46', '47', '48', '49', '50', '51', 'gz', 'mb']
file_patch = '/home/huangxin/work/data_new/Annotations/'
file_list = os.listdir(file_patch)
for file in tqdm(file_list):
    for i in start:
        if file.startswith(i):
            shutil.copyfile(os.path.join(file_patch, file), "./" + i + "/" + file)
