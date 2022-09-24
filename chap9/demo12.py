# 学习时间：2022/9/15 18:55
# 内容：字符串的编码和转换
s='天涯共此时'
# 编码
print(s.encode(encoding='GBK'))  # GBK一个中文占两个字节
print(s.encode(encoding='UTF-8')) # UTF-8一个中文占三个字节

# 解码
# byte=s.encode(encoding='GBK')
byte=b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'  # 上面和现在这样都是可以的
print(byte.decode(encoding='GBK'))