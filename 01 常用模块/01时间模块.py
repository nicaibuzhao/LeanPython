#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/28 13:35


import time
# # 一、time
# # 1、时间戳：从1970年到现在经过秒数
# #   作用：用于时间间隔的计算
# print(time.time())
#
# # 2、按照某种格式显示的时间：2020-09-28 11:11:11
# #   作用：用于展示时间
# print(time.strftime("%Y-%m-%d %H-%M-%S"))
#
# # 3、结构化时间
# #   作用：用于单独获取时间某一部分
# res = time.localtime()
# print(res)
#
# # 二、datatime
import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=3)) # 3天后
# print(datetime.datetime.now() + datetime.timedelta(days = -3)) # 3天前
# print(datetime.datetime.now() + datetime.timedelta(weeks = 3)) # 3周后
# print(datetime.datetime.now() + datetime.timedelta(weeks = -3)) # 3周前

# 时间模块需要掌握的操作
# 1、时间格式的转换
# struct_time ===>时间戳 用于计算
# s_time = time.localtime()
# res = time.mktime(s_time)
# print(res)
#
# # 时间戳 ====》struct_time
# tp_time = time.time()
# print(time.localtime(tp_time))

# print(time.localtime()) # 北京时间
# print(time.gmtime()) # 格林尼治天文台时间

# struct_time ---> 格式化的字符串时间格式
# s_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", s_time))

# 重点-------------------------------------
# format string ----> timestamp

# format string ----> struct_time -----> timestamp
srtuct_time = time.strptime("2020-09-28 14:05:09","%Y-%m-%d %X")
timestamp = time.mktime(srtuct_time) + 7*89400
print(timestamp)

# format string <----- struct_time <----- timestamp
res = time.strftime("%Y-%m-%d %X",time.localtime(timestamp))
print(res)