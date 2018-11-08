"""python3"""

import hashlib
import time

from qmail import send_mail


def download_index():
    import urllib.request
    index = urllib.request.urlopen('http://www.yinwang.org')
    content = index.read()
    filename = open('/tmp/index.html', 'wb')
    filename.write(content)
    filename.close()


def html1():
    global html1
    html1 = hashlib.md5(open('/tmp/index.html', 'rb').read()).hexdigest()


def html2():
    global html2
    html2 = hashlib.md5(open('/tmp/index.html', 'rb').read()).hexdigest()


def diff_md5():
    if html1 == html2:
        pass
    else:
        send_mail('1248247511@qq.com', '', '1248247511@qq.com', subject="yingwang.org has update")


download_index()
html1()

while True:
    time.sleep(60)
    download_index()
    html2()
    diff_md5()
