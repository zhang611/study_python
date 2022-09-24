# 学习时间：2022/9/16 15:47
# 内容：递归函数  计算阶乘

def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)

print(fun(6))