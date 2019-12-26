#提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=1920,height=1080):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("'D:\\code\\MNasNet-Keras-Tensorflow-master\\dataset\\5Chinese_national_flag\\003870.jpg'"):
    convertjpg(jpgfile, "C:\\Users\\rmzk\\Desktop\\aa")
