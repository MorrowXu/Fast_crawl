#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : mysql_orm.py
# @Email   : 464580843@qq.com
# Create on 2018/3/20 15:44
from sqlalchemy import create_engine # 创建连接
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # 导出连接库
from sqlalchemy import Column, String, Integer, Text,VARCHAR # 导入列数据类型
Base = declarative_base()

class Webcrawler_jobbole(Base):

    __tablename__ = 'jobbole'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR)
    content = Column(Text)
    create_time = Column(VARCHAR)
    url = Column(VARCHAR)

class Webcrawler_baike(Base):
    __tablename__ = 'new_baike_key'

    id = Column(Integer, primary_key=True)
    key_word = Column(VARCHAR)
    content = Column(Text)
    url = Column(VARCHAR)

class add_data(object):


    def __init__(self):
        engine = create_engine('mysql+pymysql://root:930502@localhost:3306/webcrawler?charset=utf8')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def baike_conn(self, data):
        user = Webcrawler_baike(key_word=data['title'], content=data['para'], url=data['url'])
        self.session.add(user)
        self.session.commit()


    def jobbole_conn(self, data):
        user = Webcrawler_jobbole(title=data['title'], content=data['content'], create_time=data['create_time'], url=data['url'])
        self.session.add(user)
        self.session.commit()

