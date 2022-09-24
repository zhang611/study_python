# 学习时间：2022/9/14 19:42
# 内容：集合的判断in ， not in;新增，删除
# 集合元素的判断操作
s={10,20,30,152,200}
print(10 in s)
print(120 not in s)

# 集合的新增，add（）方法，一次加一个元素
s.add(100)
print(s)

# 集合的新增，update（）方式，一次加多个元素
s.update({200,300,400})  # 放集合
print(s)
s.update([2,3,4])   # 放列表
s.update((25,41,63))  # 放元组
print(s)

# 集合的删除，remove（）方法，一次删一个，元素不存在会出异常
s.remove(100)
print(s)
# s.remove(1000)  集合中没有1000，这样删的话会报错，KeyError: 1000

# 集合的删除，discard（）方法，一次删一个，元素不存在不会异常
s.discard(200)
print(s)
s.discard(1000)   # 没有1000，但是删了亦不会报错
print(s)

# 集合的删除，pop（）方法，一次只删一个任意元素
s.pop()     # 这个方法没有参数，也不能指定参数，否则会异常
print(s)

# 集合的删除，clear（）方法，全删
s.clear()
print(s)

