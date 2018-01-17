import subprocess
import  mail2
import time

def testvpn():
    p = subprocess.Popen('ping -n 1 47.90.1.81')
    p.wait()

    if p.poll() == 0:
        mail2.send_mail(from_addr='1248247511@qq.com',password='',to_addr='1248247511@qq.com',subject='yes',content='This is a test mail!')
    else:
        mail2.send_mail(from_addr='1248247511@qq.com', password='', to_addr='1248247511@qq.com',
                        subject='no', content='This is a test mail!')

while True:
    testvpn()
    time.sleep(3600)
