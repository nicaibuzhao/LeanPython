#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/22 9:27

# def my_range(start,stop,step=1):
#     while start < stop:
#         yield start
#         start += step
#
# for i in my_range(1,5):
#     print(i)


def dog(name):
    food_list = []
    print("%s 开始吃东西了"% name)
    while True:
        # x拿到的是yield接收的值
        x = yield  food_list# x = 锅包肉
        print("%s 吃了 %s" % (name,x))
        food_list.append(x)
g = dog("alex") # 函数内出现yield，此时调用函数就会返回一个生成器
g.send(None) # 等同于 next(g) 相当于初始化生成器

res = g.send("骨头")
print(res)
res = g.send("锅包肉")
print(res)


# g.close() # 关闭之后不可传值