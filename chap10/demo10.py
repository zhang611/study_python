# 学习时间：2022/9/16 15:53
# 内容：递归函数算斐波那契数列
# 1 1 2 3 5 8 13 前两项是1，后面每一项是前两项的和

def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)

print(fun(7))
for i in range(8):
    print(fun(i+1))