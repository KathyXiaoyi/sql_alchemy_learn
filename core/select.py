# encoding: utf-8

from sqlalchemy.sql import select
from model import users, addresses, conn

# 执行查询
s = select([users])
# 类似于RDB的游标（cursor）
result = conn.execute(s)

# 遍历查询结果
for row in result:
    print row

# 只获取查询结果中的一条记录
row = result.fetchone()
# 使用字段名
print 'name:', row['name'], ' fullname:', row['fullname']
# 使用下标
print 'name:', row[1], ' fullname:', row[2]
# 使用model Column对象
print 'name:', row[users.c.name], ' fullname:', row[users.c.fullname]

# 显式关闭结果集
result.close()


# 只查询特定字段
s = select([users.c.name, users.c.fullname])
result = conn.execute(s)
for row in result:
    print row

# where语句
s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
s = select([users]).where(users.c.id == 2)



