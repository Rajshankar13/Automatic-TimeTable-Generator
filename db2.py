import sqlite3
import ew2.py

conn = sqlite3.connect('database1.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC FROM INFO1")
for row in cursor:
   print ("SubjectName = ", row[0])
   print ("StaffName = ", row[1])
   print ("NumberOfHours = ", row[2])
   print ("Theory/Practical = ", row[3], "\n")

#print ("Operation done successfully");
conn.close()