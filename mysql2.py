######################################################
# File Name: mysql2.py
# _*_ coding:UTF-8 _*_
# Author: linuan
# Mail: li-nuan@qq.com
#===================================================
#!/usr/bin/python
import mysql.connector as db
import __future__
try:
	mydb=db.connect(
			host="localhost",
			user="root",
			passwd="li123..",
			database="test"
			)
	
	myedit=mydb.cursor()
	'''
	sql="INSERT INTO student (id,name) VALUES (%s, %s)"
	val=[
		(110,'fit1'),
		(111,'fit2'),
		(112,'fit3')
	]
	
	myedit.executemany(sql,val)
	'''
	#myedit.execute("SELECT id,name FROM student WHERE name='fit1'")
	myedit.execute("SELECT id,name FROM student WHERE name LIKE '%it%'")
	result=myedit.fetchall()
	for x in result:
		print x
#	mydb.commit()
#	print "Insert sucess,ID",myedit.lastrowid
except Exception,e:
	print e
finally:
	myedit.close()
	mydb.close()
