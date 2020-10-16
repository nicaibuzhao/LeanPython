#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/29 10:43

import configparser

config = configparser.ConfigParser()
config.read("test.ini")

# 获取sections
print(config.sections())

# 获取某一section下的所有options
print(config.options("section1"))

# 获取items
print(config.items("section1"))


# 获取字符串元素
res = config.get("section1","user")
print(res)
# 获取整型元素
res = config.getint("section1","age")
print(res)
# 获取布尔型元素
res = config.getboolean("section1","is_admin")
print(res)
# 获取浮点型元素
res = config.getfloat("section1","salary")
print(res)