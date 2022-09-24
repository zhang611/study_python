# 学习时间：2022/9/13 14:17
# 内容：条件表达式
# 语法结构：x if 判断条件 else y
#
# 从键盘录入两个整数，比大小
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
# 比大小
'''
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
    上面是正常写法，下面用条件表达式写
'''
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
# 先把int型的数字变成字符串，再用字符串的连接，连起来输出
# if和else之间是条件判断，为真输出if前面的，为假输出else后面的