# import string
# 整数
# python中的整数包含正整数、负整数写法上一模一样
# python的整数理论上没有上限和下限

int = 1, 100, -8080, 0

# 以上都是整数  (1, 100, -8080, 0)
print(int)

# 十六进制数
int_16 = 0xff00, 0xa5b4c3d2

# 以上为16进制的整数 (65280, 2780087250)
print(int_16)

# 浮点型

float = 1.23, 3.14, -9.01
# 以上都是浮点数 (1.23, 3.14, -9.01)
print(float)

# 我们可以用e代替10 如 1.23*10 的 9 次方 等同于 1.23e9 或者 12.3e8

print(1.23 * pow(10, 9), 1.23e9, 12.3e8)

print(1.23 * pow(10, 9) == 1.23e9)
print(1.23 * pow(10, 9) == 12.3e8)
print(1.23e9 == 12.3e8)
# True True True

# 1230000000.0 1230000000.0 1230000000.0

# 用转义符号"\"可以将 ' " 等不能直接包含在字符串中的符号转义成普通的符号
print('I\'m \"Ok\"')
# I'm "Ok"

# \r 换行 \t 制表符 \\ 表示原样输出\ 而且\运算符是从左向右的
# ''内的字符串会被转义  r'' 内的字符串不会被转义，会原样输出，但是不能换行。
print('\\\t\\')
# \       \
print(r'\\\t\\')
# \\\t\\

# ''' ''' 里的内容允许换行并能原样输出

print('''
first line
second line
third line
''')

# first line
# second line
# third line

# boolean 类型 True T是大写的 False F是大写的
print("----------------------boolean----------------------")
print(True)
print(False)
print(3 > 2)
print(3 > 5)

print("----------------------and---------------------------")
# boolean 类型支持逻辑运算 and、or和not 运算
# and 运算
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(5 > 3 and 3 > 1)  # True

print("----------------------or----------------------------")
# or 运算

print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(5 > 3 or 1 > 3)  # True

print("----------------------not---------------------------")
# not 运算

print(not True)  # False
print(not False)  # True
print(not 1 > 2)  # True

# boolean 值常用于做判断
age = input("Please input your age :")
print(type(age))
# checkAge(string.atoi(age))

print("----------------------if---------------------------")


# if 运算
def checkAge(age):
    if age >= 18:
        print('adult')
    else:
        print('teenager')


checkAge(18)

# python中的常量已全大写的字母表示 PI

print("---------------------常量---------------------------")
PI = 3.14159265359
print("---------------------字符串赋值---------------------")
a = "ABC"
b = a
a = "XYZ"
print(a, b)

# 在python 中/ 除法的结果是浮点数，即使两个整数恰好整除，结果也是浮点数

print(10 / 3)  # 3.3333333333333335 python依旧有所有计算机系统共同的问题，就是除法无法得到准确的结果

print(9 / 3) #3.0

# python 中有一种除法 整除 // ,两个数除完一定是整数：

print(10 // 3) # 3

# % 取余数预算 结果是整数：

print(10 % 3) # 1 取余数预算

