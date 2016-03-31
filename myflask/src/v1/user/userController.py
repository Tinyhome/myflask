#coding:utf-8

from flask.json import jsonify
from v1.Cache import Cache
from flask.globals import request
from v1.Access import Access

mycache=Cache()
access=Access()

class userController:
    
    def __init__(self):
        pass
    
    @mycache.set("userlist", 20)
    def get_list(self):
        print "use database"
        return jsonify({"result":"sucess"})
    
    @access.validateToken()
    def do(self,appid=""):
        print "appid:"+appid
        if request.method=="POST":
            return jsonify({"result":"add a user"})
        
        if request.method=="PUT":
            return jsonify({"result":"edit a user"})
        
        return jsonify({"result":"do sucess"})