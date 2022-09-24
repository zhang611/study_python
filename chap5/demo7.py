# 学习时间：2022/9/13 16:01
# break语句，用于结束循环，和if一起使用
'''
从键盘录入密码，最多三次，如果正确就结束循环
'''
for _ in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
