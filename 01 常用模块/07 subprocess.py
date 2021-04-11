#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/29 15:28

import subprocess

obj = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

res = obj.stdout.read().decode("gbk")
print(res)
err_res = obj.stderr.read()
print(err_res)