# -*- coding: utf-8 -*-
# python 的字符串

print("包含中文的str")

# python 提供了ord() 函数取字符串的整数表示：

print(ord('A'))  # 65

# 同时提供了chr() 函数将整数转换成对应的字符：

print(chr(66))  # B

print(chr(25991))  # 文

print('\u4e2d\u6587')  # 中文

print('ABC')  # ABC 字符串
print(b'ABC')  # bytes 字节

# print(b'奥古斯丁') 中文是无法用bytes 直接表示的

# python 中 str 通过encode() 方法编码为指定的bytes
print('ABC'.encode('ascii'))  # b'ABC'

print('ABC'.encode('utf-8'))  # b'ABC'

# print('朱里斯'.encode('ascii'))  中文字符无法编码为bytes UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)

print('菲勃卢姆'.encode('utf-8'))  # b'\xe8\x8f\xb2\xe5\x8b\x83\xe5\x8d\xa2\xe5\xa7\x86'

print('"雅努斯" 的长度：', len('雅努斯'))  # 3

print('"ABC" 的长度：', len('ABC'))  # 3

# python 使用% 格式化 和C语言是一致的，用%实现
print("ABC,%s" % 'asdasda')

# python 的占位符
# %d  整数
# %f  浮点型
# %s  字符串
# %x  十六进制整数

# 格式化整数和浮点数还可以指定是否补0 和整数与小数的位数：

print('%2d-%02d' % (3, 1))

print('%d' % (222222222))

print('-%02d' % (1))

print('%02d' % (1))

# 直接写数字的话数字前面会补空格，如果以0开头的话会在数字前面补0
print('%12d' % (1))  # 1
print('%012d' % (1))  # 000000000001

# 中文也可以被编码成gb2312格式
print('中文'.encode('gb2312')) #b'\xd6\xd0\xce\xc4'

# python 的% 用%%表示
print('growth rate: %d %%' % (7))

# python中 %s 是永远起作用的

print('Age:%s,Gender:%s' % (25, True)) #Age:25,Gender:True
