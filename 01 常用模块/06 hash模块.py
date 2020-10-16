#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: untitled
# @Time : 2020/9/29 14:59

# 使用
# import hashlib
# m = hashlib.md5()
# m.update("hello".encode("utf-8"))
# res = m.hexdigest()
# print(res)


# 模拟撞库
cryptograph = "aee949757a2e698417463d47acac93df"

import hashlib
# 制作密码字典
passwds=[
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]
dic = {}
# 撞库获得明文密码
for p in passwds:
    res = hashlib.md5(p.encode("utf-8"))
    dic[p] = res.hexdigest()

for k,v in dic.items():
    if v == cryptograph:
        print("撞库成功 %s"%(k))


#要想保证hmac最终结果一致，必须保证：
#1:hmac.new括号内指定的初始key一样
#2:无论update多少次，校验的内容累加到一起是一样的内容

# 操作一
import hmac
h1=hmac.new('hello'.encode('utf-8'),digestmod='md5')
h1.update('world'.encode('utf-8'))

print(h1.hexdigest()) # 0e2564b7e100f034341ea477c23f283b

# 操作二
import hmac
h2=hmac.new('hello'.encode('utf-8'),digestmod='md5')
h2.update('w'.encode('utf-8'))
h2.update('orld'.encode('utf-8'))
h2.update('orld'.encode('utf-8'))

print(h1.hexdigest()) # 0e2564b7e100f034341ea477c23f283b

