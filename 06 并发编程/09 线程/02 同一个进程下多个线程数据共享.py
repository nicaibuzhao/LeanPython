#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/10/22 9:39

from threading import Thread
import time

money = 100
def task():
    global money
    money = 55

if __name__ == '__main__':
    t = Thread(target=task,)
    t.start()
    t.join()
    print(money)