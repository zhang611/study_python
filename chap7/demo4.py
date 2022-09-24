# 学习时间：2022/9/14 16:46
# 内容：字典的视图操作
'''
获取字典视图的三个方法
1.keys（）方法    获取字典的所有键（key）
2.values（）方法  获取字典的所有值（value）
3.items（）方法   获取字典中所有键值对（key，value）
'''
scores={'张三':100,'李四':98,'王五':45}
# 获取所有的键
a=scores.keys()
print(a)
print(type(a))
print(list(a))   # 使用list函数把所有的键值转化为列表

# 获取所有的值
b=scores.values()
print(b)
print(type(b))
print(list(b))

# 获取所有的键值对
c=scores.items()
print(c)   # 这里以元组的形式打印出来
print(type(c))
print(list(c))  # 转换之后的列表元素是由元组组成的
