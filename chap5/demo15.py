# 学习时间：2022/9/13 16:58
# 内容：二重循环中的break和continue
# 用于控制本层循环

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()