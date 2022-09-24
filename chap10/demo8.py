# 学习时间：2022/9/16 15:40
# 内容：变量的作用域

def fun(a,b):
    c=a+b             # 这个c就是局部变量，a，b也是局部变脸，出了函数这些变量都不存在
    print(c)

# print（c）会报错
# print（a）也会报错

name='zzc'    # 这个name就是全局变量，函数中也存在
print(name)
def fun2():
    print(name)

fun2()

def fun3():          # 使用关键字global，让局部变量变成全局变量
    global age
    age=20
    print(age)
fun3()
print(age)