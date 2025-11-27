# connection
import mysql.connector as db
con=db.connect(user='root',password='Chennarao_42',host='localhost',database='emp')
#print(con)
cur=con.cursor()
cur.execute('select * from employee1')
data=cur.fetchall()
#print(data)
for row in data:
    print(row[1],' -- ',row[2])
cur.close()
con.close()
