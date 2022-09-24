# 学习时间：2022/9/19 19:32
# 方法重写
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
    def info(self):      # 重写父类中的方法，注意左边的○
        super().info()  # 在子类中调用父类的方法，用super（）就可以
        print('学号',self.stu_no)


class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
    def info(self):             # 这也是重写父类中的info
        super().info()
        print('教龄',self.teachofyear)


stu = Student('张三',20,'1001')
teacher = Teacher('李四',34,10)

stu.info()
print('------------------')
teacher.info()