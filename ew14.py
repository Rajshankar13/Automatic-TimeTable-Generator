from tkinter import Tk,Label,Button,Entry,Frame,StringVar,IntVar
import sqlite3 as sql
import random
import pdb

A = []
copy = []
record1 = []
record2 = []
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
y1, y1p = [], []
y2, y2p = [], []
y3, y3p = [], []

conn = sql.connect('timetable4.db')

def db():
	with conn:
		s = sname.get()
		st = staff.get()
		h1 = int(h.get())
		d1 = d.get()
		yr = y.get()
		cur = conn.cursor()
		cur.execute("INSERT INTO INFO4 VALUES (?, ?, ?, ?, ?);", (s, st, h1, d1, yr))
		print("Added Successfully!")

def show():
	cur = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO4")
	for row in cur:
		print("Subject:",row[0],"Staff:",row[1],"NOH:",row[2],"T/P:",row[3],"Year:",row[4])

def delete():
	conn.execute("DELETE FROM INFO4;")
	print("Deletion Successful!")

global sname,staff,h,d,y

def pri():
	crs = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO4")
	for row in crs:
		n = row[0]
		s = row[1]
		h = row[2]
		d = row[3]
		ya = row[4]
		t = 0
		records = [n,s,h,d,ya,t]
		if(ya == 1):
			if(d == "T"):
				y1.append(records)
			else:
				y1p.append(records)
		elif(ya == 2):
			if(d == "T"):
				y2.append(records)
			else:
				y2p.append(records)
		elif(ya == 3):
			if(d == "T"):
				y3.append(records)
			else:
				y3p.append(records)
			
	for k in range(0,4):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y3:
			u[5] = 0

		while((count < 2) & (count >= 0)):
			record1 = random.choice(y3)
			if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				print(record1)
				record1[5]+=1
				if(k == 0):
					monday.append(record1[1])
				elif(k == 1):
					tuesday.append(record1[1])
				elif(k == 2):
					wednesday.append(record1[1])
				elif(k == 3):
					thursday.append(record1[1])
				copy.append(record1)
				record1[2]-=1
				count+=1

		count = 0
		while((count < 3) & (count >= 0)):
			record2 = random.choice(y3)	
			if((record2[2] > 0) & (count != 3) & (record2[5] != 2)):
				print(record2)
				record2[5]+=1
				if(k == 0):
					monday.append(record2[1])
				elif(k == 1):
					tuesday.append(record2[1])
				elif(k == 2):
					wednesday.append(record2[1])
				elif(k == 3):
					thursday.append(record2[1])
				copy.append(record2)
				record2[2]-=1
				count+=1
		count = 0
		flag = 0
		while((count < 2) & (count >= 0)):
			if(k == 0):
				monday.append(y3p[0][1])
				monday.append(y3p[1][1])
				monday.append(y3p[2][1])
				monday.append(y3p[3][1])
				print("B1 :",y3p[0])
				print("B2 :",y3p[1])
				print("B3 :",y3p[2])
				print("B4 :",y3p[3])
			elif(k == 1):
				tuesday.append(y3p[1][1])
				tuesday.append(y3p[2][1])
				tuesday.append(y3p[3][1])
				tuesday.append(y3p[0][1])
				print("B1 :",y3p[1])
				print("B2 :",y3p[2])
				print("B3 :",y3p[3])
				print("B4 :",y3p[0])
			elif(k == 2):
				wednesday.append(y3p[2][1])
				wednesday.append(y3p[3][1])
				wednesday.append(y3p[0][1])
				wednesday.append(y3p[1][1])
				print("B1 :",y3p[2])
				print("B2 :",y3p[3])
				print("B3 :",y3p[0])
				print("B4 :",y3p[1])
			elif(k == 3):
				thursday.append(y3p[3][1])
				thursday.append(y3p[0][1])
				thursday.append(y3p[1][1])
				thursday.append(y3p[2][1])
				print("B1 :",y3p[3])
				print("B2 :",y3p[0])
				print("B3 :",y3p[1])
				print("B4 :",y3p[2])
			count+=2
		print("----------------------------------")
	while(len(friday) < 10):
		friday.append("13")
		
