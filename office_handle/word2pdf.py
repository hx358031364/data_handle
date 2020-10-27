# !/usr/bin/env python
# coding=utf-8
from multiprocessing import Pool
import os
from win32com.client import Dispatch, constants, gencache


def doc2pdf(doc_name, pdf_name):
    gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
    w = Dispatch("Word.Application")
    try:
        doc = w.Documents.Open(doc_name, ReadOnly=1)
        doc.ExportAsFixedFormat(pdf_name, constants.wdExportFormatPDF, Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    except Exception as e:
        print(e)
        return 1
    finally:
        w.Quit(constants.wdDoNotSaveChanges)


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for root, ds, fs in os.walk('D:\\code\\data_handle\\office_handle\\test_file'):  # 网上这步没有写入放入word的路径，就会导致转成功后不知道pdf在哪里，这步很关键。
        for f in fs:
            fullname = os.path.join(root, f)
            if 'docx' in fullname:
                name, suffix = fullname.split(".")
                pdf = "{}.pdf".format(name)
                p.apply_async(doc2pdf, args=(fullname, pdf))

    p.close()
    p.join()

    print('All subprocesses done.')