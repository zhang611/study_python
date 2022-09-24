# 学习时间：2022/9/14 18:55
# 内容：元组的创建方式
'''
1.使用小括号定义，逗号分隔
2.使用内置函数tuple（）
注意：只包含一个元素的元组要用逗号和小括号t=(10,)
'''
# 使用小括号创建
t=('python','world',98)
print(t)
print(type(t))

# 第一种方式的小括号是可以不写的
t2='python','world',98   # 这种方式就省略了小括号
print(t2)
print(type(t2))

t3=('world')
print(t3,type(t3))   # 只有一个元素，不加逗号，会被认为是str
t4=('world',)
print(t4,type(t4))   # 加了逗号就是元祖


print()

# 使用内置函数tuple（）
t1=tuple(('python','world',98))   # 注意这里有两个括号
print(t1)
print(type(t1))

# 空列表
lst=[]
lst1=list()
print(lst,lst1)

# 空字典
d={}
d1=dict()
print(d,d1)

# 空元组
t4=()
t5=tuple()
print(t4,t5)