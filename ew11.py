from tkinter import Tk,Label,Button,Entry,Frame,StringVar,IntVar
import sqlite3 as sql
import random
import pdb

A = []
copy, copyb1, copyb2, copyb3 = [], [], [], [] 
record1 = []
record2 = []
record3 = []
record4 = []
dec = []
count = 0
flag = 0
monday = []
monday1 = []
tuesday = []
tuesday1 = []
wednesday = []
wednesday1 = []
thursday = []
thursday1 = []
friday = []
friday1 = []
y1 = []
y2 = []
y3 = []

conn = sql.connect('timetable3.db')

def db():
	with conn:
		s = sname.get()
		st = staff.get()
		h1 = int(h.get())
		d1 = d.get()
		yr = y.get()
		cur = conn.cursor()
		cur.execute("INSERT INTO INFO5 VALUES (?, ?, ?, ?, ?);", (s, st, h1, d1, yr))
		print("Added Successfully!")

def show():
	cur = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO5")
	for row in cur:
		print("Subject:",row[0],"Staff:",row[1],"NOH:",row[2],"T/P:",row[3],"Year:",row[4])

def delete():
	conn.execute("DELETE FROM INFO5;")
	print("Deletion Successful!")

global sname,staff,h,d,y

def pri():
	crs = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO5")
	for row in crs:
		n = row[0]
		s = row[1]
		h = row[2]
		d = row[3]
		ya = row[4]
		t = 0
		records = [n,s,h,d,ya,t]
		if(ya == 1):
			y1.append(records)
		elif(ya == 2):
			y2.append(records)
		elif(ya == 3):
			y3.append(records)
			
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y1:
			u[5] = 0

		if((k == 0) or (k == 1) or (k == 2) or (k == 4)):
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					print(record1)
					record1[5]+=1
					if(k == 0):
						monday.append(record1[1])
					elif(k == 1):
						tuesday.append(record1[1])
					elif(k == 2):
						wednesday.append(record1[1])
					elif(k == 4):
						friday.append(record1[1])
					copy.append(record1)
					record1[2]-=1
					count+=1

			count = 0
			flag = 0
			while((count < 4) & (count >= 0)):
				record2 = random.choice(y1)
				if((count < 4)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
						copy.append(record2)
						if((k == 0)):
							for r in range(0,3):
								if((r == 0) & (record2[0] not in copyb1) & (record2[0] not in copyb2) & (record2[0] not in copyb3)):
									print("B1 :",record2[0])
									copyb1.append(record2[0])
									record2[2]-=2
									monday.append(record2[1])
									monday.append(record2[1])
								record3 = random.choice(y1)
								while((record3[3] != "P") & (record3[2] > 0) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									record3 = random.choice(y1)
								if((r == 1)):
									print("B2 :",record3[0])
									copyb2.append(record3[0])
									record3[2]-=2
									monday.append(record3[1])
									monday.append(record3[1])
								record4 = random.choice(y1)
								while((record4[3] != "P") & (record4[2] > 0)):
									record4 = random.choice(y1)
								if((r == 2) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									print("B3 :",record4[0])
									copyb3.append(record4[0])
									record4[2]-=2
									monday.append(record4[1])
									monday.append(record4[1])
						elif(k == 1):
							for r in range(0,3):
								if((r == 0) & (record2[0] not in copyb1) & (record2[0] not in copyb2) & (record2[0] not in copyb3)):
									print("B1 :",record2[0])
									copyb1.append(record2[0])
									record2[2]-=2
									monday.append(record2[1])
									monday.append(record2[1])
								record3 = random.choice(y1)
								while((record3[3] != "P") & (record3[2] > 0) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									record3 = random.choice(y1)
								if((r == 1)):
									print("B2 :",record3[0])
									copyb2.append(record3[0])
									record3[2]-=2
									monday.append(record3[1])
									monday.append(record3[1])
								record4 = random.choice(y1)
								while((record4[3] != "P") & (record4[2] > 0)):
									record4 = random.choice(y1)
								if((r == 2) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									print("B3 :",record4[0])
									copyb3.append(record4[0])
									record4[2]-=2
									monday.append(record4[1])
									monday.append(record4[1])
						elif(k == 2):
							for r in range(0,3):
								if((r == 0) & (record2[0] not in copyb1) & (record2[0] not in copyb2) & (record2[0] not in copyb3)):
									print("B1 :",record2[0])
									copyb1.append(record2[0])
									record2[2]-=2
									monday.append(record2[1])
									monday.append(record2[1])
								record3 = random.choice(y1)
								while((record3[3] != "P") & (record3[2] > 0) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									record3 = random.choice(y1)
								if((r == 1)):
									print("B2 :",record3[0])
									copyb2.append(record3[0])
									record3[2]-=2
									monday.append(record3[1])
									monday.append(record3[1])
								record4 = random.choice(y1)
								while((record4[3] != "P") & (record4[2] > 0)):
									record4 = random.choice(y1)
								if((r == 2) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									print("B3 :",record4[0])
									copyb3.append(record4[0])
									record4[2]-=2
									monday.append(record4[1])
									monday.append(record4[1])
						elif(k == 4):
							for r in range(0,3):
								if((r == 0) & (record2[0] not in copyb1) & (record2[0] not in copyb2) & (record2[0] not in copyb3)):
									print("B1 :",record2[0])
									copyb1.append(record2[0])
									record2[2]-=2
									monday.append(record2[1])
									monday.append(record2[1])
								record3 = random.choice(y1)
								while((record3[3] != "P") & (record3[2] > 0) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									record3 = random.choice(y1)
								if((r == 1)):
									print("B2 :",record3[0])
									copyb2.append(record3[0])
									record3[2]-=2
									monday.append(record3[1])
									monday.append(record3[1])
								record4 = random.choice(y1)
								while((record4[3] != "P") & (record4[2] > 0)):
									record4 = random.choice(y1)
								if((r == 2) & (record3[0] not in copyb1) & (record3[0] not in copyb2) & (record3[0] not in copyb3)):
									print("B3 :",record4[0])
									copyb3.append(record4[0])
									record4[2]-=2
									monday.append(record4[1])
									monday.append(record4[1])
						count+=2
						flag = 1
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						print(record2)
						record2[5]+=1
						if(k == 0):
							monday.append(record2[1])
						elif(k == 1):
							tuesday.append(record2[1])
						elif(k == 2):
							wednesday.append(record2[1])
						elif(k == 4):
							friday.append(record2[1])
						count+=1
						record2[2]-=1
			print("----------------------------------")
		elif(1):
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					print(record1)
					record1[5]+=1
					thursday.append(record1[1])
					copy.append(record1)
					record1[2]-=1
					count+=1

			count = 0
			flag = 0
			while((count < 5) & (count >= 0)):
				record2 = random.choice(y1)
				if((record2[3] != "P") & (count == 3) & (flag == 0)):
					while(record2[3] != "P"):
						record2 = random.choice(y1)
				if((count < 5)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 3)) & (record2 not in copy)):
						copy.append(record2)
						thursday.append(record2[1])
						thursday.append(record2[1])
						print(record2)
						print(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						print(record2)
						record2[5]+=1
						thursday.append(record2[1])
						count+=1
						record2[2]-=1
			print("----------------------------------")
	while(len(monday) < 7):
		monday.append("13")
	while(len(tuesday) < 7):
		tuesday.append("13")
	while(len(wednesday) < 7):
		wednesday.append("13")
	while(len(thursday) < 7):
		thursday.append("13")
	while(len(friday) < 7):
		friday.append("13")
#============================================================================================================================

root = Tk()
root.title("TT")
root.geometry("500x200+100+200")

frame = Frame(root, height=720, width=720, bd=4)
frame.grid()
sname = StringVar()
l1 = Label(frame, text="Enter Subject name:-")
l1.grid(row=0, column=0, sticky="e")
e1 = Entry(frame, textvariable=sname)
e1.grid(row=0, column=1)
staff = StringVar() 
l2 = Label(frame, text="Enter Staff name:-")
l2.grid(row=1, column=0, sticky="e")
e2 = Entry(frame, textvariable=staff)
e2.grid(row=1, column=1)
h = IntVar()
l3 = Label(frame, text="Enter Number of hours:-")
l3.grid(row=2, column=0, sticky="e")
e3 = Entry(frame, textvariable=h)
e3.grid(row=2, column=1)
d = StringVar()
l4 = Label(frame, text="Theory/Practical:-")
l4.grid(row=3, column=0, sticky="e")
e4 = Entry(frame, textvariable=d)
e4.grid(row=3, column=1)
y = IntVar()
l5 = Label(frame, text="Year:-")
l5.grid(row=4, column=0, sticky="e")
e5 = Entry(frame, textvariable=y)
e5.grid(row=4, column=1)

b1 = Button(frame, text="Add", command=db)
b1.grid(row=5, column=0)
b2 = Button(frame, text="Show", command=show)
b2.grid(row=5, column=1)
b3 = Button(frame, text="Delete DB", command=delete)
b3.grid(row=6, column=0)
b4 = Button(frame, text="Print", command=pri)
b4.grid(row=6, column=1)

root.mainloop()		