import mysql.connector as db
fobj=open('D://primenumbers.txt','r')
con=db.connect(user='root',password='Chennarao_42',\
           host='localhost',database='emp')
cur=con.cursor()
insert_query=''' insert into student values(%S,%s,%s,%s,%s,%s)'''
if fobj.readable():
    for row in fobj:
        data=row.split('|')
        cur.execute(insert_query,[int(data[0]),data[1],float(data[2]),data[3],data[4],int(data[5])])
con.commit()
fobj.close()
cur.close()
con.close()
        
