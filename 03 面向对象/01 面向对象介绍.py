# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/10 13:31

"""
面向过程：
    核心是 ‘过程’二字

    过程的终极奥义就是将程序流程化
    过程是 流水线，用来分步骤解决问题的

面向对象：
    核心是 对象 二字

    对象的终极奥义就是将程序 整合
    对象是 容器，用来盛放数据与功能的
"""
# 程序 = 数据 + 功能
# 学生的数据
stu_name = "alex"
stu_age = 18
stu_gender = 'male'

# 学生的功能
def tell_info():
    print(f"姓名：{stu_name},年龄：{stu_age},性别：{stu_gender}")

