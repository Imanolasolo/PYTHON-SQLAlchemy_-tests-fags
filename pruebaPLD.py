#!/usr/bin/python3
import sqlalchemy as db
from sqlalchemy import (create_engine)
# stablish a connection
engine = create_engine('mysql+mysqldb://root:root@localhost/classicmodels')

# create views of employees table
metadata = db.MetaData()
employees = db.Table('employees', metadata, autoload= True, autoload_with=engine)
# print views of table employees
print(employees.columns.keys())
print(repr(metadata.tables['employees']))

#Create views of records
s = employees.select()
conn = engine.connect()
result = conn.execute(s)
# print records
for row in result:
   print (row)