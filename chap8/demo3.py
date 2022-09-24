# 学习时间：2022/9/14 19:07
# 内容：不可变序列好处
'''
多任务环境下，同时操作对象不用加锁
很多人都要用同一个数据的时候，可变序列就要加锁不然就乱套了
元组的内部元素可以混合列表，int，字符串都可以，是列表的时候，在列表后面追加数据，这是可以的
'''
t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))  # 用这种方式获取元组中的数据

# t[1]=100  会报错，元组是不可以修改元素的
t[1].append(100)  # t1是列表，是可变序列，可以在可变序列后加元素
print(t[1])
print(t)