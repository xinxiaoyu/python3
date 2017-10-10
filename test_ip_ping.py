import subprocess
import  mail2

def testvpn():
    p = subprocess.Popen('ping -n 1 47.90.1.81')
    p.wait()

    if p.poll() == 0:
        mail2.send_mail(from_addr='1248247511@qq.com', password, to_addr='1248247511@qq.com')
    else:
        mail2.send_mail(from_addr='1248247511@qq.com', password, to_addr='1248247511@qq.com')

testvpn()
