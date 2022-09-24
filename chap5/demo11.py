# 学习时间：2022/9/13 16:29
# 接demo10，while循环中用else

a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('已连续三次输入错误，十分钟以后再试')