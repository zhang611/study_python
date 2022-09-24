# 学习时间：2022/9/11 21:09
# 目的：print函数的使用
# print 函数可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('hello world')
print("hello world")
# print(hello world)输出字符串必须要加单引号或者双引号，不然计算机无法识别

# 可以输出含有运算符的表达式
print(3+1)
print()

'''
# 将数据输出到文件中
fp = open('C:/text.txt','a+')
print('hello world',file=fp)
fp.close()
# 代码应该没错，但是还是报错了，可能是不能往c盘里面写东西，我电脑没有分盘，所以写不了
'''

# 不进行换行输出，输出内容在同一行
print('hello', 'world', 'python')
# 用逗号进行分隔，结果会在一行输出