#============================================================================================================================
	print("==========================================================")
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y2:
			u[5] = 0

		if(k != 4):
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y2)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 0) & (record1[1] != monday[count])):
						monday1.append(record1[1])
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 1) & (record1[1] != tuesday[count])):
						tuesday1.append(record1[1])
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 2) & (record1[1] != wednesday[count])):
						wednesday1.append(record1[1])
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 3) & (record1[1] != thursday[count])):
						thursday1.append(record1[1])
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1

			count = 0
			while((count < 3) & (count >= 0)):
				record2 = random.choice(y2)	
				if((record2[2] > 0) & (count != 3) & (record2[5] != 2)):
					if((k == 0) & (record2[1] != monday[count + 2])):
						monday1.append(record2[1])
						print(record2)
						record2[5]+=1
						copy.append(record2)
						record2[2]-=1
						count+=1
					elif((k == 1) & (record2[1] != tuesday[count + 2])):
						tuesday1.append(record2[1])
						print(record2)
						record2[5]+=1
						copy.append(record2)
						record2[2]-=1
						count+=1
					elif((k == 2) & (record2[1] != wednesday[count + 2])):
						wednesday1.append(record2[1])
						print(record2)
						record2[5]+=1
						copy.append(record2)
						record2[2]-=1
						count+=1
					elif((k == 3) & (record2[1] != thursday[count + 2])):
						thursday1.append(record2[1])
						print(record2)
						record2[5]+=1
						copy.append(record2)
						record2[2]-=1
						count+=1
			count = 0
			flag = 0
			while((count < 2) & (count >= 0)):
				if(k == 0):
					if(y2p[0][1] != monday[5]):
						monday1.append(y2p[0][1])
						print("B1 :",y2p[0])
					if(y2p[1][1] != monday[6]): 
						monday1.append(y2p[1][1])
						print("B2 :",y2p[1])
					if(y2p[2][1] != monday[7]):
						monday1.append(y2p[2][1])
						print("B3 :",y2p[2])
					if(y2p[3][1] != monday[8]):
						monday1.append(y2p[3][1])
						print("B4 :",y2p[3])
				elif(k == 1):
					if(y2p[4][1] != tuesday[5]):
						tuesday1.append(y2p[4][1])
						print("B1 :",y2p[4])
					if(y2p[0][1] != tuesday[6]): 
						tuesday1.append(y2p[0][1])
						print("B2 :",y2p[0])
					if(y2p[1][1] != tuesday[7]):
						tuesday1.append(y2p[1][1])
						print("B3 :",y2p[1])
					if(y2p[2][1] != tuesday[8]):
						tuesday1.append(y2p[2][1])
						print("B4 :",y2p[2])
				elif(k == 2):
					if(y2p[3][1] != wednesday[5]):
						wednesday1.append(y2p[3][1])
						print("B1 :",y2p[3])
					if(y2p[4][1] != wednesday[6]): 
						wednesday1.append(y2p[4][1])
						print("B2 :",y2p[4])
					if(y2p[0][1] != wednesday[7]):
						wednesday1.append(y2p[0][1])
						print("B3 :",y2p[0])
					if(y2p[1][1] != wednesday[8]):
						wednesday1.append(y2p[1][1])
						print("B4 :",y2p[1])
				elif(k == 3):
					if(y2p[2][1] != thursday[5]):
						thursday1.append(y2p[2][1])
						print("B1 :",y2p[2])
					if(y2p[3][1] != thursday[6]): 
						thursday1.append(y2p[3][1])
						print("B2 :",y2p[3])
					if(y2p[4][1] != thursday[7]):
						thursday1.append(y2p[4][1])
						print("B3 :",y2p[4])
					if(y2p[0][1] != thursday[8]):
						thursday1.append(y2p[0][1])
						print("B4 :",y2p[0])
				count+=2
		else:
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y2)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 4) & (record1[1] != friday[count])):
						friday1.append(record1[1])
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1

			count = 0
			while((count < 2) & (count >= 0)):
				record2 = random.choice(y2)	
				if((record2[2] > 0) & (count != 2) & (record2[5] != 2)):
					if((k == 4) & (record2[1] != friday[count + 2])):
						friday1.append(record2[1])
						print(record2)
						record2[5]+=1
						copy.append(record2)
						record2[2]-=1
						count+=1
			count = 0
			flag = 0
			if(k == 4):
				if(y2p[1][1] != friday[5]):
					friday1.append(y2p[1][1])
					print("B1 :",y2p[1])
				if(y2p[2][1] != friday[6]): 
					friday1.append(y2p[2][1])
					print("B2 :",y2p[2])
				if(y2p[3][1] != friday[7]):
					friday1.append(y2p[3][1])
					print("B3 :",y2p[3])
				if(y2p[4][1] != friday[8]):
					friday1.append(y2p[4][1])
					print("B4 :",y2p[4])
			
		print("----------------------------------")
