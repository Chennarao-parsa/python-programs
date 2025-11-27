import mysql.connector as db
con=db.connect(user='root',password='Chennarao_42',host='localhost',database='emp')
cur=con.cursor()
insert_sql='''
insert into employee1 values(%s,%s,%s,%s,%s)
'''
data=[12,'chinna',8,'hyderabad','male']
cur.execute(insert_sql,data)
con.commit()
cur.close()
con.close()
