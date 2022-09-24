# 学习时间：2022/9/15 12:15
# 内容：字符串的查
# 可以把字符串看成关于字符的列表，类比列表的查
'''
index()方法，查子串第一次出现位置，不存在异常
rindex（）方法《查子串最后一次出现位置，不存在异常
find（）方法，查子串第一次出现位置，不存在返回-1
rfind（）方法，查子串最后一次出现位置，不存在返回-1
'''

# 和列表一样，有正向索引和逆向索引
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

print(s.find('k'))