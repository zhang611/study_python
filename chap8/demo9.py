# 学习时间：2022/9/14 20:18
# 内容：集合生成式
# 列表生成式的[]改成{}就可以了
# 注意没有元组生成式

# 列表生成式
lst=[i*i for i in range(6)]
print(lst)

# 集合生成式
s={i*i for i in range(6)}
print(s)