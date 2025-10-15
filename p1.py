import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "svgu"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE svgu")

# mycursor.execute("CREATE TABLE EMP(ein INT,ename VARCHAR(25),gender CHAR(1),salary FLOAT)")

# sql  = "INSERT INTO emp VALUES(%s,%s,%s,%s)"
# val = [('1','rudra','m','100000'),
#        ('2','nidhi','f','50000'),
#        ('3','vismay','m','70000'),]
# mycursor.executemany(sql,val)
# mydb.commit()

sql = "SELECT * FROM emp"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
