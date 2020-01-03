import matplotlib.pyplot as plt
import numpy as np
import os
txt_path = "D:\\data\\predictimg\\FileData"
txt_file_list = os.listdir(txt_path)

for file in txt_file_list:
    file_path = os.path.join(txt_path,file)
    loadtxt = np.loadtxt(file_path)
    plt.hist(x=loadtxt, bins=20, color='steelblue', edgecolor='black')
    plt.xlabel("score")
    plt.ylabel("number")
    file_name = file.split('.')[0]
    plt.title(file_name)
    plt.savefig("./" + file_name + ".jpg")
    plt.show()








