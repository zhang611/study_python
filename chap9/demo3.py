# 学习时间：2022/9/15 12:22
# 内容：字符串的大小写转换
'''
1.upper()方法，所有字符转大写
2.lower（）方法，所有字符转小写
3.swapcase（）方法，大转小，小转大
4.capitalize（）方法，第一个字符大写，其他小写
5.title（）方法。每个单词，首字母大写，其他小写
'''
s='hello,python'
a=s.upper()
print(a,id(a))  # 字符串是不可变序列，转成大写之后会产生新的字符串对象
print(s,id(s))
print(s.lower(),id(s.lower()))

s2='hello,Python'
print(s2)
print(s2.swapcase())
print(s2.capitalize())
print(s2.title())