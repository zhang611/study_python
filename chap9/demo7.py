# 学习时间：2022/9/15 17:47
# 内容：字符串的操作，替换，合并

# replace（）方法
s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))  # 第三个参数表示换几次

#  join（）方法
# 将列表或者元组中的字符串合并成一个字符串
lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))

print('*'.join('python'))
print('*'.join(t))