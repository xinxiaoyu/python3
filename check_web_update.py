def download_index2():
    import urllib.request
    index=urllib.request.urlopen('http://www.yinwang.org')
    content=index.read()

    filename=open('/tmp/index.html2','wb')
    filename.write(content)
    filename.close()

def diff_md5():
    import hashlib
    html1=hashlib.md5(open('/tmp/index.html','rb').read()).hexdigest()
    html2=hashlib.md5(open('/tmp/index.html2','rb').read()).hexdigest()
    if html1 == html2:
        pass
    else:
        do_action()

def do_action():
    import os
    os.remove('/tmp/index.html')
    os.rename('/tmp/index.html2','/tmp/index.html')
    import qmail
    qmail.send_mail('','','',subject="")

if __name__ == '__main__':
    import time
    while True:
        download_index2()
        diff_md5()
        time.sleep(60)
