#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/10/21 13:23
import time
from multiprocessing import Process
from threading import Thread

# def task(name):
#     print(f"{name}111111111111")
#     time.sleep(1)
#     print("2222222222222")
#
# t = Thread(target=task,args=("alex",))
# t.start()
# print("主")
#
# # 开启线程不需要再main下面执行代码，直接书写即可
# # 但是我们还是习惯性的将启动命令写在main下面
# # if __name__ == '__main__':
# #     pass


from multiprocessing import Process
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name


    def run(self):
        print(f"{self.name}3333333333333")
        time.sleep(1)
        print("sfsfasfafa")

if __name__ == '__main__':
    t = MyThread("alex")
    t.start()
    t.join() # 等待子线程结束之后，主线程才可以执行
    print("主")