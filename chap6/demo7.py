# 学习时间：2022/9/14 14:19
# 内容：列表的增加
'''
1.append()方式      列表末尾加一个元素
2.extend（）方式     列表末尾加多个元素
3.insert（）方式     列表任意位置加一个元素
4.切片              列表任意位置加多个元素
'''
# append（）方式
lst1=[10,20,30]
print(lst1,id(lst1))
lst1.append(100)
print(lst1,id(lst1))  # 标识不变，没有创建新的列表对象

# extend（）方式
lst2=['hello','world']
lst1.append(lst2)
print(lst1)  # 会把lst2作为一个元素放在lst1中，append（）方式只能加一个元素
lst1.extend(lst2)
print(lst1)

# insert()方式
lst1.insert(1,90)
print(lst1)

# 切片方式
lst3=[True,False,'hello']
lst1[1:]=lst3  # 把切掉的部分用新的列表替换
print(lst1)