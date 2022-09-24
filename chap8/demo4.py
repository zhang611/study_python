# 学习时间：2022/9/14 19:20
# 内容：元组的遍历
# 元组是可迭代对象，可以用for...in遍历
# 元组也可以像列表一样通过索引获取

t=('python','world',98)
# 通过索引获得元组元素
print(t[0])   # 元组和列表很像，就是不可变，用索引的时候也是用中括号，这样记
print(t[1])   # 不知道元组里面的元素格式可能会越界
print(t[2])
# print(t[3])  这样就会报错，索引超出范围

print()

# 通过遍历元组获得元组元素
for item in t:
    print(item)