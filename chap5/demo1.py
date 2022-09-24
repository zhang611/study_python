# 学习时间：2022/9/13 15:01
# 内容：内置函数range（）
# 返回值是迭代器对象
# 优点：无论值多大，内存中只存三个参数，用到才计算，不然不算
# 经常使用range函数做for循环的对象
'''
生成一个整数序列
range（stop）
range（star，stop）
range（star，stop，step）
'''
# range的三种创建方式
r=range(10)  # 默认从0开始，默认步长为1，共十个数
print(r)
print(list(r))  # 用于查看range中的整数序列，list是列表

r=range(1,10)   # 指定了从1开始到10结束，注意不包含右边的10，默认步长为1
print(r)
print(list(r))

r=range(1,10,2)  # 三个参数都给了，从1开始到10结束，步长为2
print(r)
print(list(r))

'''判断指定的整数在序列中是否存在用in，not in'''
print(7 in r)