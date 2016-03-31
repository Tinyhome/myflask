#coding:utf-8
from flask.json import jsonify
from v1.Cache import Cache
from flask.globals import request


class tokenController:
    
    def do(self):
        if request.method=="GET":
            appid=request.args.get("appid","")
            appsecret=request.args.get("appsecret","")
            if appid=="" or appsecret=="":
                return jsonify({"token":"null"})
            else:
                from v1.db.DbHelper import DbHelper
                dh=DbHelper()
                user_token=dh.load("UserMapper","user_token")
                sql=dh.do("query",user_token).filter(user_token.appid==appid,
                                                     user_token.appsecret==appsecret)
                
                getUser=sql.first()
                if getUser:
                    import hashlib
                    tokenstr=hashlib.sha256(appid+appsecret).hexdigest()
                    import datetime
                    now=datetime.datetime.now()
                    starttime=now.strftime("%Y-%m-%d %H:%M:%S")
                    endtime=now+datetime.timedelta(seconds=30)
                    sql.update({"tokenstr":tokenstr,"starttime":starttime,"endtime":endtime})
                    dh.do("commit")
                    return jsonify({"token":tokenstr})
                    
                else:
                    return jsonify({"token":"null"})
                