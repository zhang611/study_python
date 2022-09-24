# 学习时间：2022/9/12 9:28
# 内容：转义字符
print('hello\nworld')  # \n 代表换行
print('hello\tworld')  # \t 代表到下一个水平制表位，四个空格为一个水平制表位
print('hello\rworld')  # \r 代表回车，只回车不换行，前面的东西都没了
print('hello\bworld')  # \b 代表回退一格，所以o就没有了

print('http:\\www.baidu.com')  # 输出结果只有一个斜线，
print('http:\\\\www.baidu.com')  # 四个\最后输出才是是两个

print('老师说：\'\'大家好\'\'') # 在输出的内容里还要出现引号，就在前面加反斜线

# 原字符：不希望字符串中的转义字符起作用就用原字符,在字符串之前加r或R
# 字符串的最后一个字符不能是反斜线，不然会报错，最后两个是可以
print(r'hello\nworld')
print(r'hello\nworld\\')