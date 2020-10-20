## Python语法入门之并发编程

### 一、操作系统发展史

参考文档:https://www.cnblogs.com/Dominic-Ji/p/11093137.html

### 二、多道技术

单核实现并发效果

#### 必备知识点

* 并发：

  * 看起来像是同时运行的就可以称之为并
  
* 并行：
  * 真正意义上的同时执行

  ps：并行属于并发嘛？

  ​		并行肯定就是并发

  ​		单核计算机肯定不能实现并行，但是可以实现并发

  ​		补充：我们直接假设单核就是一个核，干活的就是一个人，不需要考虑cpu里面的内核数

#### 多道技术重点知识

空间上的复用与时间上的复用

* 空间上的复用

  * 多个程序共用一套计算机硬件

* 时间上的复用

  * 例子：洗衣服30s、做饭50s、烧水30s

  单道需要110s，多道只需要任务最长的一个                      切换节省时间

  * 例子：边吃饭边玩游戏													保存状态

切换 + 保存状态

```python
"""
切换CPU分为两种情况：
1、当一个程序遇到IO操作的时候，操作系统会剥夺改程序的CPU执行权限
	作用：提高了CPU的利用率，并且也不影响程序的执行效率

2、当一个程序长时间占用CPU的时候，操作系统也会剥夺改程序的CPU执行权限
	作用：降低了程序的执行效率(原本时间 + 切换时间)

"""
```



### 三、进程理论

#### 必备知识点

```python 
"""
程序就是一堆躺在硬盘上的代码，是死的
进程则表示程序正在执行的过程，是活的
"""
```



#### 进程的调度

* 先来先服务调度算法

  * ```python
    """
    对长作业有利，对短作业无益
    """
    ```

* 短作业优先调度算法

  * ```python
    """
    对短作业有利，对长作业无益
    """
    ```

* 时间片轮转法 + 多级反馈队列

![image-20201019101942075](C:\Users\mingyu.ding\AppData\Roaming\Typora\typora-user-images\image-20201019101942075.png)



* 进程三状态图

![image-20201019102540526](C:\Users\mingyu.ding\AppData\Roaming\Typora\typora-user-images\image-20201019102540526.png)



![image-20201019102850368](C:\Users\mingyu.ding\AppData\Roaming\Typora\typora-user-images\image-20201019102850368.png)

```python
# 就绪态：一切程序必须要先过就绪态才能加入运行态
# 运行态：正在被cpu执行
# 阻塞态：程序遇到io操作了
# 理想：我们希望开发的程序一直处于就绪态与运行态之间
```

#### 两个重要的概念
* 同步和异步
```python
"""描述的是任务的提交方式"""

# 同步：任务提交之后，原地等待任务的返回结果，等待的过程中不做任何事情
#      在程序层面上表现出来的感觉就是卡住了


# 异步：任务提交之后，不原地等待任务的返回结果，直接去做其他事情
#      我提交的任务结果如何获取？
#      任务的返回结果会有一个异步回调机制自动处理

```

* 阻塞非阻塞
```python

""" 描述程序的运行状态"""

# 阻塞：阻塞态
# 非阻塞：就绪态、运行态

# 理想状态：我们因该让我们写的代码永远处于就绪态和运行态之间切换
```

上述概念的组合：最高效的一种组合就是`异步非阻塞`

#### 开启进程的两种方式
注意：代码开启进程和线程的方式，代码书写基本是一样的，学会了如何开启进程就学会了如何开启线程

```python
from multiprocessing import Process
import time


def task(name):
    print(f'{name} is running')
    time.sleep(3)
    print(f'{name} is over')


if __name__ == '__main__':
    """
    注意：
    1、windows操作系统下，创建进程一定要在main内创建
    因为windows创建进程类似于模块导入的形式
    会从上往下依次执行代码
    2、linux中，则是将代码完整的拷贝一份
    """
    # 1 创建一个对象
    p = Process(target=task,args=("jason",))
    # 容器类型无论里面有几个元素，一定要用逗号隔开，哪怕只有一个元素
    # 2 开启进程
    p.start() # 告诉操作系统帮你创建一个进程
    print("主")

# 第二种方式：类的继承

from multiprocessing import Process
import time
class MyProcess(Process):
    def run(self):
        print("hello bf girl")
        time.sleep(3)
        print("get out!")
        
if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print("主")
```

##### 总结
```python
# 创建进程就是在内存中申请一块内存空间将需要运行的代码丢进去
# 一个进程对应在内存中就是一个独立的内存空间
# 多个进程对应在内存中就是多块独立的内存空间
# 进程与进程之间数据默认情况下是无法直接交互的，如果想要实现交互则需要第三方模块或工具
```
#### join方法
join方法是让主进程的代码等待子进程
```python
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
```
#### 进程之间数据相互隔离
```python
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
```

ps：人工只能相关参考资料
科大讯飞、百度api、图灵机器人


#### 进程对象及其他方法
ps:pycharm注册码获取地址：http://idea.medeming.com/jets/

```python
# 一台计算机上面运行很多进程，那么计算机是如何区分并故哪里这些进程服务端呢？
#    计算机会给每一个运行的进程分配一个PID号
# 如何查看：
#   windows电脑，加入cmd输入tasklist可以查看
#       tasklist |findstr pid查看具体的进程
#   linux电脑，终端输入ps aux
#       ps aux|grep PID查看具体的进程
```



#### 互斥锁

问题：针对多个进程操作同一份数据的时候，会出现数据错乱的问题

解决：针对上述问题，解决方式就是加锁处理，**将并发编程串行，牺牲效率但是保证了数据的安全**

```python
# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/10/20 9:35
import time
from multiprocessing import Process, Lock
import json
import random


# 查票
def search(i):
    # 文件操作读取票数
    with open("data", "r", encoding="utf8") as f:
        dic = json.load(f)
    print(f'用户{i}查询余票：{dic.get("ticket_num")}')
    # 字典取值不要用【】的形式，推荐使用get


# 买票 1、先查询  2、在买票
def buy(i):
    # 先查票
    with open("data", "r", encoding="utf8") as f:
        dic = json.load(f)

    # 模拟网络延迟
    time.sleep(random.randint(1, 3))
    # 判断当前是否有票
    if dic.get("ticket_num") > 0:
        # 修改数据库  买票
        dic["ticket_num"] -= 1
        # 写入数据库
        with open("data", "w", encoding="utf8") as f:
            json.dump(dic, f)
        print(f'用户{i}买票成功')
    else:
        print(f'用户{i}买票失败')


# 整合上面两个函数
def run(i, mutex):
    search(i)
    # 给买票环节加锁处理
    # 抢锁
    mutex.acquire()
    buy(i)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    # 在主进程中生成一把锁，让所有的子进程抢，谁先抢到谁先买票
    mutex = Lock()
    for i in range(1, 10):
        p = Process(target=run, args=(i, mutex))
        p.start()
"""
扩展：行锁  表锁
注意：
	1、锁不要轻易的使用，容易造成死锁现象
	2、锁只在处理数据的部分加，来保证数据安全；只在争抢数据的部分加锁

"""
```








