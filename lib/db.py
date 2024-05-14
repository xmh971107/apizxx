import logging
import pymysql
from config.config import *

import sys
sys.path.append('..') #提升一级到项目根目录下
import  pymysql
def conn():
    con=pymysql.connect(host="db_host",port=db_port,
                           database="xzs",user="db_user",
                           password="db_ps",db=db,charset="utf8")
    return  con
#封装数据库查询操作
def query_db(sql):
    con=conn()
    #创建游标
    cursor=con.cursor()
    logging.debug(sql)
    #创建游标执行sql
    cursor.execute(sql)
    #获取执行的结果
    result=cursor.fetchone()
    logging.debug(result)
    #关闭游标
    cursor.close()
    #关闭连接
    con.close()
    return result
#封装更改数据库操作
def change_db(sql):
    con=conn()
    cursor=con.cursor()
    try:
        cursor.execute(sql)
        #如果成功就提交
        con.commit()
    except Exception as e:
        logging.error(str(e))
    #如果失败就回滚
        con.rollback()
    finally:
        cursor.close()
        con.close()
def check_user(name):
    rel=query_db("select * from t_user where user_name ='{}'".format(name))
    return True if rel else False
def add_user(name,ps):
    change_db("insert into t_user('user_name','password')values ('{}','{}')".format(name,ps))
    print("add")
def del_user(name):
    change_db("delete from t_user where  user_name={}".format(name))
    print("删除")