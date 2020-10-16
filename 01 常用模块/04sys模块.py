#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/28 15:14
import time
import sys
import time

def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


data_size=333333
recv_size=0
while recv_size < data_size:
    time.sleep(0.01) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024
    percent=recv_size/data_size #接收的比例
    progress(percent,width=70) #进度条的宽度70