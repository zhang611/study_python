# 学习时间：2022/9/12 15:12
# 内容：布尔运算符，用于布尔值之间
'''
and 一假为假
or  一真为真
not  取反
'''

a,b=1,2
print('------------and--------------')
print(a==1 and b==2)  # True  全真为真
print(a==1 and b<2)   # False 一假为假
print(a!=1 and b==2)  # False 一假为假
print(a!=1 and b!=2)  # False 全假为假

print('-------------or--------------')
print(a==1 or b==2)  # True  全真为真
print(a==1 or b<2)   # True 一真为真
print(a!=1 or b==2)  # True 一真为真
print(a!=1 or b!=2)  # False 全假为假

print('------------not--------------')
f1=True
f2=False
print(not f1)
print(not f2)

# in 和not in表示字符在字符串里是否存在
print('---------in和not in----------')
s='hello_world'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)