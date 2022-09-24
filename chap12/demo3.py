# 学习时间：2022/9/19 17:51
class Student:
    native_pace = "吉林"  # 直接写在类里的对象，称为类属性
    def __init__(self,name,age):  # 初始化方法
        self.name = name          # self.name称为实例属性
        self.age = age

    # 实例方法
    def eat(self):   # 写一个方法
        print("学生在吃饭")

    # 静态方法
    @staticmethod
    def method():  # 静态方法这个括号里面不写self
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print("我是类方法，因为用了classmethod修饰")

# 在类之外定义的叫函数，在类里面定义的叫方法
def drink():
    print("喝水")


# 创建Student类的对象
stu1 = Student('张三',20)

print(id(stu1))     # 实例对象中有一个类指针，指向类对象
print(type(stu1))
print(stu1)   # 这个现实的是内存地址的十六进制表示

print()

print(Student)
print(id(Student))
print(type(Student))

print()

stu1.eat()
print(stu1.name)
print(stu1.age)

print()

Student.eat(stu1)        # 这行代码和42行代码等价stu1.eat()