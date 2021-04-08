import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models
import sys
import notify
import time

end_time = int(time.time())
start_time = end_time - 310
total_res = []
instance_info = [
    ('', 'cdb-')
]

for instance_name, instance_id in instance_info:
    try:
        cred = credential.Credential("", "")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdb.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cdb_client.CdbClient(cred, "a", clientProfile)

        req = models.DescribeSlowLogDataRequest()
        params = {
            "InstanceId": instance_id,
            "StartTime": start_time,
            "EndTime": end_time
        }
        req.from_json_string(json.dumps(params))

        resp = client.DescribeSlowLogData(req)
        res = resp.to_json_string()

        if json.loads(res)['TotalCount'] == 0:
            pass
        else:
            total_res.append(json.loads(res)['Items'])

    except TencentCloudSDKException as err:
        print(err)

if len(total_res) == 0:
    with open('slowsql.log', 'a') as f:
        f.write(str(time.time()) + 'no slowsql.\n')
    sys.exit(100)

for items in total_res:
    for item in items:
        notify.notify(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['Timestamp'])), item['QueryTime'], \
                      item['SqlText'], item['Database'], item['RowsExamined'], item['RowsSent'], token)


