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

class User(Base):

    __tablename__ = 'jobbole'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR)
    content = Column(Text)
    create_time = Column(VARCHAR)
    url = Column(VARCHAR)

def add_data(data):
    engine = create_engine('mysql+pymysql://root:930502@localhost:3306/webcrawler?charset=utf8')
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(title=data['title'], content=data['content'], create_time=data['create_time'], url=data['url'])
    session.add(user)
    session.commit()

