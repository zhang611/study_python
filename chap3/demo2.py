# 学习时间：2022/9/12 14:21
# 内容：从键盘录入两个整数，并求和

a=input('输入第一个数：')
b=input('输入第二个数：')
# print(a+b) 这样是错的，输入的是字符串类型，要转成int
print(int(a)+int(b))  # 这样才可以