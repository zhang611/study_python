# 学习时间：2022/9/13 14:01
# python中的特殊写法
# 和demo4对比看
# python支持下面这种写法
score=int(input('请输入一个成绩：'))
# 判断
if 90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<score<=79:
    print('C级')
elif 60<score<=69:
    print('D级')
elif 0<score<=59:
    print('E级')
else:
    print('成绩不在有效成绩范围内')

