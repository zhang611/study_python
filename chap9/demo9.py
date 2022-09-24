# 学习时间：2022/9/15 18:03
# 内容：字符串的切片,类比列表的切片
# 字符串和列表不同，是不可以修改的，只能切
# 按索引切
s='hello,python'
s1=s[:5]
s2=s[6:]
s3='!'
new_str=s1+s3+s2

print(s1)
print(s2)
print(new_str)

print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new_str))   # 一共五个字符串参与运算

print(s[::2])   # 第三个参数是步长
print(s[::-1])  # 倒着输出了
print(s[-6::1])