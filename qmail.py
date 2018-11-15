import smtplib
from email.message import EmailMessage


def send_mail(from_addr='', password='', \
              to_addr='', subject='', \
              content=''):
    msg = EmailMessage()
    msg['Subject'] = '%s' % subject
    msg['From'] = '%s' % from_addr
    msg['To'] = '%s' % to_addr
    msg.set_content(content)
    s = smtplib.SMTP('smtp.qq.com','587')
    s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(msg['From'], password)
    s.send_message(msg)
    s.quit()

    
if __name__ == '__mail__':
    send_mail()
