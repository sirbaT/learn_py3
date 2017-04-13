# -*- coding: utf-8 -*-
# python中的list，list 是一种有序的集合，可以随时添加和删除其他的元素
# list 是先进后出的 （栈）
classmates = ['赛车', '选美', '艺术']

print(classmates)  # ['赛车', '选美', '艺术']

print(len(classmates))  # 3

print(classmates[0])  # 赛车
print(classmates[1])  # 选美
print(classmates[2])  # 艺术

print(classmates[-1])  # 艺术

# list 是一个有序的表，所以追加的元素都是追加到末尾的 append()
classmates.append('Adam')

print(classmates)# ['赛车', '选美', '艺术', 'Adam']

# insert 把元素插入到指定的位置，第一个参数为位置
classmates.insert(1, 'Jack')
print(classmates)#['赛车', 'Jack', '选美', '艺术', 'Adam']



