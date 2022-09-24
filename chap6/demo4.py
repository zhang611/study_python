# 学习时间：2022/9/14 13:50
# 内容：列表中多个元素的查
lst=['hello','world',98,'hello']
# 获取列表中制定元素的索引，index（）方法，注意这里不是函数，给元素出索引
print(lst.index('hello'))  # 存在重复元素，只返回第一个的索引
print(lst.index('hello',1,4))  # 在1-4之间找hello，还是老样子，从1开始，不包括4，就是在索引1,2,3之中找hello

# 获取列表中的单个元素，给索引出元素
print(lst[2])
print(lst[-3])