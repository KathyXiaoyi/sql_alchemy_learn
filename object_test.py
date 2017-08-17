# encoding: utf-8

import model
from sqlalchemy import orm
from sqlalchemy import create_engine

# 创建数据库引擎 & 建立所有表
engine = create_engine('mysql://root:@127.0.0.1:3306/test?charset=utf8mb4', echo=True)
model.metadata.bind = engine
model.metadata.create_all()

# 建立session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)
session = orm.scoped_session(sm)

