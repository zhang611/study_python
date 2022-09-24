# 学习时间：2022/9/23 14:24
# python中的常用模块

import sys
import time
import urllib.request  # 爬虫的时候经常使用
print(sys.getsizeof(24))   # 看占了多少字节
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print('------------------')
print(time.time())  # 输出的是秒
print(time.localtime(time.time()))  # 转换成具体时间
print('-----------------')
print(urllib.request.urlopen('http://www.baidu.com').read())