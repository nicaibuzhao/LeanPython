#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/10/22 9:41

from threading import Thread,active_count,current_thread
import time
import os

def task():
    # print("hello world",os.getpid())
    print("hello world",current_thread().name) # 获取线程名字
    time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    t.join()
    # print("主",os.getpid())
    print("主",active_count()) # 统计当前正在活跃的线程数