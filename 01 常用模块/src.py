#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/9 10:56

# 接下来要做的是：拿到日志的生产者即loggers来生产日志
# 第一个日志生产者：kkk
# 第二个日志生产者：bbb
# 但是需要先导入日志配置字段LOGGER_DIC
# import  setting
# from logging import config,getLogger
# config.dictConfig(setting.LOGGING_DIC)
# logger1 = getLogger("kkk")
#
#
# logger1.info("这是一条info日志")
# logger1.debug("这是一条debug日志")


# 1、日志的命名
#    日志名是区别业务归属的一种非常重要的标识

# 2、日志轮转
#    日志记录着程序运行过程中的关键信息


print(chr(7989))