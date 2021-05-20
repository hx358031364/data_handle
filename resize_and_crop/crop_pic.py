from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir):
    img = Image.open(jpgfile)
    width = img.size[0] * 0.3
    height = img.size[1] * 0.4
    print(width,height)
    region = img.crop((0, 0, width, height))
    region.save(os.path.join(outdir, os.path.basename(jpgfile)))
for jpgfile in glob.glob("D:\\data\\beijingweishi\\*.jpg"):
    convertjpg(jpgfile, "D:\\data_resize\\BTV\\")
