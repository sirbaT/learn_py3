# this is annotation

print("Hello world!")
print("111", "222", "333")
# name = input()
# print("Hello", name)
a = 200
if a > 0:
    print(a)
else:
    print(-a)
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n, f, s1, s2, s3, s4)

print("包含中文的str")

print(ord('A'))  # 65
print(ord('z'))  # 122

print(chr(66))  # B
print(chr(25991))  # 文

print('\u4e2d\u6587')  # 中文

print(b'zhongwen'.__sizeof__())
print('zhongwen'.__sizeof__())

