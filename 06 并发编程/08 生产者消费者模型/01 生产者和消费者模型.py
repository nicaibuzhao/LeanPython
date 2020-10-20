from multiprocessing import Process,Queue,JoinableQueue
import time
import random

def producer(name,food,q):
    for i in range(5):
        data = f"{name}生产了{food}{i}"
        # 模拟延迟
        time.sleep(random.randint(1,3))
        print(data)
        # 将数据放入队列中
        q.put(data)

def consumer(name,g):
    # 消费者
    while True:
        food = q.get() # 没有数据就会卡住
        # 判断当前是否有结束标识
        # if food is None:
        #     break
        time.sleep(random.randint(1,3))
        print(f"{name}吃了{food}")
        q.task_done()# 告诉队列你已经从里面取了数据并处理


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer,args=("egon","包子",q))
    p2 = Process(target=producer,args=("tank","粥",q))
    c1 = Process(target=consumer,args=("chunge",q))
    c2 = Process(target=consumer,args=("xinge",q))

    p1.start()
    p2.start()

    # 将消费者设置成守护进程
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    # 等待生产者生产完毕自后，往队列中添加特定的结束符号
    # q.put(None) # 肯定在所有生产者，生产数据的末尾
    q.join() # 等待队列中所有的数据被取完在执行往下的代码
    """
    JoinableQueue 每当你往该队列中存入数据的时候，内部会又一个计数器
    +1；每当你调用task_done的时候，计数器-1
    q.join() 当计数器为0的时候才会往下执行
    """
    # 只要q.join()执行完毕，说明消费者已经处理完数据了，消费者就没有存在的必要了








