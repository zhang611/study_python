# 学习时间：2022/9/19 19:57
# 特殊属性，特殊方法

print(dir(object))  # dir这个函数可以查看类的所有属性和方法
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 创建C类的对象
x = C('Jack',20)  # x是C类型的一个实例对象
print(x.__dict__)  # 这个特殊方法可以查看实例对象的属性字典
print(C.__dict__)  # 这个特殊方法也可以看类对象的方法和属性的字典
print('--------------------')
print(x.__class__)  # 这个方法可以输出对象所属的类型
print(C.__bases__)   # 这个方法可以输出其父类的元组
print(C.__base__)    # 输出距离最近的父类
print(C.__mro__)     # 查看类的层次结构
print(A.__subclasses__())  # 查看A的子类列表