# 当前目录下所有文件夹下的文件名(不带后缀)写入对应txt文件(以文件夹命名)中
import os

# 如果文件夹不存在创建文件夹
def Makedir(path):
    folder = os.path.exists(path)
    if (not folder):
        os.makedirs(path)

# 利用os.listdir()、os.walk()获取文件夹和文件名
def GetFileName(fileDir, outDir):
    list_name = []
    Makedir(outDir)
    for dir in os.listdir(fileDir):  # 获取当前目录下所有文件夹和文件(不带后缀)的名称
        filePath = os.path.join(fileDir, dir)  # 得到文件夹和文件的完整路径
        if os.path.isdir(filePath) and not (filePath == outDir):
            txt = outDir + dir + ".txt"
            # 获取根目录路径、子目录路径，根目录和子目录下所有文件名
            for root, subDir, files in os.walk(filePath):
                for fileName in files:
                    f = open(txt, 'a')  # 以追加方式打开文件
                    fileName = os.path.splitext(fileName)[0] + '\n'  # 分割，不带后缀名
                    f.write(fileName)
                    f.close()

def main():
    fileDir = "D:\\data\\test\\"  # 输入文件夹路径
    outDir = "D:\\data\\test\\FileData\\"
    files = GetFileName(fileDir, outDir)

# 判断是否是程序主入口而已，如果是程序主入口，则代码块执行，否则代码块不执行
# 主要用于别人调用此代码时，不要进入该代码的入口
if __name__ == "__main__":
    main()

