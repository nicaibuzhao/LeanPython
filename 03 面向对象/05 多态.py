#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/13 9:30

# 1 什么是多态：同一事物有多种形态

# class Animal:
#     pass
#
# class People(Animal):
#     pass
#
# class Dog(Animal):
#     pass
#
# class Pig(Animal):
#     pass


# 2 为什么要有多态：
#   多态性指的是可以不用考虑对象具体类型的情况下而直接使用对象

class Animal:
    def say(self):
        print('d动物的基本叫声~~~',end=' ')

class People(Animal):
    def say(self):
        super().say()
        print('People')

class Dog(Animal):
    def say(self):
        super().say()
        print('Dog')

class Pig(Animal):
    def say(self):
        super().say()
        print('Pig')

obj1 = People()
obj2 = Dog()
obj3 = Pig()

obj1.say()
obj2.say()
obj3.say()

# 定义统一的接口，接受传入的对象
def animal_say(animal):
    animal.say()

animal_say(obj3)
animal_say(obj2)
animal_say(obj2)
animal_say(obj2)
animal_say(obj1)
