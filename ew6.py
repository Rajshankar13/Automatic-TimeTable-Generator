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
		cur.execute("INSERT INTO INFO3 VALUES (?, ?, ?, ?, ?);", (s, st, h1, d1, yr))
		print("Added Successfully!")

def show():
	cur = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO3")
	for row in cur:
		print("Subject:",row[0],"Staff:",row[1],"NOH:",row[2],"T/P:",row[3],"Year:",row[4])

def delete():
	conn.execute("DELETE FROM INFO3;")
	print("Deletion Successful!")

global sname,staff,h,d,y

def printf(list):
	for r in list:
		print(r)

def pri():
	mondayy1,mondayy2,mondayy3 = [], [], []
	tuesdayy1,tuesdayy2,tuesdayy3 = [], [], []
	wednesdayy1,wednesdayy2,wednesdayy3 = [], [], []
	thursdayy1,thursdayy2,thursdayy3 = [], [], []
	fridayy1,fridayy2,fridayy3 = [], [], []
	crs = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO3")
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

		if((k == 2) or (k == 3)):
			for i in range(0,100):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					record1[5]+=1
					if(k == 2):
						wednesdayy1.append(record1)
						wednesday.append(record1[1])
					elif(k == 3):
						thursday.append(record1[1])
						thursdayy1.append(record1)
					copy.append(record1)
					record1[2]-=1
					count+=1

			count = 0
			flag = 0
			for i in range(0,3000):
				record2 = random.choice(y1)
				if((record2[3] != "P") & (count == 2) & (flag == 0)):
					while(record2[3] != "P"):
						record2 = random.choice(y1)
				if((count < 4)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
						copy.append(record2)
						if(k == 2):
							wednesday.append(record2[1])
							wednesday.append(record2[1])
							wednesdayy1.append(record2)
							wednesdayy1.append(record2)
						elif(k == 3):
							thursday.append(record2[1])
							thursday.append(record2[1])
							thursdayy1.append(record2)
							thursdayy1.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						record2[5]+=1
						if(k == 2):
							wednesday.append(record2[1])
							wednesdayy1.append(record2)
						elif(k == 3):
							thursday.append(record2[1])
							thursdayy1.append(record2)
						count+=1
						record2[2]-=1
		elif(1):
			for i in range(0,100):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					record1[5]+=1
					if(k == 0):
						monday.append(record1[1])
						mondayy1.append(record1)
					elif(k == 1):
						tuesday.append(record1[1])
						tuesdayy1.append(record1)
					else:
						friday.append(record1[1])
						fridayy1.append(record1)
					copy.append(record1)
					record1[2]-=1
					count+=1

			count = 0
			flag = 0
			for i in range(0,3000):
#				pdb.set_trace()
				record2 = random.choice(y1)
				if((record2[3] != "P") & (count == 3) & (flag == 0)):
					while(record2[3] != "P"):
						record2 = random.choice(y1)
				if((count < 5)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 3)) & (record2 not in copy)):
						copy.append(record2)
						if(k == 0):
							monday.append(record2[1])
							monday.append(record2[1])
							mondayy1.append(record2)
							mondayy1.append(record2)
						elif(k == 1):
							tuesday.append(record2[1])
							tuesday.append(record2[1])
							tuesdayy1.append(record2)
							tuesdayy1.append(record2)
						else:
							friday.append(record2[1])
							friday.append(record2[1])
							fridayy1.append(record2)
							fridayy1.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						record2[5]+=1
						if(k == 0):
							monday.append(record2[1])
							mondayy1.append(record2)
						elif(k == 1):
							tuesday.append(record2[1])
							tuesdayy1.append(record2)
						else:
							friday.append(record2[1])
							fridayy1.append(record2)
						count+=1
						record2[2]-=1
	if(len(fridayy1) < 7):
		mondayy1.clear()
		tuesdayy1.clear()
		wednesdayy1.clear()
		thursdayy1.clear()
		fridayy1.clear()
		pri()
#============================================================================================================================
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y2:
			u[5] = 0

		for i in range(0,100):
			record1 = random.choice(y2)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday[count])):
					monday1.append(record1[1])
					mondayy2.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1					
				elif((k == 1) & (record1[1] != tuesday[count])):
					tuesday1.append(record1[1])
					tuesdayy2.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday[count])):
					wednesday1.append(record1[1])
					wednesdayy2.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday[count])):
					thursday1.append(record1[1])
					thursdayy2.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday[count])):
					friday1.append(record1[1])
					fridayy2.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
	
		count = 0
		flag = 0
		for i in range(0,3000):
			record2 = random.choice(y2)
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2])):
						monday1.append(record2[1])
						monday1.append(record2[1])
						mondayy2.append(record2)
						mondayy2.append(record2)
					elif((k == 1) & (record2[1] != tuesday[count+2])):
						tuesday1.append(record2[1])
						tuesday1.append(record2[1])
						tuesdayy2.append(record2)
						tuesdayy2.append(record2)
					elif((k == 2) & (record2[1] != wednesday[count+2])):
						wednesday1.append(record2[1])
						wednesday1.append(record2[1])
						wednesdayy2.append(record2)
						wednesdayy2.append(record2)
					elif((k == 3) & (record2[0] != thursday[count+2])):
						thursday1.append(record2[1])
						thursday1.append(record2[1])
						thursdayy2.append(record2)
						thursdayy2.append(record2)
					elif((k == 4) & (record2[1] != friday[count+2])):
						friday1.append(record2[1])
						friday1.append(record2[1])
						fridayy2.append(record2)
						fridayy2.append(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2])):
						monday1.append(record2[1])
						mondayy2.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 1) & (record2[1] != tuesday[count+2])):
						tuesday1.append(record2[1])
						tuesdayy2.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 2) & (record2[1] != wednesday[count+2])):
						wednesday1.append(record2[1])
						wednesdayy2.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 3) & (record2[1] != thursday[count+2])):
						thursday1.append(record2[1])
						thursdayy2.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 4) & (record2[1] != friday[count+2])):
						friday1.append(record2[1])
						fridayy2.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
	if(len(fridayy2) < 6):
		mondayy2.clear()
		tuesdayy2.clear()
		wednesdayy2.clear()
		thursdayy2.clear()
		fridayy2.clear()
		pri()
