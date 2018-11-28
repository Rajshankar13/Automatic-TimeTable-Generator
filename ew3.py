from tkinter import Tk,Label,Button,Entry,Frame,StringVar,IntVar
import sqlite3 as sql
import random

A = []
om1 = []
ot1 = []
ow1 = []
oth1 = [] 
of1 = []
om2 = []
ot2 = []
ow2 = []
oth2 = [] 
of2 = []
om3 = []
ot3 = []
ow3 = []
oth3 = [] 
of3 = []
om4 = []
ot4 = []
ow4 = []
oth4 = [] 
of4 = []
copy = []
record1 = []
record2 = []
n1 = []
dec = []
count = 0
flag = 0
monday = []
monday1 = []
monday2 = []
tuesday = []
tuesday1 = []
tuesday2 = []
wednesday = []
wednesday1 = []
wednesday2 = []
thursday = []
thursday1 = []
thursday2 = []
friday = []
friday1 = []
friday2 = []
y1 = []
y2 = []
y3 = []
y4 = []

conn = sql.connect('timetable2.db')

def db():
	with conn:
		s = sname.get()
		st = staff.get()
		h1 = int(h.get())
		d1 = d.get()
		yr = y.get()
		cur = conn.cursor()
		cur.execute("INSERT INTO INFO2 VALUES (?, ?, ?, ?, ?);", (s, st, h1, d1, yr))
		print("Added Successfully!")

def show():
	cur = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO2")
	for row in cur:
		print("Subject:",row[0],"Staff:",row[1],"NOH:",row[2],"T/P:",row[3],"Year:",row[4])

def delete():
	conn.execute("DELETE FROM INFO2;")
	print("Deletion Successful!")

global sname,staff,h,d,y

def pr(list):
	for i in list:
		print(i)

