# 学习时间：2022/9/12 14:45
# 内容：赋值运算符
# 执行顺序从右往左
i=3+4
print(i)

# 链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
# 从这理解一下，什么是变量，变量就是一个标志，不要理解成盒子

# 参数赋值
a=20
a+=30   # 这种写法相当于a=a+30,其他符号一样，没什么好说的
print(a)

# 系列解包赋值
a,b,c=20,30,40
print(a,b,c)
# 好处，交换两个变量的值，python中不用中间变量
a,b=10,20
print('交换之前：','a =',a,'b =',b)
a,b=b,a
print('交换之后：','a =',a,'b =',b)

