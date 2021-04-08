from urllib import request
import json


def notify(Timestamp, QueryTime, SqlText, Database, RowsExamined, RowsSent, token):
    notify_title = '生产环境数据库发现慢查询'
    notify_text = '### 生产环境数据库发现慢查询: ' + "\n"\
                  + '### 时间: ' + str(Timestamp) + "\n"\
                  + '### 执行时长: ' + str(QueryTime) + '秒' + "\n"\
                  + '### 执行语句: ' + "\n" \
                  + '```' + "\n" \
                  + str(SqlText) + "\n" \
                  + '```' + "\n" \
                  + '### 库名: ' + str(Database) + "\n"\
                  + '### 扫描行数: ' + str(RowsExamined) + "\n"\
                  + '### 结果集行数: ' + str(RowsSent)
    params = {
        "msgtype": "markdown",
        "markdown": {
            "title": notify_title,
            "text": notify_text
        }
    }
    params = bytes(json.dumps(params), 'utf8')
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    ding_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + str(token)

    req = request.Request(url=ding_url, data=params, headers=headers, method='POST')
    request.urlopen(req).read()


if __name__ == '__main__':
    notify()
