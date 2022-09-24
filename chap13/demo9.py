# 学习时间：2022/9/19 20:09
# 两个下划线开始，结束的方法交特殊方法
a = 20
b = 100
c = a + b
d = a.__add__(b)  # 这是a+b的底层算法

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name  # 自己写相加的方法，这就可以加了
    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2  # 本来是不可以相加的，但是我可以自己写方法
print(s)
s = stu1.__add__(stu2)
print(s)

print('-------------------------')
lst = [11,22,33,44]
print(len(lst))   # 这个len是函数，输出列表的长度
print(lst.__len__())  # 这个是用方法输出列表长度
print(len(stu1))  # 本来没有这个函数，要用的话要自己写个方法