from PIL import Image, ImageDraw, ImageFont
import os

def add_shuiyin(save_path,label,imageFile,fontOne):
    imageInfo = Image.open(imageFile)
    draw = ImageDraw.Draw(imageInfo)
    print(imageInfo.size)

    # draw.text((imageInfo.size[0]*0.16, imageInfo.size[1] * 0.04), label, fill=(0, 0, 0), font=fontOne)
    draw.text((imageInfo.size[0]*0.7, imageInfo.size[1] * 0.04), label, fill=(0, 0, 0), font=fontOne)
    imageInfo.save(r"{}".format(save_path))

fontOne=ImageFont.truetype("c:/Windows/Fonts/SIMSUN.TTC", 35)
labes = ["秘密★3年", "秘密★5年", "秘密★10年",
         "秘密★三年", "秘密★五年", "秘密★十年",
         "机密★3年", "机密★5年", "机密★10年",
         "机密★三年", "机密★五年", "机密★十年",
         "绝密★3年", "绝密★5年", "绝密★10年",
         "绝密★三年", "绝密★五年", "绝密★十年"]
listdir = os.listdir('./test_file')
if __name__ == '__main__':
    for i in range(0,18):
        label = labes[i]
        for f in listdir:
            file_path = os.path.join('./test_file', f)
            add_shuiyin('D:\\data\\mb\\mb_tietu\\r_{}_{}'.format(str(i), f), label, file_path, fontOne)
    print("success")