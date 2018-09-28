#!/opt/bb/bin/python

from sqlalchemy import inspect
from sqlalchemy.sql import select

from insert_data import engine, metadata, cookies

print("Query data start")

inspector = inspect(engine)
print(inspector.get_table_names())

print("Select all")
s = select([cookies])
print str(s)

rp = engine.execute(s)
print(type(rp))
results = rp.fetchall()
print(results)
print(type(results))
print(type(results[0]))

print("Select some columns")
s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = engine.execute(s)
keys = rp.keys()
print(keys)
print(type(keys))
result = rp.first()
print(result)
print(type(result))

print("Select with ordering")
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
rp = engine.execute(s)
for cookie in rp:
    print("{} - {}".format(cookie.quantity, cookie.cookie_name))

print("Query data end")


