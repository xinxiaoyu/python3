from urllib import request, parse
import time
import re
import json
import requests

time = str(time.time())
url = 'http://prometheus.abc.com/api/v1/query?query=up%7Bjob%3D%22consul_eureka%22%7D&time='+time+'&_='+time

get_url = request.urlopen(url)
data = get_url.read()
data_bytes = data.decode('utf-8')
app = re.findall(r'application":"(.+?)"?,"instance', data_bytes)

dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token='
data2 = {
    "msgtype": "text",
    "text": {"content": "application-number: " + str(len(set(app)))}
}
headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}

r = requests.post(url=dingding_url, data=json.dumps(data2), headers=headers)

print(r.json())
