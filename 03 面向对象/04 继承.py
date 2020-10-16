#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/10/12 16:16



# 3 如何实现继承
# 示范1 ： 类与类之间存在冗余问题
# class Student():
#     school = "oldboy"
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def choose_course(self):
#         print(f'学生：{self.name} 正在选课')
#
# class Teacher():
#     school = "oldboy"
#
#     def __init__(self,name,age,sex,salary,level):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print(f"老师：{self.name} 正在给学生打分")


# 示范2：基于继承，解决代码冗余的问题

# class OldboyPeople():
#     school = "oldboy"
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# class Student(OldboyPeople):
    # school = "oldboy"
    #
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    # def choose_course(self):
    #     print(f'学生：{self.name} 正在选课')

# stu_obj = Student("alex",18,"female")
# print(stu_obj.choose_course())
# print(stu_obj.school)


# class Teacher(OldboyPeople):
#     # school = "oldboy"
#
#     def __init__(self,name,age,sex,salary,level):
#         OldboyPeople.__init__(self,name,age,sex)
#         self.salary = salary
#         self.level = level
#
#     def score(self):
#         print(f"老师：{self.name} 正在给学生打分")
#
# to_teacheer = Teacher("alex",18,"female",3000,"hight")
# print(to_teacheer.__dict__)
# print(to_teacheer.score())
# print(to_teacheer.school)

# 4 单继承下的属性查找

class Foo:
    def f1(self):
        print("Foo.f1")

    def f2(self):
        print("Foo.f2")
        self.f1()

class Bar(Foo):
    def f1(self):
        print("Bar.f1")

obj = Bar()
obj.f2()