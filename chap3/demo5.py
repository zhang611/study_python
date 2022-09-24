# 学习时间：2022/9/12 14:58
# 内容：比较运算符
# 其结果为布尔类型
a,b=10,20
print("a>b吗？",a>b)  # False
print("a<b吗？",a<b)  # True

# 就是这样，很简单，没什么好说的
# >,<,>=,<=,==,!=这六个符号
# 比较运算符比较的是值，is比较的是id（标识）

a=10
b=10
print(a==10)        # True
print(a is b)       # True
print(a is not b)   # False 就是和上面那个互逆
# 从这里理解变量，a和b都指向同一个地方，那个地方存10，值也一样，标识也一样

list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)        # True
print(list1 is list2)      # False
print(list1 is not list2)  # True  就是和上面那个互逆
print(id(list1))
print(id(list2))
