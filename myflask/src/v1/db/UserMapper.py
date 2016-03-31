#coding:utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,VARCHAR,TIMESTAMP
from sqlalchemy.sql import func

UserBase=declarative_base()

class user_role(UserBase):
    
    __tablename__="user_role"
    
    def __init__(self,id,rolename):
        self.id=id
        self.rolename=rolename
    
    id=Column(Integer,primary_key=True)
    rolename=Column(VARCHAR(50))
    
class user_sys(UserBase):
    __tablename__="user_sys"
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_name=Column(VARCHAR(50),nullable=False)
    user_pwd=Column(VARCHAR(50),nullable=False,default="123")
    user_regdate=Column(TIMESTAMP,nullable=False,default=func.current_timestamp())
    
class user_info(UserBase):
    __tablename__="user_info"
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,nullable=False)
    user_qq=Column(VARCHAR(50))
    
class user_token(UserBase):
    __tablename__="user_token"
    id=Column(Integer,primary_key=True,autoincrement=True)
    appid=Column(VARCHAR(100),nullable=False)
    appsecret=Column(VARCHAR(100),nullable=False)
    tokenstr=Column(VARCHAR(200))
    starttime=Column(TIMESTAMP)
    endtime=Column(TIMESTAMP)
    
    
    