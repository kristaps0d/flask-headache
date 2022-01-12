from os import getenv
import sqlite3

def init_database():
	global con

	db_dir = getenv('DATABASE_LOC')
	if db_dir is None:
		raise SystemExit('\nfix(.env)!: missing "DATABASE_LOC"\n')

	con = sqlite3.connect(db_dir)
	cur = con.cursor()

	try:
		cur.execute('''SELECT * FROM rooms''')
	except:
		init_table(con.cursor())

def deinit_database():
	if con is not None:
		con.close()

def init_table(cur):
	cur.execute('''
	CREATE TABLE rooms (
		room_name TEXT,
		room_key TEXT	
	)''')