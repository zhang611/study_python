# 学习时间：2022/9/12 9:56
# 内容python中的标识符和保留字
# python中一切皆对象，包括文件名，都不可以用保留字

# 标识符：变量（名），函数，类，模块和其他对象起的名字叫标识符
# 1.字母数字下划线组成
# 2.不能以数字开头
# 3.不能是保留字
# 4.区分大小写
# 5.不能含有空格，可以用下划线

import keyword
print(keyword.kwlist)  # 保留字表