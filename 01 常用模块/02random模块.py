#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/28 14:15

import random
#
# print(random.random())#(0,1)----float    大于0且小于1之间的小数
#
# print(random.randint(1,3))  #[1,3]    大于等于1且小于等于3之间的整数
#
# print(random.randrange(1,3)) #[1,3)    大于等于1且小于3之间的整数
#
# print(random.choice([1,'23',[4,5]]))#1或者23或者[4,5]，可以自定义随机内容
#
# print(random.sample([1,'23',[4,5]],2))#在列表元素内随机返回任意2个组合
#
# print(random.uniform(1,3))#大于1小于3的小数，如1.927109612082716
#
#
# item=[1,3,5,7,9]
# random.shuffle(item) #打乱item的顺序,相当于"洗牌"
# print(item)

# 应用：随机验证码

res = ""
for i in range(6):
    s1 = chr(random.randint(65,90)) # chr() 返回一个字符相对应的Unicode字符
    s2 = str(random.randint(0,9))
    res += random.choice([s1,s2])
print(res)








