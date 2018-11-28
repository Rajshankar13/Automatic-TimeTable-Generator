import sqlite3

conn = sqlite3.connect('timetable3.db')
conn.execute('''CREATE TABLE INFO5
			(SUBJECTNAME	CHAR(50)	NOT NULL,
			STAFFNAME	CHAR(50)	NOT NULL,
			NOH	INT	NOT NULL,
			DEC	CHAR(1) NOT NULL,
			YEAR INT NOT NULL);''')

conn.close()