#============================================================================================================================
	print("==========================================================")
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y1:
			u[5] = 0

		if(k != 4):
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 0) & (record1[1] != monday[count]) & (record1[1] != monday1[count])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 1) & (record1[1] != tuesday[count]) & (record1[1] != tuesday1[count])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 2) & (record1[1] != wednesday[count]) & (record1[1] != wednesday1[count])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 3) & (record1[1] != thursday[count]) & (record1[1] != thursday1[count])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
			count = 0
			while((count < 2) & (count >= 0)):
				if((k == 0) & (y1p[0][1] != monday[2]) & (y1p[0][1] != monday[3]) & (y1p[0][1] != monday1[2]) & (y1p[0][1] != monday1[3]) & (y1p[1][1] != monday[2]) & (y1p[1][1] != monday[3]) & (y1p[1][1] != monday1[2]) & (y1p[1][1] != monday1[3]) & (y1p[2][1] != monday[2]) & (y1p[2][1] != monday[3]) & (y1p[2][1] != monday1[2]) & (y1p[2][1] != monday1[3])):
					print("B1 :",y1p[0])
					print("B2 :",y1p[1])
					print("B3 :",y1p[2])
				elif((k == 1) & (y1p[0][1] != tuesday[2]) & (y1p[0][1] != tuesday[3]) & (y1p[0][1] != tuesday1[2]) & (y1p[0][1] != tuesday1[3]) & (y1p[1][1] != tuesday[2]) & (y1p[1][1] != tuesday[3]) & (y1p[1][1] != tuesday1[2]) & (y1p[1][1] != tuesday1[3]) & (y1p[2][1] != tuesday[2]) & (y1p[2][1] != tuesday[3]) & (y1p[2][1] != tuesday1[2]) & (y1p[2][1] != tuesday1[3])):
					print("B1 :",y1p[3])
					print("B2 :",y1p[0])
					print("B3 :",y1p[1])
				elif((k == 2) & (y1p[0][1] != wednesday[2]) & (y1p[0][1] != wednesday[3]) & (y1p[0][1] != wednesday1[2]) & (y1p[0][1] != wednesday1[3]) & (y1p[1][1] != wednesday[2]) & (y1p[1][1] != wednesday[3]) & (y1p[1][1] != wednesday1[2]) & (y1p[1][1] != wednesday1[3]) & (y1p[2][1] != wednesday[2]) & (y1p[2][1] != wednesday[3]) & (y1p[2][1] != wednesday1[2]) & (y1p[2][1] != wednesday1[3])):
					print("B1 :",y1p[2])
					print("B2 :",y1p[3])
					print("B3 :",y1p[0])
				elif((k == 3) & (y1p[0][1] != thursday[2]) & (y1p[0][1] != thursday[3]) & (y1p[0][1] != thursday1[2]) & (y1p[0][1] != thursday1[3]) & (y1p[1][1] != thursday[2]) & (y1p[1][1] != thursday[3]) & (y1p[1][1] != thursday1[2]) & (y1p[1][1] != thursday1[3]) & (y1p[2][1] != thursday[2]) & (y1p[2][1] != thursday[3]) & (y1p[2][1] != thursday1[2]) & (y1p[2][1] != thursday1[3])):
					print("B1 :",y1p[1])
					print("B2 :",y1p[2])
					print("B3 :",y1p[3])
				count+=2
			count = 0
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 0) & (record1[1] != monday[4]) & (record1[1] != monday1[4]) & (record1[1] != monday[5]) & (record1[1] != monday1[5]) & (record1[1] != monday[6]) & (record1[1] != monday1[6]) & (record1[1] != monday[7]) & (record1[1] != monday1[7]) & (record1[1] != monday[8]) & (record1[1] != monday1[8])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 1) & (record1[1] != tuesday[4]) & (record1[1] != tuesday1[4]) & (record1[1] != tuesday[5]) & (record1[1] != tuesday1[5]) & (record1[1] != tuesday[6]) & (record1[1] != tuesday1[6]) & (record1[1] != tuesday[7]) & (record1[1] != tuesday1[7]) & (record1[1] != tuesday[8]) & (record1[1] != tuesday1[8])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 2) & (record1[1] != wednesday[4]) & (record1[1] != wednesday1[4]) & (record1[1] != wednesday[5]) & (record1[1] != wednesday1[5]) & (record1[1] != wednesday[6]) & (record1[1] != wednesday1[6]) & (record1[1] != wednesday[7]) & (record1[1] != wednesday1[7]) & (record1[1] != wednesday[8]) & (record1[1] != wednesday1[8])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 3) & (record1[1] != thursday[4]) & (record1[1] != thursday1[4]) & (record1[1] != thursday[5]) & (record1[1] != thursday1[5]) & (record1[1] != thursday[6]) & (record1[1] != thursday1[6]) & (record1[1] != thursday[7]) & (record1[1] != thursday1[7]) & (record1[1] != thursday[8]) & (record1[1] != thursday1[8])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1

		else:
			count = 0
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 4) & (record1[1] != friday[count]) & (record1[1] != friday1[count])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
			count = 0
			while((count < 2) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 4) & (record1[1] != friday[count+2]) & (record1[1] != friday1[count+2])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
			count = 0
			while((count < 3) & (count >= 0)):
				record1 = random.choice(y1)
				if((record1[2] > 0) & (count != 3) & (record1[5] != 2)):
					if((k == 4) & (record1[1] != friday[count+4]) & (record1[1] != friday1[count+4])):
						print(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
		print("-----------------------------")
	
						
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