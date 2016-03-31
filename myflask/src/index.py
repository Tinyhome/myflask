#coding:utf-8

from flask import Flask,jsonify
from sqlalchemy.sql import func
from flask.globals import request

bbb =Flask(__name__)   #__main__

from flaskext.mysql import MySQL
bbb.config.from_pyfile("tiny.conf", silent=False)

mysql = MySQL()
mysql.init_app(bbb)


@bbb.route("/<controller>",methods=["GET","POST","PUT","ABC"])
def index(controller):    # 使用网址中路由中的两个参数,http://127.0.0.1:9090/v1/get/user/detail
    
#     print request.args.get("username","tiny")
#     print request.form.get("age",0)
#     print request.json
    
    version=request.headers.get("version","v1")
#     print request.json.get("age")
    
    
    #动态加载模块
    m=__import__(version+"."+controller+"."+controller+"Controller",fromlist=[controller+"Controller"])     #获得模块
    getclass=getattr(m, controller+"Controller")  #获得类名
    method=getattr(getclass(), "do") #获取方法
    
    print request.method
    print request.headers.get("version","v1")
    
    return method()
      

bbb.run("127.0.0.1",9090,debug=True)