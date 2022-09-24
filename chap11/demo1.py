# 学习时间：2022/9/16 17:00
# 异常处理机制：try except语句
# 程序可能会出错的时候用这种方法

try:
    a=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    c=a/b
    print('结果为',c)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')