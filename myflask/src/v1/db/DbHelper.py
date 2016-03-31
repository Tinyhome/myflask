#coding:utf-8
from sqlalchemy import create_engine

def getsession():

    connect_string="mysql+mysqldb://root:jiafabing@localhost/myweb"
    eng=create_engine(connect_string,echo=False)  #创建数据库引擎
    
    from sqlalchemy.orm import sessionmaker
    DB_Session=sessionmaker(bind=eng)
    session=DB_Session()
    session.execute("set names utf8")
    return session

class DbHelper:
    
    dbsession=None
    def __init__(self):
        self.dbsession=getsession()
        
    def load(self,mname,mclass):
        #动态加载模块
        m=__import__("v1.db."+mname,fromlist=[mclass])     #获得模块
        getclass=getattr(m, mclass)                        #获得类名
        return getclass

    def do(self,methodname,*args):
        do_method=getattr(self.dbsession, methodname)  
        return do_method(*args)