# 学习时间：2022/9/15 17:55
# 内容：字符串的比较操作，比较运算符

print('apple'>'app')  # True，比出大小
# 每个字符串的第一个字符比，相等则比第二个字符，以此类推
# 比较原理：比字符的原始值，用ord（）函数可以看见，chr（原始值）为逆函数

print('apple'>'banana')
print(ord('a'),ord('b'))
print(chr(97),chr(98))