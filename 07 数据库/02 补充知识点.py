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
    database = "day48",
    charset = "utf8",#  编码千万不写成utf-8
    autocommit = True, # 自动提交
)  # 链接数据库

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 产生一个游标对象,帮我们执行命令

# 增
sql = "insert into user(name,password) values(%s,%s)"
# rows =cursor.execute(sql,("nicai","123456"))
rows = cursor.executemany(sql,[("nicai","123456"),("nicai","123456"),("nicai","123456")])
print(rows)
# conn.commit() # 确认操作

# # 改
# sql = "update user set name='buzhidao' where id=2"
# rows =cursor.execute(sql)
# print(rows)
# conn.commit() # 确认操作
#
# # 删除
# sql = 'delete from user id=1'
# rows = cursor.execute(sql)
# conn.commit() # 确认操作
"""
增删改查中
    增删改涉及到数据的修改
    需要二次确认
"""







