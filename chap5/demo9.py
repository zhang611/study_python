# 学习时间：2022/9/13 16:13
# continue语句，用于结束当前循环，进入下一轮循环，常与if一起使用
'''要求输出1到50之间所有5的倍数，使用continue'''
'''
for item in range(1,51):
    if item%5==0:
        print(item)
这个方法很好，但是不符合要求，没有用到continue
'''
for item in range(1,51):
    if item%5:
        continue
    else:
        print(item)