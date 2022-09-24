# 学习时间：2022/9/13 14:05
# 内容：嵌套if
""""
会员      大于等于200，八折
         大于等于100，九折
非会员    大于等于200,9.5折
         不打折
"""
answer=input('您是会员吗？y/n')
money=float(input('请输入您的购物金额：'))
if answer=='y':
    if money>=200:
        print('打八折，付款金额为：',money*0.8)
    elif money>=100:
        print('打九折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else:
    if money>=200:
        print('打九五折，付款金额为：',money*0.95)
    else:
        print('不打折。付款金额为：',money)