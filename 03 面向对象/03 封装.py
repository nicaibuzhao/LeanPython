#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/10 15:51




# 二、将封装的属性进行隐藏操作
# 1、 如何隐藏：在属性名前面加上__前缀，就会实现一个对外隐藏属性效果


# 2、为什么要隐藏？
# class Foo:
#     __x =1
#     def __f1(self):
#         print('from test')


# property 是一个装饰器，是用来将绑定给对象的方法，伪装成一个数据属性
class People():
    def __init__(self,name,height,weight):
        self.__name=name
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        x = 1
        return self.weight / (self.height ** 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @name.deleter
    def name(self):
        pass

obj1 = People("alex",1.83,70)
print(obj1.bmi)













