# 学习时间：2022/9/15 17:25
# 内容：字符串的劈分
'''
split()方法，从左分，默认劈分符是空格，返回值是列表
rsplit（）方法，从右边开始劈分
'''
s='hello world python'
lst=s.split()          # 默认分隔符就是空格
print(lst)
s1='hello|world|python'
print(s1.split(sep='|'))    # 这里使用到了关键字sep指定分隔符
print(s1.split(sep='|',maxsplit=1))  # 这里用到了关键字 maxsplit ，指最大分几次

print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit('|',maxsplit=1))  # 和split（）方法的区别，要通过maxsplit看出