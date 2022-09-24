# 学习时间：2022/9/14 16:37
# 内容：键（key）的判断;字典元素删除；字典元素新增,修改

# 用in，not in判断键是否在字典中
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

# 字典元素删除，用del语句,删指定的键值对
del scores['张三']
print(scores)

# 清空字典的元素，全删，用clear（）方式
scores.clear()
print(scores)

# 字典中新增
scores['陈六']=98
print(scores)

# 修改字典的元素，给指定的键改值
scores['陈六']=100
print(scores)