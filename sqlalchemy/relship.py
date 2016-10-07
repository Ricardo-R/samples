#!/usr/bin/python
# coding=UTF-8
# pylint: disable=no-member

import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

MYSQL_URI='mysql+mysqldb://auth:auth@localhost/test?charset=utf8'

engine      = create_engine(MYSQL_URI, max_overflow=5, echo=False)
Base = declarative_base()

class Pen(Base):
    __tablename__ = 'pen'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    # 开启级联删除，默认不开启
    papers = relationship('Paper', backref='pen', cascade='all')

class Paper(Base):
    __tablename__ = 'paper'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    pen_id = Column(Integer, ForeignKey('pen.id'))

# 一对多关系的测试例子
def one2m_test(engine=''):
    # sessionmaker returns class instead of instance
    Session = sessionmaker(bind=engine)

    # add 
    session = Session()
    pens = []
    pens.append(Pen(id=1, name='vex'))
    pens.append(Pen(id=2, name='alex'))
    pens.append(Pen(id=3, name='mario'))
    session.add_all(pens)
    session.commit()

    papers = []
    papers.append(Paper(id=1, name='Fire', pen_id='1'))
    papers.append(Paper(id=2, name='WhiteWalker', pen_id='2'))
    papers.append(Paper(id=3, name='WhiteWalker', pen_id='3'))
    session.add_all(papers)
    session.commit()

    # 级联删除
    rs = session.query(Pen).filter(Pen.id==2).first()
    session.delete(rs)
    session.commit()

    rs = session.query(Pen).get(3)
    session.delete(rs)
    session.commit()

    session.close()

user_group = Table('user_group', Base.metadata,
                Column('user_id', Integer, ForeignKey('users.id')),
                Column('group_id', Integer, ForeignKey('groups.id')))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    groups = relationship('Group', secondary=user_group, enable_typechecks=False,
            backref=backref('users',enable_typechecks=False))

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

# 多对多关系的测试例子
def m2m_test(engine=''):
    # sessionmaker returns class instead of instance
    Session = sessionmaker(bind=engine)

    # add 
    session = Session()
    users = []
    users.append(User(id=1, name='vex'))
    users.append(User(id=2, name='alex'))
    users.append(User(id=3, name='mario'))
    session.add_all(users)
    session.commit()

    groups = []
    groups.append(Group(id=1, name='Fire'))
    groups.append(Group(id=2, name='WhiteWalker'))
    groups.append(Group(id=3, name='WhiteWalker'))
    session.add_all(groups)
    session.commit()

    # Build/Modify many-to-many relationship
    rs = session.query(User).get(1)
    rg = session.query(Group).filter(Group.id>1).all()
    rs.groups = rg
    session.add(rs)
    session.commit()

    rg = session.query(Group).get(1)
    rs = session.query(User).filter(User.id>1).all()
    rg.users = rs
    session.add(rg)
    session.commit()

    session.close()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def run():
    one2m_test(engine)
    m2m_test(engine)

if __name__ == '__main__':
    run()
