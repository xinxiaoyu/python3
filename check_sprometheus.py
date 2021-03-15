from urllib import request
from datetime import date, timedelta
import time
import re
import json
import os


time_now = str(time.time())
today = date.today()
yesterday = today - timedelta(days=1)
prom_url = 'http://abc.com/api/v1/query?query=up%7Bjob%3D%22consul_eureka%22%7D&time='\
           + str(time_now)+'&_=' + str(time_now)
ding_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + \
           ''

get_url = request.urlopen(prom_url)
data = get_url.read()
data_bytes = data.decode('utf-8')
app = re.findall(r'application":"(.+?)"?,"instance', data_bytes)


def notice():
    diff = set(app).symmetric_difference(set(list_app))
    params = {
        "msgtype": "text",
        "text": {"content": "发现有新增或删除的应用: " + str(diff)}
    }
    params = bytes(json.dumps(params), 'utf8')
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}

    req = request.Request(url=ding_url, data=params, headers=headers, method='POST')
    request.urlopen(req).read()


if os.path.exists(str(yesterday) + '.txt'):
    with open(str(yesterday) + '.txt', 'r') as f:
        list_app = []
        for line in f:
            line = line.strip('\n')
            list_app.append(line)
    if set(app).symmetric_difference(set(list_app)):
        notice()
    os.remove(str(yesterday) + '.txt')
else:
    print(str(yesterday) + '.txt 文件不存在.')

with open(str(today) + '.txt', 'w') as f1:
    for line1 in set(app):
        f1.write(line1 + '\n')
