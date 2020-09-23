# @Time    : 2020/9/23 10:34
# @Author  : Arvin
# @File    : DocumentOp2.py
# @Software: PyCharm
# @Title   :

import os
import docx
from win32com import client
import re
import camelot

if __name__ == '__main__':
    path = 'E:/Arvin/Document/WebCrawler/DocumenOp/documents'
    files = os.listdir(path)
    print(files)
    for file in files:
        print(file)
        file_path = 'E:/Arvin/Document/WebCrawler/DocumenOp/documents/' + file
        tables = camelot.read_pdf(file_path, pages='1', flavor='stream')
        print(tables)
        print(tables[0])
        print(tables[0].data)