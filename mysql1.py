######################################################
# File Name: mysql1.py
# _*_ coding:UTF-8 _*_
# Author: linuan
# Mail: li-nuan@qq.com
#===================================================
#!/usr/bin/python
import os
if os.getenv('DB','MySQL')=='MySQL':
	import MySQLdb as db
else:
	import sqlite3 as db

def get_conn(**kwargs):
	if os.getenv('DB','MySQL')=='MySQL':
		return db.connect(host=kwargs.get('host','localhost'),
			user=kwargs.get('user'),
			passwd=kwargs.get('passwd'),
			port=kwargs.get('port',3306),
			db=kwargs.get('db'))
	else:
		return db.connect(database=kwargs.get('db'))

def main():
	conn = get_conn(host='127.0.0.1',
			user='root',
			passwd='li123..',
			port=3306,
			db='test')

	cur = conn.cursor()
	cur.execute("select * from student")
	print(cur.fetchall())

	cur.close()
	conn.close()

if __name__=='__main__':
	main()
