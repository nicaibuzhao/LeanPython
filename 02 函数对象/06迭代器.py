#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/21 9:29

"""
1、什么是迭代器
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，单纯的重复不是跌打

2、为什么要迭代
    迭代器是用来迭代取值的工具，而涉及到把多个值循环去来的类型有：
    列表、字符串、元组、字典、集合、文件

    l = [1,3,4,5,0]
    i = 0
    while i < len(l):
        print(l[i])
        i ++=1

    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
    为了解决基于索引迭代取值的局限性
    python必须提供一种能够不依赖于索引的取值方式，这就是迭代器


3、如何用迭代器


"""
# 可迭代对象：但凡内置有__iter__方法的都称之为可迭代的对象


# 调用可迭代对象下的__iter__方法会将其转换成迭代器对象
# d = {"a":1,"b":2,"c":3}
# d_iterator = d.__iter__()
# print(d_iterator)

# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__())
# print(d_iterator.__next__()) # 抛出异常 StopIteration

# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break
#
#
# print("==================") # 在一个迭代器取值，取干净的情况下再次取值，就取不到
# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break


# 3、可迭代对象与迭代器对象详解
# 3.1 可迭代对象("可以转化成迭代器的对象")：内置有__iter__方法对象
# 3.2 迭代器对象：内置有__next__方法且内置有__iter__方法的对象
#           迭代器对象.__next__():得到迭代器的下一个值
#           迭代器对象.__iter__:得到迭代器的本身，调了跟没调一样
d = {"a":1,"b":2,"c":3}
d_iterator = d.__iter__()

# for 循环的工作原理

# 1、d.__iter__()得到一个迭代器对象
# 2、迭代器对象.__next__() 拿到一个返回值，然后将该返回值赋值给k
# 3、循环往复步骤2，直到跑抛出StopIteration异常，for循环会捕捉异常然后结束循环
for k in d:
    print(k)





