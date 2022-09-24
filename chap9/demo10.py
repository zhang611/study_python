# 学习时间：2022/9/15 18:34
# 内容：格式化字符串
# %作为占位符
# %s字符串，%i%d整数，%f浮点数
name='张三'
age=20
print('我叫%s，今年%d岁' % (name,age))   # %()括号里面是一个元组

# {}作为占位符  format（）方法
print('我叫{0},今年{1}岁'.format(name,age))

# f-string
print(f'我叫{name},今年{age}岁')