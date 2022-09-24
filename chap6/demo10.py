# 学习时间：2022/9/14 14:51
# 内容：列表的排序
'''
1.sort()方法     默认是升序
2.sorted（）函数
'''
lst=[20,40,10,98,54]
print('排序前的列表',lst,id(lst))

lst.sort()
print('排序后的列表',lst,id(lst))  # id不变，没有产生新的列表

lst.sort(reverse=True)  # 降序排序
print(lst)

# 使用内置函数sorted（），会产生新的列表对象
lst=[20,40,10,98,54]
new_lst=sorted(lst)    # 用函数，产生了新的列表对象
print(lst)
print(new_lst)
lst2=sorted(lst,reverse=True)  # 还是使用关键字reverse变成降序
print(lst2)
