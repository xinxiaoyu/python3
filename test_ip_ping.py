import os
from urllib import request
import json

ding_url = 'https://oapi.dingtalk.com/robot/send?access_token='


def notice():
    params = {
        "msgtype": "text",
        "text": {"content": "测试: ping成功"}
    }
    params = bytes(json.dumps(params), 'utf8')
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}

    req = request.Request(url=ding_url, data=params, headers=headers, method='POST')
    request.urlopen(req).read()


ip_list = ['174.137.63.74', 'www.baidu.com']
cmd = 'ping -c 1'
for i in ip_list:
    if os.system('ping -n 1 ' + i):
        pass
    else:
        notice()
