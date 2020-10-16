# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/15 20:21

# 精髓：可以把函数当成变量去用
# func=内存地址
def func():
    print("from func")


# 1、可以赋值
# f = func
# print(f,func())
# f()

# 2、可以当操作函数的参数传入
# def foo(x): # x = func的内存地址
#     # print(x)
#     x()
# foo(func) # foo(func的内存地址)

# 3、函数可以作为参数传入另外一个函数
# def foo(x): # x = func的内存地址
#     return x
# res = foo(func)  # foo(func的内存地址)
# print(res)
# res()

# 4、可以当做容器类型的一个元素
l = [func]


# print(l)
# l[0]()

# dict = {"k1":func}
# dict["k1"]()


def login():
    print("登录功能")


def transfer():
    print("转账功能")


def check_banlance():
    print("查询余额")


def withdraw():
    print("提现")


def register():
    print("注册")


func_dict = {
    "0": ["退出",None],
    "1": ["登录", login],
    "2": ["转账", transfer],
    "3": ["查询余额", check_banlance],
    "4": ["提现", withdraw],
    "5": ["注册", register],
}

while True:
    # print("""
    # 0 退出
    # 1 登录
    # 2 转账
    # 3 查询余额
    # 4 提现
    # 5 注册
    # """)
    for k in func_dict:
        print(k,func_dict[k][0])

    choice = input("请输入命令编号： ").strip()
    if not choice.isdigit():
        print("必输输入编号")
        continue

    if choice == "0":
        break

    if choice in func_dict:
        func_dict[choice][1]()
    else:
        print("命令编号不存在")

    #
    # if choice == "1":
    #     login()
    # if choice == "2":
    #     transfer()
    # if choice == "3":
    #     check_banlance()
    # if choice == "4":
    #     withdraw()
    # else:
    #     print("指令不存在")
