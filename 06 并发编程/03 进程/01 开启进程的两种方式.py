# 第一种
# from multiprocessing import Process
# import time
#
#
# def task(name):
#     print(f'{name} is running')
#     time.sleep(3)
#     print(f'{name} is over')
#
#
# if __name__ == '__main__':
#     """
#     注意：
#     1、windows操作系统下，创建进程一定要在main内创建
#     因为windows创建进程类似于模块导入的形式
#     会从上往下依次执行代码
#     2、linux中，则是将代码完整的拷贝一份
#     """
#     # 1 创建一个对象
#     p = Process(target=task,args=("jason",))
#     # 容器类型无论里面有几个元素，一定要用逗号隔开，哪怕只有一个元素
#     # 2 开启进程
#     p.start() # 告诉操作系统帮你创建一个进程
#     print("主")

# 第二种方式：类的继承

from multiprocessing import Process
import time
class MyProcess(Process):
    def run(self):
        print("hello bf girl")
        time.sleep














