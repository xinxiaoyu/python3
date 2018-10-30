import subprocess
import qmail
import time


def sendmail1():
    qmail.send_mail(from_addr='1248247511@qq.com', password='', to_addr='1248247511@qq.com',
                    subject='lang_mail_yes', content='This is a test mail!')

def sendmail2():
    qmail.send_mail(from_addr='1248247511@qq.com', password='', to_addr='1248247511@qq.com',
                    subject='no', content='This is a test mail!')

a = 0

def testvpn():
    p = subprocess.Popen(['ping', '-c', '1', '103.210.23.200'])
    p.wait()

    global a
    if p.poll() == 0:
        a += 1
        if a == 1:
            sendmail1()
        else:
            print('pass')
    else:
        sendmail2()
        a = 0

while True:
    testvpn()
    time.sleep(60)
