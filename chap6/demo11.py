# 学习时间：2022/9/14 15:00
# 内容：列表生成式
# 用这种方式快速生成列表
lst1=[i for i in range(1,10)]
print(lst1)

lst2=[i*i for i in range(1,10)]
print(lst2)

'''列表中的元素为2,4,6,8,10'''
lst3=[i for i in range(2,11,2)]
print(lst3)