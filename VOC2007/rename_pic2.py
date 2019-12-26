import os
jpg_path = "E:\\改格式"
jpg_filelist = os.listdir(jpg_path) #该文件夹下所有的文件（包括文件夹）
count=0

def get_all_files(dir):
    files_ = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_


files = get_all_files(jpg_path)
print(files)

for f in files:
    os.rename(f,f+str(count)+".jpg")
    count+=1
