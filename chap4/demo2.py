# 学习时间：2022/9/13 13:32
# 内容：单分支结构，如果...就...
money=1000
s=int(input('请输入取款金额'))
# 判断余额是否充足
if money>=s:
    money-=s
    print('取款成功，余额为：',money)