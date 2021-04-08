import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import time
from datetime import date, timedelta
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.monitor.v20180724 import monitor_client, models
import if_web

while True:
    if if_web.if_ok() == 0:
        break
    else:
        time.sleep(60)

try:
    cred = credential.Credential("", "")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "monitor.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = monitor_client.MonitorClient(cred, "", clientProfile)

    req = models.GetMonitorDataRequest()
    params = {
        "Namespace": "",
        "MetricName": "",
        "Period": 60,
        "StartTime": str(date.today()-timedelta(days=1)) + "T07:00:00+08:00",
        "EndTime": str(date.today()-timedelta(days=1)) + "T23:50:00+08:00",
        "Instances": [
            {
                "Dimensions": [
                    {
                        "Name": "vip",
                        "Value": ""
                    }
                ]
            }
        ]
    }
    req.from_json_string(json.dumps(params))

    resp = client.GetMonitorData(req)
    res = resp.to_json_string()

except TencentCloudSDKException as err:
    print(err)


timestamps = json.loads(res)["DataPoints"][0]['Timestamps']
values = json.loads(res)["DataPoints"][0]["Values"]

import second

new_values = []
for i in range(len(values)):
    new_values.append(round(values[i] + second.values[i], 2))

new_timestamps = []
for j in timestamps:
    time_local = time.localtime(j)
    new_timestamps.append(time.strftime("%H:%M", time_local))


def plot_curve1(x, y, title):
    plt.figure(figsize=(15, 5))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=2))
    plt.title(title, fontproperties='SimHei')
    plt.plot(pd.to_datetime(x), y)
    plt.ylabel(u'单位: Mbps', fontproperties='SimHei')
    plt.xlabel(u'时间', fontproperties='SimHei')
    plt.savefig(r'D:\images\traffic' + str(date.today()) + '.png')


plot_curve1(new_timestamps, new_values, u'昨天' + u'(' + str(date.today()-timedelta(days=1)) + u')' + u'带宽')

import main


main.notice()

import os

if os.path.exists(r'D:\images\traffic' + str(date.today()) + '.png'):
    os.remove(r'D:\images\traffic' + str(date.today()) + '.png')
