import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='python')
sql_drop ='drop table student'
sql = 'create table student(id int,name varchar(20),score double)'

cursor = conn.cursor()
# cursor.execute(sql_drop)
# cursor.execute(sql)
cursor.execute('''insert into student(id,name,score) values (1,'hd',50)''')

conn.commit()

cursor.close()
conn.close()