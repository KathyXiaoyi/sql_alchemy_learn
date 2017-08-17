# encoding: utf-8
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


# 创建数据库引擎(数据库连接池) - 使用内存数据库sqlite
engine = create_engine('sqlite:///:memory:', echo=True)
# 建立连接
conn = engine.connect()


metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('fullname', String(50)),
              Column('password', String(12))
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

metadata.create_all(engine)

