# 学习时间：2022/9/14 16:29
# 内容：获取字典中的值，知道了键要想知道值
'''
1.使用[]
2.get（）方法
'''
# 使用中括号
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])
# print(scores['陈六'])    KeyError: '陈六'   这个找不存在的会直接报错

print()

# 使用get（）方法    这样更好
print(scores.get('张三'))
print(scores.get('陈六'))   # None  不会报错，只显示不存在
print(scores.get('麻七',99))  # 如果不存在，返回99