# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/22 9:54


def deco1(func1):  # func1 = wrapper2的内存地址
    def wraaper1(*args, **kwargs):
        print("正在运行====》deco1.wrapper1")
        res1 = func1(*args, **kwargs)
        return res1

    return wraaper1


def deco2(func2):  # func2 = wrapper3的内存地址
    def wraaper2(*args, **kwargs):
        print("正在运行====》deco2.wrapper2")
        res2 = func2(*args, **kwargs)
        return res2

    return wraaper2


def deco3(x):
    def outter3(func3):  # func3 = 被装饰对象原函数的(index函数)的内存地址
        def wraaper3(*args, **kwargs):
            print("正在运行====》deco3.outter3.wrapper3")
            res3 = func3(*args, **kwargs)
            return res3

        return wraaper3

    return outter3


# 加载顺序是自下而上的
@deco1  # index = deco1(wrapper2的内存地址)  ===>  index = wrapper1的内存地址
@deco2  # index = deco2(wrapper3的内存地址)  ===》 index = wrapper2的内存地址
@deco3(1111)  # ===》@outter3 ====》index = outter3(index) ===》index= wrapper3的内存地址
def index(x, y):
    print("from index %s:%s" % (x, y))


# 执行顺序自上而下
index(1, 2)  # wraaper1(1,2)
