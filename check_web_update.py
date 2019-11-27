"""python3"""
import hashlib
import os
from shutil import copyfile
from qmail import send_mail


def download_index():
    import urllib.request
    index = urllib.request.urlopen('http://www.yinwang.org')
    content = index.read()
    filename = open('index.html2', 'wb')
    filename.write(content)
    filename.close()

    if not os.path.exists('index.html'):
        copyfile('index.html2', 'index.html')


def diff_md5():
    html1 = hashlib.md5(open('index.html', 'rb').read()).hexdigest()
    html2 = hashlib.md5(open('index.html2', 'rb').read()).hexdigest()
    if html1 == html2:
        pass
    else:
        send_mail('1248247511@qq.com', '', '1248247511@qq.com', subject="yingwang.org has update")


if __name__ == '__main__':
    download_index()
    diff_md5()
    copyfile('index.html2', 'index.html')
