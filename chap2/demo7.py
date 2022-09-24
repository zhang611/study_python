# 学习时间：2022/9/12 10:47
# 内容：数据类型，字符串
'''
不可变的字符序列，可不可变和列表对比理解
可用单引号，双引号，三引号定义字符串
单，双引号定义的字符串必须在一行
三引号定义的字符串可在连续的多行
'''
str1='人生苦短，我学python'
str2="人生苦短，我学python"
str3='''人生苦短，
我学python'''
str4="""人生苦短，
我学python"""

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))