# encoding: utf -8

from model import users, addresses, conn

# 单条插入：
ins = users.insert().values(name='jack', fullname='Jack Jones')
conn.execute(ins)
# 单条插入
conn.execute(users.insert(), name='wendy', fullname='Wendy Williams')

# 批量插入
to_insert_data_list = [
    {'name': 'wendy', 'fullname': 'Wendy Williams'},
    {'name': 'lily', 'fullname': 'su lily'},
    {'name': 'lucy', 'fullname': 'wu lucy'},
]
conn.execute(users.insert(), to_insert_data_list)
# 批量插入
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address': 'jack@yahoo.com'},
    {'user_id': 1, 'email_address': 'jack@msn.com'},
    {'user_id': 2, 'email_address': 'www@www.org'},
    {'user_id': 2, 'email_address': 'wendy@aol.com'},
])
