import sqlite3
from google.cloud import storage
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys
con=mysql.connector.connect(user='root',password='Anand@123' host='35.223.49.176', database='Customer')
cursor=con.cursor();
query=("select * from sampledatafoodsales")
cursor.execute(query)
frame=pd.Dataframe(cursor.fetchall)