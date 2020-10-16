# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/17 17:28

# 装饰器
"""
1、什么是装饰器
    器指的是工具，可以定义成函数
    装饰指的是为其他事物添加额外的东西点缀

    装饰器指的是定义一个函数，该函数是用来为其他函数添加额外的功能


2、为什么要用装饰器
    开放封闭原则：
        开放：指的是对拓展功能的开放的
        封闭：指的是对修改源代码是封闭的

    装饰器就是在不修改被装饰对象源代码以及调用方式的前提下为被装饰对象添加新功能


3、如何使用


"""
import time


# 需求：在不修改index函数的源代码以及代用方式的前提下为其添加统计运行时间的功能
# 方案一：
# 问题：没有修改被装饰对象的调用方式，但是修改了其源代码
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print("index %s %s" % (x, y))
#     stop = time.time()
#     print(stop - start)
#
# index(111, 222)


# 方式二：
# 问题：没有改变被装饰对象的源代码，但是该变了其调用方式
# def index(x, y):
#     time.sleep(3)
#     print("index %s %s" % (x, y))
# def wrapper():
#     start = time.time()
#     index(111, 222)
#     stop = time.time()
#     print(stop - start)
# wrapper()

# 方式三：
# 如何在方式二的基础上不改变函数的调用方式
# def index(x, y):
#     time.sleep(3)
#     print("index %s %s" % (x, y))
# def wrapper():
#     start = time.time()
#     index(111, 222)
#     stop = time.time()
#     print(stop - start)
# wrapper()


# 方式三的优化：1、将index的参数写活
# import time
# def index(x,y,z):
#     time.sleep(3)
#     print("index %s %s %s"%(x,y,z))
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     index(*args,**kwargs)
#     stop = time.time()
#     print(stop - start)
#
# wrapper(2222,3333,44444)


# 方式三的优化：2、在优化1的基础上把被装饰对象写活，原来只能装饰index
# def index(x, y, z):
#     time.sleep(3)
#     print("index %s %s %s" % (x, y, z))
#
# def outter(func):
        # func = index的内存地址
#     def wrapper(*args, **kwargs): # *args, **kwargs 接收多个参数
#         start = time.time()
#         func(*args, **kwargs) # index 内存地址
#         stop = time.time()
#         print(stop - start)
#     return wrapper
#
#
# f = outter(index)  # f = outter(index 内存地址)
# f(111,222,333)

# 方式三的优化：3、将wrapper做的跟被装饰函数一模一样
# 语法糖：可以让人开心的语法
# 在被装饰对象正上方的单独一行写@装饰器名称



# def outter(func):
#     # func = index的内存地址
#     def wrapper(*args, **kwargs):  # *args, **kwargs 接收多个参数
#         start = time.time()
#         res = func(*args, **kwargs)  # index 内存地址
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
#
#
# @outter
# def index(x,y,z):
#     time.sleep(3)
#     print("index %s %s %s" % (x,y,z))
# @outter
# def home(name):
#     time.sleep(3)
#     print("welcome %s to home page" % name)
#     return 123
#
#
# def outter(func):
#         # func = index的内存地址
#     def wrapper(*args, **kwargs): # *args, **kwargs 接收多个参数
#         start = time.time()
#         res = func(*args, **kwargs) # index 内存地址
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
#
#
# home("alex")
# index(1,2,3)

# 总结:无参装饰器模板
# def outter(func):
#     def wrapper(*args, **kwargs):
#         # 1、调用原函数
#         # 2、为其增新功能
#         res = func(*args, **kwargs)
#         return res
#     return wrapper

def auth(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增新功能
        name = input("your name>>>: ").strip()
        password = input("your password>>>: ").strip()
        if name == "alex" and password == "123":
            res = func(*args, **kwargs)
            return res
        else:
            print("账号密码错误")
    return wrapper


@auth
def index():
    print("from index")

index()