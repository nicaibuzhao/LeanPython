from multiprocessing import Process
money = 100
def task():
    global money # 局部变量修改全局比阿亮
    money = 666
    print("子进程",money)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(money)