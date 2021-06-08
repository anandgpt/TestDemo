import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Holi#123", database="Anandetails")

mycursor = mydb.cursor()
#sql="CREATE DATABASE ANANDETAILS"
#sql="Create table Information(friend_name varchar(15), phone_no bigint(10))"
"""sql =" insert into information(friend_name,phone_no) values(%s,%s)"
val =[


    ('Anurag panday', 9455688558),
    ('Krishnakant', 9865669465)
    ]
mycursor.executemany(sql, val)
mydb.commit()"""
sql="Select friend_name,phone_no from information"
mycursor.execute(sql);
myresult=mycursor.fetchall();
for x in myresult:
  print(x)
print(mydb)
print("Query executed")