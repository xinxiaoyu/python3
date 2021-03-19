from urllib import request, error
import json

check_url = [
    ('a登陆页面', 'https://mgt.a.com/adminCenter/#/login/admin'),
    ('b登陆页面', 'https://www.a.com/userCenter/#/login/user'),
    ('prod-a', 'http://prometheus.a.com'),
    ('prod-b', 'http://alertmanager.a.com'),
    ('c页面', 'https://www.a.com')
]
ding_url = 'https://oapi.dingtalk.com/robot/send?access_token='


def notify(url_name, url):
    notify_title = url_name + '告警'
    notify_text = '### ' + str(url_name) + '发现异常: ' + str(e.reason) + '\n'\
                  + '##### 地址: [' + str(url) + '](' + str(url) + ')'
    params = {
        "msgtype": "markdown",
        "markdown": {
            "title": notify_title,
            "text": notify_text
        }
    }
    params = bytes(json.dumps(params), 'utf8')
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}

    req = request.Request(url=ding_url, data=params, headers=headers, method='POST')
    request.urlopen(req).read()


for url_name, url in check_url:
    try:
        response = request.urlopen(url)
    except error.HTTPError as e:
        notify(url_name, url)
    except error.URLError as e:
        notify(url_name, url)
