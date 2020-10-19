from multiprocessing import Process
import time


def task(name,n):
    print(f'{name} is running')
    time.sleep(n)
    print(f'{name} is over')


if __name__ == '__main__':
    # 1 创建一个对象
    p1 = Process(target=task,args=("jason",1))
    p2 = Process(target=task,args=("egon",2))
    p3 = Process(target=task,args=("tank",3))
    star_time = time.time()
    p1.start() # 告诉操作系统帮你创建一个进程，仅仅是告诉操作系统创建进程
    p2.start()
    p3.start()
    # p.join() # 主进程等待子进程p运行结束之后在继续往后运行
    p1.join()
    p2.join()
    p3.join()
    print("主",time.time())
