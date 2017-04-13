# -*- coding: utf-8 -*-

# tuple 是另一种有序列表叫元祖：tuple。tuple 和list 非常类似，但是tuple 一旦初始化就不能修改。
# tuple 可以使用 classmates[0],classmates[-1] .
# 但是不能用 append(),insert() 这两个方法

classmates = ("lp", "lg", "bb")
print(classmates)  # ('lp', 'lg', 'bb')

# 可以直接用()就可以生成一个元祖 tuple
t = ()
print(t)  # ()

# 如果要定义只有一个元素的元祖 1
t = (1)
print(t)  # 1 只是普通的元素1

# 如果想用1个元素的元祖
t = (1,)
print(t)  # (1,) 这样做可以避免被误认为括号（1）

t = ('a', 'b', ['A', 'B'])
print(t)  # ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # ('a', 'b', ['X', 'Y'])
