#!/usr/bin/python
# coding=UTF-8

from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData, ForeignKey
import MySQLdb

MYSQL_URI='mysql+mysqldb://auth:auth@localhost/test?charset=utf8'

engine      = create_engine(MYSQL_URI, max_overflow=5, echo=True)
metadata    = MetaData()

def tables(metadata=''):
    user = Table('user', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(20)))
    addr = Table('addr', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('email', String(40)),
                    Column('user_id', ForeignKey('user.id')))

def sql_test(engine=''):
    engine.execute("insert into user(id, name) values(null, 'alex');") 
    engine.execute("insert into user(id, name) values(null, 'vex');") 
    rs = engine.execute("select id from user where name='vex';") 
    vexid = int(rs.first()[0])
    sql = "insert into addr(email, user_id) values('vex@gmail.com', %ld);" %(vexid)
    engine.execute(sql) 

def run():
    metadata.drop_all(engine)
    tables(metadata)
    metadata.create_all(engine)
    sql_test(engine)

if __name__ == '__main__':
    run()
