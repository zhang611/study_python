# 学习时间：2022/9/12 10:34
# 内容：数据类型，浮点型
a=3.14159
print(a,type(a))
'''
浮点数的存储可能不精确
计算机是二进制存储，这个问题是二进制的底层问题
导入decimal模块可以解决
'''
n1=1.1
n2=2.2
n3=2.1
print(n1+n2) # 这个有误差
print(n1+n3) # 这个正常

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))