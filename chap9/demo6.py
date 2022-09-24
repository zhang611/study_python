# 学习时间：2022/9/15 17:34
# 内容：字符串的判断
'''
isidentifier()方法判断字符串是否是合法的标识符
isspace（）方法，字符串是否全由回车，换行，tab组成
isalpha（）方法，字符串是否全字母
issdecimal（）方法，字符串是否全由十进制数组成
isnumeric（）方法，字符串是否全数字
isalnum（）方法，字符串是否全由数字和字母组成
'''

s='hello,python'
print('1.',s.isidentifier())  # False,有逗号，不是纯字母数字下划线
print('2.','hello'.isidentifier())  # hello就是合法的标识符
print('3.','张三_'.isidentifier())
print('4.','张三_123'.isidentifier())

print('5.','\t'.isspace())
print('6.','abc'.isalpha())
print('7.','张三'.isalpha())              # 中文文字也是字母
print('8.','张三1'.isalpha())

print('9.','123'.isdecimal())
print('10.','123四'.isdecimal())          # 中文的数字，不是十进制数字

print('11.','123'.isnumeric())
print('12.','123四'.isnumeric())

print('13.','abc1'.isalnum())
print('14.','张三abc1'.isalnum())
print('15.','abc  1'.isalnum())
