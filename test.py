#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/12/7 11:26
import random
food = [33,'麻辣烫','鱼粉','板面','黄焖鸡','炒面','重庆小面','释面','兰州拉面','米线',]

while True:
    res = input("请输入‘今天中午吃啥’： ")
    if res == '今天中午吃啥' or res == '':
        print(food[random.randint(0, 9)])
        break
    else:
        print("中午吃啥都不知道，啥也不是~~")