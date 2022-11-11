from __future__ import print_function

from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(host='localhost',
                             database='world',
                             user='adi',
                             password='mysDublin#1')

# Get two buffered cursors
curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)

# Query 
query = ("SELECT DISTINCT Name FROM world.country WHERE name like 'I%'")

curA.execute(query)

# Iterate through the result of curA
for (name) in curA:
  print(name)  

cnx.close()