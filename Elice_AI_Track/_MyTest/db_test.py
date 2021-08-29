import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', charset='utf8') 
cursor = conn.cursor() 

sql = "CREATE DATABASE developer2" 

cursor.execute(sql) 

conn.commit() 
conn.close() 