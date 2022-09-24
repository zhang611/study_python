# 学习时间：2022/9/13 16:22
# 内容：else语句
'''
和if搭配        if不成立，执行else
和while搭配     没有break，执行else
和for搭配       for循环都执行完了也没有遇到过break，就要执行else
'''

# 还是输入密码的问题
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('三次密码都错误，十分钟后再试')