#coding:utf-8
from flask.globals import request
from flask.json import jsonify
import datetime

class Access:
    def validateToken(self):
        def _token(func):
            def __token(*args):
                getToken=request.args.get("token")
                from v1.db.DbHelper import DbHelper
                dh=DbHelper()
                user_token=dh.load("UserMapper", "user_token")
                
                ret=dh.do("query",user_token).filter(user_token.tokenstr==getToken\
                                                     ,user_token.starttime<=datetime.datetime.now()\
                                                     ,user_token.endtime>=datetime.datetime.now()).first()
                
                if ret:
#                     print ret.appid
                    return func(*args,appid=ret.appid)
                else:
                    return jsonify({"result":"access error"})
                
            return __token
        return _token