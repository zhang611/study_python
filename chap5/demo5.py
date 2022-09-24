# 学习时间：2022/9/13 15:36
# n内容：for—in循环
'''
in表示从字符串，序列等中依次取值，也叫遍历
遍历对象必须是课迭代对象
'''
for item in 'python':
    print(item)

for i in range(5):
    print(i)

# 如果不需要自定义变量，则写成下划线_
for _ in range(3):
    print('人生苦短，我学python')

# 用for循环计算1到100整数和
sum=0
for item in range(101):
    sum+=item
print('1到100之间整数和为：',sum)

# 用for计算1到100之间的偶数和
sum=0
for a in range(101):
    if a%2==0:
        sum+=a
print('1到100之间的整数和为：',sum)
