from multiprocessing import Process,Queue
"""
研究思路：
    1、主进程和子进程之间通信
    2、子进程和子进程之间通信

"""


def producer(q):
    q.put("我是29技师")
    # print("hello big baby~")

def consumer(g):
    print(q.get())



if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=(q,))
    p1 = Process(target=consumer,args=(q,))
    p.start()
    p1.start()
    # print(q.get())