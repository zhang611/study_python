# 学习时间：2022/9/19 18:35
# 类中的属性不希望别人使用就在前面加两个下划线

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age   # 年龄比向外在类的外部被使用，所以加__，可以在内部使用，君子协议
    def show(self):
        print(self.name,self.__age)

stu = Student('张三',20)
stu.show()
# 在类的外部使用name和age
print(stu.name)
# print(stu.__age)  # 'Student' object has no attribute '__age'  报错说没有这样的属性

# 不希望被使用，但是是可以使用的
print(dir(stu))  # 先从这个列表中找到age的名字
print(stu._Student__age)  # 再使用这个名字得到age的值
# 君子协议，python留的后门，防君子不防小人