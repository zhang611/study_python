# 学习时间：2022/9/16 14:42
# 内容：函数参数传递内存分析
'''
不可变对象，函数无法修改实参的值，在函数内部可以改一下他的复制品，字符串，数字改不了
可变对象，函数可以修改实参的值，可以改列表
'''

def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(55)
    print('arg1=',arg1)
    print('arg2=',arg2)


n1=11
n2=[22,33,44]
print(n1)
print(n2)
print('-------------------')
fun(n1,n2)
print(n1)
print(n2)