# 学习时间：2022/9/13 16:44
# 嵌套循环
# 打印一个直角三角形，9行的
for i in range(1,10):
    # for j in range(1,i):       # 这里不能这样写，这样写i最大是9，这时j只有8，打不了9行
    for j in range(i) :
         print('*',end='\t')
    print()

