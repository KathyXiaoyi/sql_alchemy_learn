from sqlalchemy.engine import create_engine

engine = create_engine('mysql://root:@127.0.0.1:3306/test?charset=utf8mb4', echo=True)
connection = engine.connect()
print connection
