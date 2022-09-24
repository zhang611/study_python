# 学习时间：2022/9/14 19:56
# 内容：集合之间的关系,相等，子集，交集，超集

# 判断两个集合是否相等
s1={10,20,30,40}
s2={40,20,10,30}
print(s1==s2)
print(s1!=s2)

# 一个集合是否是另一个集合的子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))  # s2是s1的子集，
print(s3.issubset(s1))  # s3不是s1的子集

# 一个集合是否是另一个集合的超集
print(s1.issuperset(s2))   # s1是s2的超集
print(s1.issuperset(s3))   # s1不是s3的超集

# 两个集合是否有交集
print(s1.isdisjoint(s2))  # 是否没有交集，否，就是有交集
print(s1.isdisjoint(s3))