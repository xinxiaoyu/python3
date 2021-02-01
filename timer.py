"""python3"""

import time
import winsound


def action(x, y):
    start_time = time.strftime('%H:%M')
    end_time = time.strftime('%H:%M')
    print('开始时间 {0}'.format(start_time))
    for i in range(x, y):
        time.sleep(60)
        print('已用 {0} 分钟'.format(i))
    print('结束时间 {0}'.format(end_time))
    winsound.Beep(2000, 10000)


action(1, 2)
#test
