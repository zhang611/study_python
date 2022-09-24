# 学习时间：2022/9/15 19:09
# 内容：函数的创建和调用

# 函数调用的参数传递
'''
1.位置实参，第一个位置的实参给第一个位置的形参
2.关键字实参，根据形参的名称传实参
'''

def calc(a,b):   # 这个ab是形参
    c=a+b
    return c

result = calc (10,20)     # 这个10,20是实参
print(result)

result2= calc (b=200,a=300)
print(result2)