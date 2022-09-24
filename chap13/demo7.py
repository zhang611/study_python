# 学习时间：2022/9/19 19:48
# 多态
# 说实话不太明白，学了java再回来看看吧
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:
    def eat(self):
        print('人吃五谷杂粮')

# 定义一个函数
def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())  # 狗和猫是继承动物的，但是重写了动物的eat方式，所以打印自己的
fun(Dog())
fun(Animal())
print('---------------------')
fun(Person())