# 学习时间：2022/9/13 13:16
# 内容：对象的布尔值
# python中一切皆对象，都有其布尔值
'''
以下对象的布尔值是False
False
数值0
None
空字符串
空列表
空元组
空字典
空集合
'''
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))       # 空列表
print(bool(list()))   # 空列表
print(bool(()))       # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))       # 空字典
print(bool(dict()))   # 空字典
print(bool(set()))    # 空集合

print('其他对象的布尔值都为True')