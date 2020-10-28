'''
PDF转图片
'''

import fitz
import os
from PyPDF2 import PdfFileReader

def PDF_Pic(doc,from_page,to_page):
    Doc=doc[0:-4]
    doc = fitz.open(doc)
    for pg in range(from_page-1,to_page):
        page = doc[pg]
        zoom = int(100)
        rotate = int(0)
        H=20; M=40; L=60
        trans = fitz.Matrix(zoom / M, zoom / M).preRotate(rotate)
        pm = page.getPixmap(matrix=trans,alpha=True)
        pm.writePNG(Doc+"%s.png" % str(pg+1))
    #print("操作完成!")
    p3="\n操作完成!\n"
    return p3


listdir = os.listdir('D:\\data\\hongtou')
if __name__ == '__main__':
    for pdf_files in listdir:
        pdf_file = os.path.join('D:\\data\\hongtou',pdf_files)
        reader = PdfFileReader(pdf_file)
        # 不解密可能会报错：PyPDF2.utils.PdfReadError: File has not been decrypted
        if reader.isEncrypted:
            reader.decrypt('')
        page_num = reader.getNumPages()
        print(page_num)
        PDF_Pic(pdf_file, 1, page_num)
