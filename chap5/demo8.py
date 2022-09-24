# 学习时间：2022/9/13 16:07
# 用while实现输入三次密码，和demo7一起看
a=0
while a<3:
     pwd=input('请输入密码：')
     if pwd=='8888':
         print('密码正确')
         break
     else:
         print('密码错误')
     a+=1