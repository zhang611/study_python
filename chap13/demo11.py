# 学习时间：2022/9/23 13:29
# 类的赋值和浅拷贝

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

# (1)变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)  # cpu1和cpu2的内存地址相同，是一个对象，放在了两个变量中
print('------------------------')

# （2）类的浅拷贝
disk = Disk()  # 创建一个硬盘类的对象
computer = Computer(cpu1,disk)  # 创建一个计算机类的对象

import copy  # 浅拷贝
computer2 = copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
# computer和computer2是不同的变量地址不同，但是里面的东西是同一个对象，地址一样
print('---------------------------')

# 深拷贝
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
# 不同于浅拷贝里面东西也拷贝了一份，地址也不同了