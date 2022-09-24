# 学习时间：2022/9/14 20:07
# 内容：集合的数学操作
'''
交集：两个集合共有的
并集：包含两个集合的集合
差集：a集合减去ab所共有的，或者，b集合减去ab所共有的
对称差集：两集合的并集减去交集
注意：这些操作之后原集合都不会发生变化
'''
# 交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)  # 这也表示求交集

# 并集操作
print(s1.union(s2))
print(s1 | s2)  # 这也表示求并集

# 差集操作
print(s1.difference(s2))
print(s1 - s2)  # 这也表示求差集

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)     # 这也表示对称差集
