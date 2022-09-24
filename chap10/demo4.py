# 学习时间：2022/9/16 15:04
# 内容：参数的默认值

def fun(a,b=10):    # 这个b=10就是默认值，要是没有传参，第二个参数就是10，传了就按照传了的算
    print(a,b)

fun(100)
fun(10,20)
# 按住ctrl加上鼠标点击print可以看print函数的源码
print('hello',end='\t')  # print函数的默认值，最后end='\n'是换行，这里直接指定end='\t'显示的结果就不是换行了
print('world')