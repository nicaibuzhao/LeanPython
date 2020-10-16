# -*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/10 14:16


# 先定义类
class Student():
    # 1、定义变量
    stu_school = 'oldboy'

    # 2、定义功能
    def tell_stu_info(stu_obj):
        print('学生信息：名字%s 年龄：%s 性别：%s'%(
            stu_obj['stu_name'],
            stu_obj['stu_age'],
            stu_obj['stu_gender'],
        ))

    def set_info(stu_obj,x,y,z):
        stu_obj['stu_name']=x
        stu_obj['stu_age']=y
        stu_obj['stu_gender']=z

    print("===============================")
# 再调用类产生对象
stu1_obj = Student()
stu2_obj = Student()
stu3_obj = Student()