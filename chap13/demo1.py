# 学习时间：2022/9/19 18:31
# 封装

class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print("汽车已启动...")

car = Car('宝马x5')
car.start()
print(car.brand)

# 在类的外部使用了类当中封装的属性，方法
