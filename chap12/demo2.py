# 学习时间：2022/9/19 17:39
# 类的使用
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
