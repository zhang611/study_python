# 学习时间：2022/9/15 18:45
# 内容：格式化字符串的宽度和精度
# 百分号形式表示
print('%d' % 99)
print('%10d' % 99)     # 中间的10代表宽度
print('hellohello')

print('%f' % 3.1415926)
print('%.3f' % 3.1415926)   # 中间的.3代表精度

print('%10.3f' % 3.1415926)  # 同时表示宽度和精度

# 花括号表示
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))   # 使用冒号点3的形式，这个3表示一共三位数
print('{0:.3f}'.format(3.1415926))   # 加个f表示三位小数
print('{0:10.3f}'.format(3.1415926))  # 10表示宽度为10位