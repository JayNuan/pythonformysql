######################################################
# File Name: createdatabases.py
# _*_ coding:UTF-8 _*_
# Author: linuan
# Mail: li-nuan@qq.com
#===================================================
#!/usr/bin/python
import mysql.connector as db
try:
	mydb=db.connect(
			host='localhost',
			user='root',
			passwd='li123..'
			)
	
	myedit=mydb.cursor()
	myedit.execute("CREATE DATABASE if not exists linuan")
	myedit.execute("show databases")

	for x in myedit:
		print x
except:
	print "The command is error"
finally:
	myedit.close()
	mydb.close()
