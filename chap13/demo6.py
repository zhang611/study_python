# 学习时间：2022/9/19 19:39
# str方法本来是输出对象的内存地址，现在修改一下

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):  # 重写object类中的str方法
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)
stu = Student('张三',20)
print(dir(stu))
# 使用dir这个函数查看这个类的所有属性和方法，这里有很多东西但是我们也没定义
# 这些东西都是从父类object哪里继承的

# __str__方法，返回对象的描述
print(stu)
print(type(stu))