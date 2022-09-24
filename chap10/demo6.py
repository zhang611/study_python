# 学习时间：2022/9/16 15:23
# 个数可变的参数
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)     # 这个是最基本的位置传参

print('-------------------------------')

lst = [11,22,33]
# fun(lst)  这样会报错，只有一个参数TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst)   # 这样就不会报错了

print('-------------------------------')

fun(a=100,c=600,b=500)
print('-------------------------------')
dic={'a':111,'b':222,'c':333}
# fun(dic) 这也是会报错
fun(**dic)