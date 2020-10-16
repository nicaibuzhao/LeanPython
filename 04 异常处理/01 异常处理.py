#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/10/16 15:18

# 1 什么是异常？
# 异常是异常是程序发生错误的信号，程序一旦出错就会抛出异常，程序的运行随即终止

# print('start...')
# [1231][1000]
# print('stop...')

# 1.1 异常处理的三个特征
# 异常的追踪信息
# 异常的类型
# 异常的内容

# 2 为何处理异常
#  为了增强程序的健壮性，即便程序运行过程中出错了，也不要终止程序
# 而是捕捉异常并处理：将出错信息记录在日志里

# 3 如何处理异常？
# 3.1 语法上的错误
# 处理方式一：必须在程序运行前就改正
# if 1>2
#     print('run....')


# 3.2 逻辑上的错误
# # TypeError：数字类型无法与字符串类型相加
# 1+'2'
#
# # ValueError：当字符串包含有非数字的值时，无法转成int类型
# num=input(">>: ") #输入hello
# int(num)
#
# # NameError：引用了一个不存在的名字x
# x
#
# # IndexError：索引超出列表的限制
# l=['egon','aa']
# l[3]
#
# # KeyError：引用了一个不存在的key
# dic={'name':'egon'}
# dic['age']
#
# # AttributeError：引用的属性不存在
# class Foo:
#     pass
# Foo.x
#
# # ZeroDivisionError：除数不能为0
# 1/0

# 3.2 针对逻辑上的异常又分为两种处理方式
# 3.2.1 错误发生的条件是可以预知的，使用if判断来解决
# age = input('>>>>: ').strip() # 输入的只要不是数字就会出错
# if age.isdigit():
#     age = int(age)
#     if age > 18:
#         print('猜大了')
#     elif age < 18:
#         print('猜小了')
#     else:
#         print('猜对了')
# else:
#     print('必须输入数字~~')

# 3.2.2 错误发生的条件是无法预知的
# try:
#     # 有可能会抛出异常的代码
#     子代码块1
#     子代码块2
#     子代码块3
# except 异常类型1 as e:
#     pass
# except 异常类型2 as e:
#     pass
# ....
# else:
#     如果被监测的子代码块,没有异常发生,则会执行else
# finally:
#     无论被监测的代码块有没有异常,都会执行finally的子代码

# 用法一
# print('start....')
#
# try:
#     print('11111111111111')
#     l = ["aaa",'bbbb']
#     l[3] # 抛出异常 IndexError，被监测的代码块同级别的后续代码不会运行
#
#     print('22222222222222')
#     print('x')
#
#     print('33333333333333')
#     dic = {"a":1}
#     dic['a']
# except IndexError as e:
#     print('异常已经被处理',e)
# print('end....')

# 用法二：
# print('start....')
#
# try:
#     print('11111111111111')
#     l = ["aaa",'bbbb']
#     # l[3] # 抛出异常 IndexError，被监测的代码块同级别的后续代码不会运行
#
#     print('22222222222222')
#     xxxx
#
#     print('33333333333333')
#     dic = {"a":1}
#     dic['a']
# except IndexError as e:
#     print('异常已经被处理',e)
# except NameError as e:
#     print('异常已经被处理',e)
# print('end....')

# 用法三：
# print('start....')
#
# try:
#     print('11111111111111')
#     l = ["aaa", 'bbbb']
#     # l[3] # 抛出异常 IndexError，被监测的代码块同级别的后续代码不会运行
#
#     print('22222222222222')
#     xxxx
#
#     print('33333333333333')
#     dic = {"a": 1}
#     dic['a']
# except (IndexError,NameError) as e:
#     print('异常已经被处理', e)
# except KeyError as e:
#     print("字典的key不存在：",e)
# except Exception as e:# 万能异常
#     print("所有异常都可以匹配上")
#
# print('end....')


# 用法四：else 不能单独与try配合使用，必须要搭配 except
# print('start....')
#
# try:
#     print('11111111111111')
#     l = ["aaa", 'bbbb']
#     # l[3] # 抛出异常 IndexError，被监测的代码块同级别的后续代码不会运行
#
#     print('22222222222222')
#     xxxx
#
#     print('33333333333333')
#     dic = {"a": 1}
#     dic['a']
#
# except Exception as e:# 万能异常
#     print("所有异常都可以匹配上")
# else:
#     print("==============")
#
# print('end....')


# 用法五： finally可以单独与try配合使用
print('start....')

try:
    print('11111111111111')
    l = ["aaa", 'bbbb']
    # l[3] # 抛出异常 IndexError，被监测的代码块同级别的后续代码不会运行

    print('22222222222222')
    xxxx

    print('33333333333333')
    dic = {"a": 1}
    dic['a']

finally: # 不处理异常，无论是否发生异常都会执行finally的子代码
    # 应该把被监测代码中回收系统资源的代买，写在finally中
    print("==============")

print('end....')