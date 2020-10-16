# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/19 15:12

from functools import wraps


# 第一种方式：
# def auth(func, db_type):
#     def wrapper(*args, **kwargs):
#         name = input("your name -->").strip()
#         pwd = input("your password --->").strip()
#
#         if db_type == "file":
#             # 从文件中去账号密码进行验证
#             if name == "alex" and pwd == "123":
#                 print("基于文件的验证")
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print("user or password error")
#         elif db_type == "mysql":
#             print("基于数据库的验证")
#         elif db_type == "ldap":
#             print("基于ldap的验证")
#         else:
#             print("不支持该db_type")
#
#     return wrapper
#
#
# # @auth  # 账号密码来源是文件
# def index(x, y):
#     print("index -->%s %s" % (x, y))
#
#
# # 账号密码来源是mysql
# def home(name):
#     print('home ===>%s' % name)
#
#
# # 账号密码来源是ldap
# def transfer():
#     print("transfer")
#
#
# index = auth(index, "file")
# home = auth(home, "mysql")
# transfer = auth(transfer, "ldap")
#
# home("alex")


# 语法糖


def auth(db_type):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = input("your name -->").strip()
            pwd = input("your password --->").strip()

            if db_type == "file":
                print("基于文件的验证")
                if name == "alex" and pwd == "123":
                    res = func(*args, **kwargs)
                    return res
            elif db_type == "mysql":
                print("基于数据库的验证")
            elif db_type == "ldap":
                print("基于ldap的验证")
            else:
                print("不支持该db_type")

        return wrapper

    return deco


@auth(db_type="file")  # @deco  # index = deco(index) # index = wrapper
def index(x, y):
    print("index -->%s %s" % (x, y))


@auth(db_type="mysql")  # @deco  # home = deco(home) # home = wrapper
def home(name):
    print('home ===>%s' % name)


@auth(db_type="ldap")  # @deco  # transfer = deco(transfer) # transfer = wrapper
def transfer():
    print("transfer")


# index = auth(index, "file")
# home = auth(home, "mysql")
# transfer = auth(transfer, "ldap")
index(1, 2, 3)
home("alex")
transfer()



# 有参装饰器模板：
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args, **kwargs):
            # 1、调用原函数
            # 2、为其增新功能
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outter


@有参装饰器(1,y=2,z=4)
def index(x,y,z):
    print("index %s %s %s" % (x, y, z))










