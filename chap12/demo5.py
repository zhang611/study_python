# 学习时间：2022/9/19 18:08
# 动态绑定属性和方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def eat(self):
        print(self.name + "在吃饭")

stu1 = Student('张三',20)
stu2 = Student('李四',30)


# 动态绑定属性和方法，直接添加就行，只是给一个对象添加了，其他对象没有
# 说的好像很高大上，实际上就那么回事，没有那么难的
# 为stu2动态绑定性别属性
stu2.gender = '女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

# 动态绑定方法
stu1.eat()
stu2.eat()

def show():
    print("定义在类之外的，称为函数")  # 把这个函数绑定在对象上
stu1.show = show()                # 就这样写就可以了，python很简单
stu1.show