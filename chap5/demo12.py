# 学习时间：2022/9/13 16:33
# 嵌套循环
'''输出一个三行四列的矩形'''
for i in range(3):
    for j in range(4):
        print('*',end='\t')    # end='\t'代表不换行输出
    print()                    # 空的print函数就代表换行