def pri():
	crs = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO2")
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
		else:
			y4.append(records)
	
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y1:
			u[5] = 0
		while((count < 2) & (count > -1)):
			record1 = random.choice(y1)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if(k == 0):
					om1.append(record1)
					monday.append(record1[1])
					record1[5]+=1
				elif(k == 1):
					ot1.append(record1)
					tuesday.append(record1[1])
					record1[5]+=1
				elif(k == 2):
					ow1.append(record1)
					wednesday.append(record1[1])
					record1[5]+=1
				elif(k == 3):
					oth1.append(record1)
					thursday.append(record1[1])
					record1[5]+=1
				else:
					of1.append(record1)
					friday.append(record1[1])
					record1[5]+=1
				copy.append(record1)
				record1[2]-=1
				count+=1

		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y1)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				while(record2[3] != "P"):
					record2 = random.choice(y1)
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if(k == 0):
						monday.append(record2[1])
						monday.append(record2[1])
						om1.append(record2)
						om1.append(record2)
					elif(k == 1):
						tuesday.append(record2[1])
						tuesday.append(record2[1])
						ot1.append(record2)
						ot1.append(record2)
					elif(k == 2):
						wednesday.append(record2[1])
						wednesday.append(record2[1])
						ow1.append(record2)
						ow1.append(record2)
					elif(k == 3):
						thursday.append(record2[1])
						thursday.append(record2[1])
						oth1.append(record2)
						oth1.append(record2)
					else:
						friday.append(record2[1])
						friday.append(record2[1])
						of1.append(record2)
						of1.append(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
					copy.append(record2)
					if(k == 0):
						monday.append(record2[1])
						om1.append(record2)
						record1[5]+=1
					elif(k == 1):
						tuesday.append(record2[1])
						ot1.append(record2)
						record1[5]+=1
					elif(k == 2):
						wednesday.append(record2[1])
						ow1.append(record2)
						record1[5]+=1
					elif(k == 3):
						thursday.append(record2[1])
						oth1.append(record2)
						record1[5]+=1
					else:
						friday.append(record2[1])
						of1.append(record2)
						record1[5]+=1
					count+=1
					record2[2]-=1

#		print("----------------------------------")

	pr(om1)
	print("------------------------------------------")
	pr(ot1)
	print("------------------------------------------")
	pr(ow1)
	print("------------------------------------------")
	pr(oth1)
	print("------------------------------------------")
	pr(of1)
	print("------------------------------------------")
		
	for r in om1:
		t = []
		q = []
		if(r[5] >= 2):
			q = ot1[1]
			if((q[1] != r[1]) & (q[5] <= 1 in om1) & (r[5] <= 1 in ot1)):
				t = q
				q = r
				r = t

#----------------------------------------------------------------------------------------------------------------------

	print("--------------------------------------------------")
	
'''	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y2:
			u[5] = 0
		while((count < 2) & (count > -1)):
			record1 = random.choice(y2)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday[count])):
					om2.append(record1)
					monday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1					
				elif((k == 1) & (record1[1] != tuesday[count])):
					ot2.append(record1)
					tuesday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday[count])):
					ow2.append(record1)
					wednesday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday[count])):
					oth2.append(record1)
					thursday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday[count])):
					of2.append(record1)
					friday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
	
		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y2)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				while(record2[3] != "P"):
					record2 = random.choice(y1)
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2])):
						om2.append(record2)
						om2.append(record2)
						monday1.append(record2[1])
						monday1.append(record2[1])
					elif((k == 1) & (record2[1] != tuesday[count+2])):
						ot2.append(record2)
						ot2.append(record2)
						tuesday1.append(record2[1])
						tuesday1.append(record2[1])
					elif((k == 2) & (record2[1] != wednesday[count+2])):
						ow2.append(record2)
						ow2.append(record2)
						wednesday1.append(record2[1])
						wednesday1.append(record2[1])
					elif((k == 3) & (record2[0] != thursday[count+2])):
						oth2.append(record2)
						oth2.append(record2)
						thursday1.append(record2[1])
						thursday1.append(record2[1])
					elif((k == 4) & (record2[1] != friday[count+2])):
						of2.append(record2)
						of2.append(record2)
						friday1.append(record2[1])
						friday1.append(record2[1])
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2])):
						om2.append(record2)
						monday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 1) & (record2[1] != tuesday[count+2])):
						ot2.append(record2)
						tuesday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 2) & (record2[1] != wednesday[count+2])):
						ow2.append(record2)
						wednesday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 3) & (record2[1] != thursday[count+2])):
						oth2.append(record2)
						thursday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 4) & (record2[1] != friday[count+2])):
						of2.append(record2)
						friday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1

		print("--------------------------------")

#-----------------------------------------------------------------------------------------------------------------

	print("--------------------------------------------------")
	
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y3:
			u[5] = 0
		while((count < 2) & (count > -1)):
			record1 = random.choice(y3)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday[count]) & (record1[1] != monday1[count])):
					om3.append(record1)
					monday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1					
				elif((k == 1) & (record1[1] != tuesday[count]) & (record1[1] != tuesday1[count])):
					ot3.append(record1)
					tuesday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday[count]) & (record1[1] != wednesday1[count])):
					ow3.append(record1)
					wednesday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday[count]) & (record1[1] != thursday1[count])):
					oth3.append(record1)
					thursday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday[count]) & (record1[1] != friday1[count])):
					of3.append(record1)
					friday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
	
		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y3)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				while(record2[3] != "P"):
					record2 = random.choice(y1)
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2])):
						om3.append(record2)
						om3.append(record2)
						monday2.append(record2[1])
						monday2.append(record2[1])
					elif((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2])):
						ot3.append(record2)
						ot3.append(record2)
						tuesday2.append(record2[1])
						tuesday2.append(record2[1])
					elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2])):
						ow3.append(record2)
						ow3.append(record2)
						wednesday2.append(record2[1])
						wednesday2.append(record2[1])
					elif((k == 3) & (record2[1] != thursday[count+2]) & (record2[1] != thursday1[count+2])):
						oth3.append(record2)
						oth3.append(record2)
						thursday2.append(record2[1])
						thursday2.append(record2[1])
					elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2])):
						of3.append(record2)
						of3.append(record2)
						friday2.append(record2[1])
						friday2.append(record2[1])
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2])):
						om3.append(record2)
						monday2.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2])):
						ot3.append(record2)
						tuesday2.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2])):
						ow3.append(record2)
						wednesday2.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 3) & (record2[1] != thursday[count+2]) & (record2[1] != thursday1[count+2])):
						oth3.append(record2)
						thursday2.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2])):
						of3.append(record2)
						friday2.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1

		print("--------------------------------")

#-----------------------------------------------------------------------------------------------------------------

	print("--------------------------------------------------")
	
	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y4:
			u[5] = 0
		while((count < 2) & (count > -1)):
			record1 = random.choice(y4)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday[count]) & (record1[1] != monday1[count]) & (record1[1] != monday2[count])):
					om4.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1					
				elif((k == 1) & (record1[1] != tuesday[count]) & (record1[1] != tuesday1[count]) & (record1[1] != tuesday2[count])):
					ot4.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday[count]) & (record1[1] != wednesday1[count]) & (record1[1] != wednesday2[count])):
					ow4.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday[count]) & (record1[1] != thursday1[count]) & (record1[1] != thursday2[count])):
					oth4.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday[count]) & (record1[1] != friday1[count]) & (record1[1] != friday2[count])):
					of4.append(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
	
		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y4)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				while(record2[3] != "P"):
					record2 = random.choice(y1)
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2]) & (record2[1] != monday2[count+2])):
						om4.append(record2)
						om4.append(record2)
					elif((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2]) & (record2[1] != tuesday2[count+2])):
						ot4.append(record2)
						ot4,append(record2)
					elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2]) & (record2[1] != wednesday2[count+2])):
						ow4.append(record2)
						ow4.append(record2)
					elif((k == 3) & (record2[1] != thursday[count+2]) & (record2[1] != thursday1[count+2]) & (record2[1] != thursday2[count+2])):
						oth4.append(record2)
						oth4.append(record2)
					elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2]) & (record2[1] != friday2[count+2])):
						of4.append(record2)
						of4.append(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday[count+2]) & (record2[1] != monday1[count+2]) & (record2[1] != monday2[count+2])):
						om4.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 1) & (record2[1] != tuesday[count+2]) & (record2[1] != tuesday1[count+2]) & (record2[1] != tuesday2[count+2])):
						ot4.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 2) & (record2[1] != wednesday[count+2]) & (record2[1] != wednesday1[count+2]) & (record2[1] != wednesday2[count+2])):
						ow4.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 3) & (record2[1] != thursday[count+2]) & (record2[1] != thursday1[count+2]) & (record2[1] != thursday2[count+2])):
						oth4.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 4) & (record2[1] != friday[count+2]) & (record2[1] != friday1[count+2]) & (record2[1] != friday2[count+2])):
						of4.append(record2)
						record2[5]+=1
						count+=1
						record2[2]-=1

		print("--------------------------------")

#-----------------------------------------------------------------------------------------------------------------
'''

		
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