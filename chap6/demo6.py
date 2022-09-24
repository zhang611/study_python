# 学习时间：2022/9/14 14:13
# 内容：1.判断指定的元素在列表中是否存在，用in，not in
#      2.遍历列表中的元素，用for...in
print('p' in 'python')
print('k' not in 'python')

lst=[10,20,'hello','world']
print(10 in lst)
print(100 not in lst)

for i in lst:
    print(i,end='\t')  # 这样写代表不换行输出