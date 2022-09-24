# 学习时间：2022/9/23 14:32
# 第三方模块的安装 pip方式

import schedule
import time

def job():
    print('哈哈-----')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


# 可以使用这个做定时发送邮件