# 学习时间：2022/9/14 17:08
# 内容：字典生成式
# 内置函数zip（） 如果个数不相等，会以少的为基准

items=['fruits','books','others']
prices=[98,78,85]

d={item.upper():price   for item,price in zip(items,prices)}  # 这里用到了upper方式
print(d)