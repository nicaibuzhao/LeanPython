#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/12/4 9:31

import pymysql

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = "root",
    password = '123456',
    database = "day47",
    charset = "utf8" #  编码千万不写成utf-8
)  # 链接数据库

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 产生一个游标对象,帮我们执行命令
"""
pymysql.cursors.DictCursor  以字典的形式返回结果
"""
sql = 'select * from emp;'

res = cursor.execute(sql)
# print(res)  # execute 返回的是当前sql语句所影响的行数
# 获取命令的查询结果
# print(cursor.fetchone()) # 只拿一条
# print(cursor.fetchall()) # 拿所有
print(cursor.fetchmany(2)) # 指定拿几条数据

cursor.scroll(1,"relative") # 相对于光标所在的位置继续向后移动1位
cursor.scroll(1,"absolute") # 相对于数据的开头往后继续移动1位













