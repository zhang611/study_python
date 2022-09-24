# 学习时间：2022/9/12 10:54
# 内容：数据类型转换
'''
print('我叫'+name+'今年'+age+'a岁')
上面那样是不可以的，连接字符串不能有int类型的20，要转成字符串
+是连字符，连接字符串
'''

name='张三'
age=20
print(type(name),type(age))
print('我叫'+name+',今年'+str(age)+'岁') # age本来是int类型，用str函数转化为str类型

'''
str，int，float，bool
四个之间相互转
'''

print('-------------str()将其他类型转化为str类型---------------------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('-------------int()将其他类型转化为int类型---------------------')
s1='128'    # 成功，字符串只有整数数字串可以转
s2='76.77'  # 失败
s3='hello'  # 失败
f1=98.7     # 成功，小数部分直接截掉
b1=True     # 成功，真就是1，假就是0
print(type(s1),type(s2),type(s3),type(f1),type(b1))
print(int(s1),type(int(s1))) # 成功
# print(int(s2),type(int(s2))) 失败
# print(int(s3),type(int(s3))) 失败
print(int(f1),type(int(f1))) # 成功
print(int(b1),type(int(b1))) # 成功

print('-----------float()将其他类型转化为float类型-------------------')
s1='128.98'  # 成功，数字串可以转
s2='76'      # 成功，后面加个点零变成浮点型
s3='hello'   # 失败，只有数字串可以转
ff=True      # 成功，加个点零
i=98         # 成功，加个点零
print(type(s1),type(s2),type(s3),type(ff),type(i))
print(float(s1),type(float(s1)))  # 成功
print(float(s2),type(float(s2)))  # 成功
# print(float(s3),type(float(s3)))  失败
print(float(ff),type(float(ff)))  # 成功
print(float(i),type(float(i)))    # 成功