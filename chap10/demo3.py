# 学习时间：2022/9/16 14:54
# 内容：函数的返回值
# 有多个返回值时，结果为元组

def fun(num):
    odd=[]     # 存奇数
    even=[]    # 存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,23,44,53,55]))