# 学习时间：2022/9/15 12:55
# 内容：字符串的对齐操作
'''
1.center()方法  居中对齐
2.ljust（）方法，左对齐
3.rjust（）方法，右对齐
4.zfill（）方法，右对齐
'''
s='hello,Python'
print(s.center(20,'*'))  # 在20个位置的中间，其他位置用*填充
print(s.ljust(20,'*'))   # 左对齐，其他位置用*填充
print(s.ljust(10))
print(s.ljust(20))

print(s.rjust(20,'*'))
print(s.rjust(10))
print(s.rjust(20))

print(s.zfill(20))   # 右对齐，使用0进行填充
print(s.zfill(10))
print('-8910'.zfill(8))  # 注意0填充到了什么位置