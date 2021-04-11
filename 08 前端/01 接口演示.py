#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: LeanPython
# @Time : 2020/12/14 19:54

from flask import Flask,request

app = Flask(__name__)
@app.route('/index/',methods=['get','post'])
def index():
    print(request.form) # 获取前端form表单提交过来的非文件数据
    # print(request.files) # 获取前端form表单提交过来的文件数据
    # file_obj = request.files.get('myfile.png')
    # file_obj.save(file_obj.name)
    return "ok"

app.run()