from multiprocessing import Process, current_process
import time
import os


def task():
    # print(f"{current_process().pid} is running")  # 查看当前进程号
    # print(f"{os.getpid()} is running")  # 查看当前进程号

    time.sleep(3)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate() # 杀死当前进程
    # 是告诉操作系统杀死当前进程，是需要一定的时间，而代码的运行速度极快
    # 所以需要一个时间间隔
    time.sleep(0.1)
    print(p.is_alive()) # 判断当前进程是否存活
    # print("主",os.getpid())
    # print("主主",os.getppid()) # 获取父进程号
