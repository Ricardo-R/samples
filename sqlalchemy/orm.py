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
from sqlalchemy.orm import sessionmaker

MYSQL_URI='mysql+mysqldb://auth:auth@localhost/test?charset=utf8'

engine      = create_engine(MYSQL_URI, max_overflow=5, echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'userx'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Addr(Base):
    __tablename__ = 'addrx'
    id = Column(Integer, primary_key=True)
    email = Column(String(40))

def orm_test(engine=''):
    # sessionmaker returns class instead of instance
    Session = sessionmaker(bind=engine)

    # add
    session = Session()
    new = User(name='test')
    session.add(new)
    session.commit()

    users = []
    users.append(User(name='vex'))
    users.append(User(name='alex'))
    users.append(User(id=1000, name='mario'))
    session.add_all(users)
    session.commit()
    session.close()

    # update
    session = Session()
    session.query(User).filter(User.id == 1000).update({'id' : 2000})
    session.commit()
    session.close()

    # query
    session = Session()
    rs = session.query(User).filter_by(name = 'mario').all()
    print rs
    for i in rs:
        print (i.id, i.name)
    rs = session.query(User).filter_by(name = 'mario').first()
    print rs
    print rs.id, rs.name
    session.commit()
    session.close()

    # delete
    session = Session()
    session.query(User).filter(User.name == 'mario').delete()
    session.commit()
    session.close()

    session.close()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    user_id = Column(Integer, ForeignKey('person.id'))

def fkey_test(engine=''):
    # sessionmaker returns class instead of instance
    Session = sessionmaker(bind=engine)

    # ForeignKey example
    session = Session()
    users = []
    users.append(Person(id=1, name='vex'))
    users.append(Person(id=2, name='alex'))
    users.append(Person(id=3, name='mario'))
    session.add_all(users)
    session.commit()

    books = []
    books.append(Book(id=1, name='Fire', user_id='1'))
    books.append(Book(id=2, name='WhiteWalker', user_id='1'))
    books.append(Book(id=3, name='WhiteWalker', user_id='3'))
    session.add_all(books)
    session.commit()

    session.close()

def run():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    orm_test(engine)
    fkey_test(engine)

if __name__ == '__main__':
    run()
