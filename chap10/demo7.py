# 学习时间：2022/9/16 15:32

def fun1(a,b=10):   # b是默认形参
    print('a=',a)
    print('b=',b)

def fun2(*args):   # 个数可变的位置形参
    print(args)

def fun3(**args):   # 个数可变的关键字形参
    print(args)

fun2(10,20,30,40,50)       # 传多少都可以
fun3(a=11,b=22,c=33,d=44)  # 传多少都可以

def fun4(a,b,*,c,d):  # 中间加个*，是指c和d只能用关键字参数传递
    print(a,b,c,d)
fun4(10,20,d=30,c=40)