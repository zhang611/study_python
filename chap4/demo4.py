# 学习时间：2022/9/13 13:46
# 内容：多分支结构，if...elif...elif...else
# 从键盘录入一个整数成绩，判断成绩等级
'''
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
其他成绩为非法数据
'''

score=int(input('请输入一个成绩：'))
# 判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('成绩不在有效成绩范围内')