#============================================================================================================================
	
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y3:
			u[5] = 0
		
		if((k == 0) or (k == 3)):
			for i in range(0,100):
				record1 = random.choice(y3)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 0) & (record1[1] != monday[count]) & (record1[1] != monday1[count])):
						record1[5]+=1
						mondayy3.append(record1)
						copy.append(record1)
						record1[2]-=1
						count+=1					
					elif((k == 3) & (record1[1] != thursday[count]) & (record1[1] != thursday1[count])):
						record1[5]+=1
						thursdayy3.append(record1)
						copy.append(record1)
						record1[2]-=1
						count+=1

			count = 0
			flag = 0
			for i in range(0,3000):
				record2 = random.choice(y3)
				if((count < 4)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
						copy.append(record2)
						if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2])):
							mondayy3.append(record2)
							mondayy3.append(record2)
						elif((k == 3) & (record2[0] != thursday[count+2]) & (record2[0] != thursday1[count+2])):
							thursdayy3.append(record2)
							thursdayy3.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2])):
							record2[5]+=1
							mondayy3.append(record2)
							count+=1
							record2[2]-=1
						elif((k == 3) & (record2[1] != thursday[count+2]) & (record2[1] != thursday1[count+2])):
							record2[5]+=1
							thursdayy3.append(record2)
							count+=1
							record2[2]-=1
		elif(1):
			for i in range(0,100):
				record1 = random.choice(y3)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 1) & (record1[1] != tuesday[count]) & (record1[1] != tuesday1[count])):
						record1[5]+=1
						tuesdayy3.append(record1)
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 2) & (record1[1] != wednesday[count]) & (record1[1] != wednesday1[count])):
						record1[5]+=1
						wednesdayy3.append(record1)
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 4) & (record1[1] != friday[count]) & (record1[1] != friday1[count])):
						fridayy3.append(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
	
			count = 0
			flag = 0
			for i in range(0,3000):
				record2 = random.choice(y3)
				if((record2[3] != "P") & (count == 0) & (flag == 0)):
					while(record2[3] != "P"):
						record2 = random.choice(y1)
				if((count < 3)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
						copy.append(record2)
						if((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2])):
							tuesdayy3.append(record2)
							tuesdayy3.append(record2)
						elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2])):
							wednesdayy3.append(record2)
							wednesdayy3.append(record2)
						elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2])):
							fridayy3.append(record2)
							fridayy3.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						if((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2])):
							record2[5]+=1
							tuesdayy3.append(record2)
							count+=1
							record2[2]-=1
						elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2])):
							record2[5]+=1
							wednesdayy3.append(record2)
							count+=1
							record2[2]-=1
						elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2])):
							record2[5]+=1
							fridayy3.append(record2)
							count+=1
							record2[2]-=1
	if(len(fridayy3) < 5):
		mondayy3.clear()
		tuesdayy3.clear()
		wednesdayy3.clear()
		thursdayy3.clear()
		fridayy3.clear()
		pri()
	else:
		print("Hi")
		printf(mondayy1)
		print("---------------------------------------")
		printf(tuesdayy1)
		print("---------------------------------------")
		printf(wednesdayy1)
		print("---------------------------------------")
		printf(thursdayy1)
		print("---------------------------------------")
		printf(fridayy1)
		print("---------------------------------------")
		print("=====================================================================")
		printf(mondayy2)
		print("---------------------------------------")
		printf(tuesdayy2)
		print("---------------------------------------")
		printf(wednesdayy2)
		print("---------------------------------------")
		printf(thursdayy2)
		print("---------------------------------------")
		printf(fridayy2)
		print("---------------------------------------")
		print("=====================================================================")
		printf(mondayy3)
		print("---------------------------------------")
		printf(tuesdayy3)
		print("---------------------------------------")
		printf(wednesdayy3)
		print("---------------------------------------")
		printf(thursdayy3)
		print("---------------------------------------")
		printf(fridayy3)
		print("---------------------------------------")
		print("=====================================================================")
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