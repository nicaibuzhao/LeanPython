import queue
from multiprocessing import Queue

# 创建一个队列
q = Queue(5) # 括号内可以传数字，标识生成的队列最大可以同时存放的数据量
# 当队列数据放满之后，如果还有数据要方程序会阻塞，直到位置让出来
# 队列中存数据
q.put(11111)
q.full() # 判断当前队列是否满了
q.empty() #判断当前队列是否空
"""
存取数据  存的目的是为了取
千方百计的存，简单快捷的取
"""
# 队列中取数据
v1 = q.get() # 队列中如果已经没有数据的化，get方法会原地阻塞
v2 = q.get_nowait()# 没有数据之后，直接报错
v3 = q.get(timeout=3) # 没有数据之后，等待3秒 报错
print(v1)

"""
q.full()
q.empty()
q.get_nowait()
在多进程情况下是不精确的

"""




