# 学习时间：2022/9/14 14:33
# 内容：列表的删除
'''
1.remove()方式        一次删一个元素
2.pop（）方式         删除指定位置元素
3.切片               一次删多个
4.clear（）方式       清空列表
5.del               删除列表
'''
# remove方式
lst=[10,20,30,40,50,60,30]
lst.remove(30)   # 有重复，只会删除第一个元素;元素不存在会报错
print(lst)

# pop（）方式
lst.pop(1)   # 移除索引为1位置上的元素，不写默认移除最后一个；越界则报错
print(lst)
lst.pop()
print(lst)

# 切片  会创建新的列表
new_list=lst[1:3]
print('原表',lst)
print('切后',new_list)

# 切片  不产生新的列表
lst[1:3]=[]
print(lst)

# clear方式
lst.clear()
print(lst)

# del语句
del lst
# print(lst)   NameError: name 'lst' is not defined

