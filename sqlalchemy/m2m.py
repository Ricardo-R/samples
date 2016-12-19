#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Sequence
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref
from devrest.model.ext import DictableModel, RestModel
from devrest.model.purview import register_filter
from flask import request

Base = declarative_base(cls=DictableModel)

class User(Base, RestModel):
    __tablename__ = 'users'
    __key_field__ = 'name'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name    = Column(String(64), nullable=False, unique=True)
    name_zh = Column(String(128), nullable=True)
    projects= association_proxy('user_projects', 'project')
    '''
    如果要访问到role的信息，需要访问user_projects。
    使用代理的好处是，屏蔽了中间表的细节，操作可以方便等同于使用Table,
    但是，role信息是访问必须的，所以我们如果要访问role信息就不应该屏蔽
    中间表。使用了代理之后，projects可以方便访问到对应的所有项目，
    user_projects可以访问到对应的中间对象。
    '''

    def __init__(self, name, name_zh=''):
        self.name   = name
        self.name_zh= name_zh


class Project(Base, RestModel):
    __tablename__ = 'projects'
    __key_field__ = 'name'
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name    = Column(String(64), nullable=False, unique=True)
    desc    = Column(String(256), nullable=True)
    users   = association_proxy('project_users', 'user')

    def __init__(self, name, desc=''):
        self.name   = name
        self.desc   = desc


class UserProject(Base):
    __tablename__ = 'user_project'
    user_id     = Column(Integer, ForeignKey('users.id'), primary_key=True)
    project_id  = Column(Integer, ForeignKey('projects.id'), primary_key=True)
    role        = Column(String(64), nullable=True)
    user        = relationship(User,
                    backref=backref('user_projects', enable_typechecks=False))
    project     = relationship(Project,
                    backref=backref('project_users', enable_typechecks=False))

    def __init__(self, proxy=None, role=None):
        self.role = role
        if type(proxy) is User:
            self.user   = proxy
        elif type(proxy) is Project:
            self.project= proxy

def m2mtest():
    u = User('lg')
    p = Project('gdc')
    u.projects.append(p)
    p.users.append(u)

    '''
    This will show you that 'u.projects.append(p)' equivalent to 'p.users.append(u)' above.
    Both do that same thing, also means a duplicate INSERT on 'UserProject'.
    Be careful!
    '''
    print u.projects
    print p.users

if __name__ == '__main__':
    m2mtest()
