from tkinter import Tk,Label,Button,Entry,Frame,StringVar,IntVar,Toplevel
import sqlite3 as sql
import random

root = Tk()
copy = []
record1 = []
record2 = []
count = 0
flag = 0
y1 = []
y2 = []
y3 = []
monday0 = []
monday1 = []
tuesday0 = []
tuesday1 = []
wednesday0 = []
wednesday1 = []
thursday0 = []
thursday1 = []
friday0 = []
friday1 = []

conn = sql.connect('timetable3.db')

cntm=0
cntt=0
cntw=0
cntth=0
cntf=0
cntm2=0
cntt2=0
cntw2=0
cntth2=0
cntf2=0
cntm3=0
cntt3=0
cntw3=0
cntth3=0
cntf3=0

def db():
	with conn:
		s = sname.get()
		st = staff.get()
		h1 = int(h.get())
		d1 = d.get()
		cur = conn.cursor()
		cur.execute("INSERT INTO INFO3 VALUES (?, ?, ?, ?, ?);", (s, st, h1, d1, yr))
		print("Added Successfully!")
		
def show():
	cur = conn.execute("SELECT SUBJECTNAME, STAFFNAME, NOH, DEC, YEAR FROM INFO3")
	for row in cur:
		print("Subject:",row[0],"Staff:",row[1],"NOH:",row[2],"T/P:",row[3],"Year:",row[4])

def delete():
	conn.execute("DELETE FROM INFO2;")
	print("Deletion Successful!")

global sname,staff,h,d,y

def monday(record1):
	global cntm
	if(cntm == 0):
		m1.delete(0, "end")
		m1.insert(0, record1[0])
		cntm+=1
	elif(cntm == 1):
		m2.delete(0, "end")
		m2.insert(0, record1[0])
		cntm+=1
	elif(cntm == 2):
		m3.delete(0, "end")
		m3.insert(0, record1[0])
		cntm+=1
	elif(cntm == 3):
		m4.delete(0, "end")
		m4.insert(0, record1[0])
		cntm+=1
	elif(cntm == 4):
		m5.delete(0, "end")
		m5.insert(0, record1[0])
		cntm+=1
	elif(cntm == 5):
		m6.delete(0, "end")
		m6.insert(0, record1[0])
		cntm+=1
	elif(cntm == 6):
		m7.delete(0, "end")
		m7.insert(0, record1[0])

def mondayy2(record1):
	global cntm2
	if(cntm2 == 0):
		m12.delete(0, "end")
		m12.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 1):
		m22.delete(0, "end")
		m22.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 2):
		m32.delete(0, "end")
		m32.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 3):
		m42.delete(0, "end")
		m42.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 4):
		m52.delete(0, "end")
		m52.insert(0, record1[0])
		cntm2+=1
	else:
		m62.delete(0, "end")
		m62.insert(0, record1[0])

def mondayy3(record1):
	global cntm3
	if(cntm3 == 0):
		m13.delete(0, "end")
		m13.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 1):
		m23.delete(0, "end")
		m23.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 2):
		m33.delete(0, "end")
		m33.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 3):
		m43.delete(0, "end")
		m43.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 4):
		m53.delete(0, "end")
		m53.insert(0, record1[0])
		cntm3+=1
	else:
		m63.delete(0, "end")
		m63.insert(0, record1[0])

def tuesday(record1):
	global cntt
	if(cntt == 0):
		t1.delete(0, "end")
		t1.insert(0, record1[0])
		cntt+=1
	elif(cntt == 1):
		t2.delete(0, "end")
		t2.insert(0, record1[0])
		cntt+=1
	elif(cntt == 2):
		t3.delete(0, "end")
		t3.insert(0, record1[0])
		cntt+=1
	elif(cntt == 3):
		t4.delete(0, "end")
		t4.insert(0, record1[0])
		cntt+=1
	elif(cntt == 4):
		t5.delete(0, "end")
		t5.insert(0, record1[0])
		cntt+=1
	elif(cntt == 5):
		t6.delete(0, "end")
		t6.insert(0, record1[0])
		cntt+=1
	elif(cntt == 6):
		t7.delete(0, "end")
		t7.insert(0, record1[0])

def tuesdayy2(record1):
	global cntt2
	if(cntt2 == 0):
		t12.delete(0, "end")
		t12.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 1):
		t22.delete(0, "end")
		t22.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 2):
		t32.delete(0, "end")
		t32.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 3):
		t42.delete(0, "end")
		t42.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 4):
		t52.delete(0, "end")
		t52.insert(0, record1[0])
		cntt2+=1
	else:
		t62.delete(0, "end")
		t62.insert(0, record1[0])

def tuesdayy3(record1):
	global cntt3
	if(cntt3 == 0):
		t13.delete(0, "end")
		t13.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 1):
		t23.delete(0, "end")
		t23.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 2):
		t33.delete(0, "end")
		t33.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 3):
		t43.delete(0, "end")
		t43.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 4):
		t53.delete(0, "end")
		t53.insert(0, record1[0])
		
def wednesday(record1):
	global cntw
	if(cntw == 0):
		w1.delete(0, "end")
		w1.insert(0, record1[0])
		cntw+=1
	elif(cntw == 1):
		w2.delete(0, "end")
		w2.insert(0, record1[0])
		cntw+=1
	elif(cntw == 2):
		w3.delete(0, "end")
		w3.insert(0, record1[0])
		cntw+=1
	elif(cntw == 3):
		w4.delete(0, "end")
		w4.insert(0, record1[0])
		cntw+=1
	elif(cntw == 4):
		w5.delete(0, "end")
		w5.insert(0, record1[0])
		cntw+=1
	else:
		w6.delete(0, "end")
		w6.insert(0, record1[0])

def wednesdayy2(record1):
	global cntw2
	if(cntw2 == 0):
		w12.delete(0, "end")
		w12.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 1):
		w22.delete(0, "end")
		w22.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 2):
		w32.delete(0, "end")
		w32.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 3):
		w42.delete(0, "end")
		w42.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 4):
		w52.delete(0, "end")
		w52.insert(0, record1[0])
		cntw2+=1
	else:
		w62.delete(0, "end")
		w62.insert(0, record1[0])

def wednesdayy3(record1):
	global cntw3
	if(cntw3 == 0):
		w13.delete(0, "end")
		w13.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 1):
		w23.delete(0, "end")
		w23.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 2):
		w33.delete(0, "end")
		w33.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 3):
		w43.delete(0, "end")
		w43.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 4):
		w53.delete(0, "end")
		w53.insert(0, record1[0])

		
def thursday(record1):
	global cntth
	if(cntth == 0):
		th1.delete(0, "end")
		th1.insert(0, record1[0])
		cntth+=1
	elif(cntth == 1):
		th2.delete(0, "end")
		th2.insert(0, record1[0])
		cntth+=1
	elif(cntth == 2):
		th3.delete(0, "end")
		th3.insert(0, record1[0])
		cntth+=1
	elif(cntth == 3):
		th4.delete(0, "end")
		th4.insert(0, record1[0])
		cntth+=1
	elif(cntth == 4):
		th5.delete(0, "end")
		th5.insert(0, record1[0])
		cntth+=1
	else:
		th6.delete(0, "end")
		th6.insert(0, record1[0])

def thursdayy2(record1):
	global cntth2
	if(cntth2 == 0):
		th12.delete(0, "end")
		th12.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 1):
		th22.delete(0, "end")
		th22.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 2):
		th32.delete(0, "end")
		th32.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 3):
		th42.delete(0, "end")
		th42.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 4):
		th52.delete(0, "end")
		th52.insert(0, record1[0])
		cntth2+=1
	else:
		th62.delete(0, "end")
		th62.insert(0, record1[0])

def thursdayy3(record1):
	global cntth3
	if(cntth3 == 0):
		th13.delete(0, "end")
		th13.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 1):
		th23.delete(0, "end")
		th23.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 2):
		th33.delete(0, "end")
		th33.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 3):
		th43.delete(0, "end")
		th43.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 4):
		th53.delete(0, "end")
		th53.insert(0, record1[0])
		cntth3+=1
	else:
		th63.delete(0, "end")
		th63.insert(0, record1[0])
		
def friday(record1):
	global cntf
	if(cntf == 0):
		f1.delete(0, "end")
		f1.insert(0, record1[0])
		cntf+=1
	elif(cntf == 1):
		f2.delete(0, "end")
		f2.insert(0, record1[0])
		cntf+=1
	elif(cntf == 2):
		f3.delete(0, "end")
		f3.insert(0, record1[0])
		cntf+=1
	elif(cntf == 3):
		f4.delete(0, "end")
		f4.insert(0, record1[0])
		cntf+=1
	elif(cntf == 4):
		f5.delete(0, "end")
		f5.insert(0, record1[0])
		cntf+=1
	elif(cntf == 5):
		f6.delete(0, "end")
		f6.insert(0, record1[0])
		cntf+=1
	elif(cntf == 6):
		f7.delete(0, "end")
		f7.insert(0, record1[0])

def fridayy2(record1):
	global cntf2
	if(cntf2 == 0):
		f12.delete(0, "end")
		f12.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 1):
		f22.delete(0, "end")
		f22.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 2):
		f32.delete(0, "end")
		f32.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 3):
		f42.delete(0, "end")
		f42.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 4):
		f52.delete(0, "end")
		f52.insert(0, record1[0])
		cntf2+=1
	else:
		f62.delete(0, "end")
		f62.insert(0, record1[0])

def fridayy3(record1):
	global cntf3
	if(cntf3 == 0):
		f13.delete(0, "end")
		f13.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 1):
		f23.delete(0, "end")
		f23.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 2):
		f33.delete(0, "end")
		f33.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 3):
		f43.delete(0, "end")
		f43.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 4):
		f53.delete(0, "end")
		f53.insert(0, record1[0])

def pri():
	rm1, rm2, rm3 = [], [], []
	rt1, rt2, rt3 = [], [], []
	rw1, rw2, rw3 = [], [], []
	rth1, rth2, rth3 = [], [], []
	rf1, rf2, rf3 = [], [], []
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
			for i in range(0,300):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					record1[5]+=1
					if(k == 2):
						rw1.append(record1)
						wednesday0.append(record1[1])
					elif(k == 3):
						rth1.append(record1)
						thursday0.append(record1[1])
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
							rw1.append(record2)
							rw1.append(record2)
							wednesday0.append(record2[1])
							wednesday0.append(record2[1])
						elif(k == 3):
							rth1.append(record2)
							rth1.append(record2)
							thursday0.append(record2[1])
							thursday0.append(record2[1])
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						record2[5]+=1
						if(k == 2):
							rw1.append(record2)
							wednesday0.append(record2[1])
						elif(k == 3):
							rth1.append(record2)
							thursday0.append(record2[1])
						count+=1
						record2[2]-=1
		elif(1):
			for i in range(0,300):
				record1 = random.choice(y1)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					record1[5]+=1
					if(k == 0):
						rm1.append(record1)
						monday0.append(record1[1])
					elif(k == 1):
						rt1.append(record1)
						tuesday0.append(record1[1])
					else:
						rf1.append(record1)
						friday0.append(record1[1])
					copy.append(record1)
					record1[2]-=1
					count+=1

			count = 0
			flag = 0
			for i in range(0,3000):
				record2 = random.choice(y1)
				if((record2[3] != "P") & (count == 3) & (flag == 0)):
					while(record2[3] != "P"):
						record2 = random.choice(y1)
				if((count < 5)):
					if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 3)) & (record2 not in copy)):
						copy.append(record2)
						if(k == 0):
							rm1.append(record2)
							rm1.append(record2)
							monday0.append(record2[1])
							monday0.append(record2[1])
						elif(k == 1):
							rt1.append(record2)
							rt1.append(record2)
							tuesday0.append(record2[1])
							tuesday0.append(record2[1])
						else:
							rf1.append(record2)
							rf1.append(record2)
							friday0.append(record2[1])
							friday0.append(record2[1])
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						record2[5]+=1
						if(k == 0):
							rm1.append(record2)
							monday0.append(record2[1])
						elif(k == 1):
							rt1.append(record2)
							tuesday0.append(record2[1])
						else:
							rf1.append(record2)
							friday0.append(record2[1])
						count+=1
						record2[2]-=1
	if(len(rf1) < 7):
		pri()
#============================================================================================================================

	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y2:
			u[5] = 0

		for i in range(0,300):
			record1 = random.choice(y2)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday0[count])):
					rm2.append(record1)
					monday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1					
				elif((k == 1) & (record1[1] != tuesday0[count])):
					rt2.append(record1)
					tuesday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday0[count])):
					rw2.append(record1)
					wednesday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday0[count])):
					rth2.append(record1)
					thursday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday0[count])):
					rf2.append(record1)
					friday1.append(record1[1])
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
					if((k == 0) & (record2[1] != monday0[count+2])):
						rm2.append(record2)
						rm2.append(record2)
						monday1.append(record2[1])
						monday1.append(record2[1])
					elif((k == 1) & (record2[1] != tuesday0[count+2])):
						rt2.append(record2)
						rt2.append(record2)
						tuesday1.append(record2[1])
						tuesday1.append(record2[1])
					elif((k == 2) & (record2[1] != wednesday0[count+2])):
						rw2.append(record2)
						rw2.append(record2)
						wednesday1.append(record2[1])
						wednesday1.append(record2[1])
					elif((k == 3) & (record2[0] != thursday0[count+2])):
						rth2.append(record2)
						rth2.append(record2)
						thursday1.append(record2[1])
						thursday1.append(record2[1])
					elif((k == 4) & (record2[1] != friday0[count+2])):
						rf2.append(record2)
						rf2.append(record2)
						friday1.append(record2[1])
						friday1.append(record2[1])
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2])):
						rm2.append(record2)
						monday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 1) & (record2[1] != tuesday0[count+2])):
						rt2.append(record2)
						tuesday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 2) & (record2[1] != wednesday0[count+2])):
						rw2.append(record2)
						wednesday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 3) & (record2[1] != thursday0[count+2])):
						rth2.append(record2)
						thursday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
					elif((k == 4) & (record2[1] != friday0[count+2])):
						rf2.append(record2)
						friday1.append(record2[1])
						record2[5]+=1
						count+=1
						record2[2]-=1
	if(len(rf2) < 6):
		pri()
		
#---------------------------------------------------------------------------------------------------------------------------------------------

	for k in range(0,5):
		count = 0
		record1 = []
		record2 = []
		copy = []
		for u in y3:
			u[5] = 0
		
		if((k == 0) or (k == 3)):
			for i in range(0,300):
				record1 = random.choice(y3)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 0) & (record1[1] != monday0[count]) & (record1[1] != monday1[count])):
						rm3.append(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1					
					elif((k == 3) & (record1[1] != thursday0[count]) & (record1[1] != thursday1[count])):
						rth3.append(record1)
						record1[5]+=1
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
						if((k == 0) & (record2[1] != monday0[count+2]) & (record2[1] != monday1[count+2])):
							rm3.append(record2)
							rm3.append(record2)
						elif((k == 3) & (record2[0] != thursday0[count+2]) & (record2[0] != thursday1[count+2])):
							rth3.append(record2)
							rth3.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						if((k == 0) & (record2[1] != monday0[count+2]) & (record2[1] != monday1[count+2])):
							rm3.append(record2)
							record2[5]+=1
							count+=1
							record2[2]-=1
						elif((k == 3) & (record2[1] != thursday0[count+2]) & (record2[1] != thursday1[count+2])):
							rth3.append(record2)
							record2[5]+=1
							count+=1
							record2[2]-=1
		elif(1):
			for i in range(0,300):
				record1 = random.choice(y3)
				if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
					if((k == 1) & (record1[1] != tuesday0[count]) & (record1[1] != tuesday1[count])):
						rt3.append(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 2) & (record1[1] != wednesday0[count]) & (record1[1] != wednesday1[count])):
						rw3.append(record1)
						record1[5]+=1
						copy.append(record1)
						record1[2]-=1
						count+=1
					elif((k == 4) & (record1[1] != friday0[count]) & (record1[1] != friday1[count])):
						rf3.append(record1)
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
						if((k == 1) & (record2[1] != tuesday0[count+2]) & (record2[1] != tuesday1[count+2])):
							rt3.append(record2)
							rt3.append(record2)
						elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record2[1] != wednesday1[count+2])):
							rw3.append(record2)
							rw3.append(record2)
						elif((k == 4) & (record2[1] != friday0[count+2]) & (record2[1] != friday1[count+2])):
							rf3.append(record2)
							rf3.append(record2)
						count+=2
						flag = 1
						record2[2]-=2
					elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
						copy.append(record2)
						if((k == 1) & (record2[1] != tuesday0[count+2]) & (record2[1] != tuesday1[count+2])):
							rt3.append(record2)
							record2[5]+=1
							count+=1
							record2[2]-=1
						elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record2[1] != wednesday1[count+2])):
							rw3.append(record2)
							record2[5]+=1
							count+=1
							record2[2]-=1
						elif((k == 4) & (record2[1] != friday0[count+2]) & (record2[1] != friday1[count+2])):
							rf3.append(record2)
							record2[5]+=1
							count+=1
							record2[2]-=1
	if(len(rf3) < 5):
		pri()
	else:
		for m in rm1:
			monday(m)
		for m in rm2:
			mondayy2(m)
		for	m in rm3:
			mondayy3(m)
		for m in rt1:
			tuesday(m)
		for m in rt2:
			tuesdayy2(m)
		for	m in rt3:
			tuesdayy3(m)
		for m in rw1:
			wednesday(m)
		for m in rw2:
			wednesdayy2(m)
		for	m in rw3:
			wednesdayy3(m)
		for m in rth1:
			thursday(m)
		for m in rth2:
			thursdayy2(m)
		for	m in rth3:
			thursdayy3(m)
		for m in rf1:
			friday(m)
		for m in rf2:
			fridayy2(m)
		for	m in rf3:
			fridayy3(m)
		
#-------------------------------------------------------------------------------------------------------------------------------

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

b1 = Button(frame, text="Add", command=db)
b1.grid(row=4, column=0)
b2 = Button(frame, text="Show", command=show)
b2.grid(row=4, column=1)
b3 = Button(frame, text="Delete DB", command=delete)
b3.grid(row=5, column=0)
b4 = Button(frame, text="Print", command=pri)
b4.grid(row=5, column=1)

def fn(E1,E2,B1,E3,E4,B2,E5,E6,E7,e1,e2,e3,e4,e5):
	E1.insert(0,'8:45 to 9:45')
	E2.insert(0,'9:45 to 10:45')
	B1.insert(0,'15 Minute Break')
	E3.insert(0,'11:00 to 12:00')
	E4.insert(0,'12:00 to 1:00')
	B2.insert(0,'30 Minute Break')
	E5.insert(0,'1:30 to 2:30')
	E6.insert(0,'2:30 to 3:30')
	E7.insert(0,'3:30 to 4:30')
	e1.insert(0,'Monday')
	e2.insert(0,'Tuesday')
	e3.insert(0,'Wednesday')
	e4.insert(0,'Thursday')
	e5.insert(0,'Friday')

#---------MondayY1
top1 = Toplevel()
top1.title("Year1")
m1 = Entry(top1)
m1.grid(row=1,column=1)
m2 = Entry(top1)
m2.grid(row=2,column=1)
m3 = Entry(top1)
m3.grid(row=4,column=1)
m4 = Entry(top1)
m4.grid(row=5,column=1)
m5 = Entry(top1)
m5.grid(row=7,column=1)
m6 = Entry(top1)
m6.grid(row=8,column=1)
m7 = Entry(top1)
m7.grid(row=9, column=1)
#----------TuesdayY1

t1 = Entry(top1)
t1.grid(row=1,column=2)
t2 = Entry(top1)
t2.grid(row=2,column=2)
t3 = Entry(top1)
t3.grid(row=4,column=2)
t4 = Entry(top1)
t4.grid(row=5,column=2)
t5 = Entry(top1)
t5.grid(row=7,column=2)
t6 = Entry(top1)
t6.grid(row=8,column=2)
t7 = Entry(top1)
t7.grid(row=9, column=2)
#-----------WednesdayY1

w1 = Entry(top1)
w1.grid(row=1,column=3)
w2 = Entry(top1)
w2.grid(row=2,column=3)
w3 = Entry(top1)
w3.grid(row=4,column=3)
w4 = Entry(top1)
w4.grid(row=5,column=3)
w5 = Entry(top1)
w5.grid(row=7,column=3)
w6 = Entry(top1)
w6.grid(row=8,column=3)
#-----------ThursdayY1

th1 = Entry(top1)
th1.grid(row=1,column=4)
th2 = Entry(top1)
th2.grid(row=2,column=4)	
th3 = Entry(top1)
th3.grid(row=4,column=4)
th4 = Entry(top1)
th4.grid(row=5,column=4)
th5 = Entry(top1)
th5.grid(row=7,column=4)
th6 = Entry(top1)
th6.grid(row=8,column=4)
#-----------FridayY1

f1 = Entry(top1)
f1.grid(row=1,column=5)
f2 = Entry(top1)
f2.grid(row=2,column=5)
f3 = Entry(top1)
f3.grid(row=4,column=5)
f4 = Entry(top1)
f4.grid(row=5,column=5)
f5 = Entry(top1)
f5.grid(row=7,column=5)
f6 = Entry(top1)
f6.grid(row=8,column=5)
f7 = Entry(top1)
f7.grid(row=9, column=5)

E1 = Entry(top1)
E1.grid(row=1,column=0)
E2 = Entry(top1)
E2.grid(row=2,column=0)
B1 = Entry(top1)
B1.grid(row=3, column=2)
E3 = Entry(top1)
E3.grid(row=4,column=0)
E4 = Entry(top1)
E4.grid(row=5,column=0)
B2 = Entry(top1)
B2.grid(row=6,column=2)
E5 = Entry(top1)
E5.grid(row=7,column=0)
E6 = Entry(top1)
E6.grid(row=8,column=0)
E7 = Entry(top1)
E7.grid(row=9,column=0)
e1 = Entry(top1)
e1.grid(row=0, column=1)
e2 = Entry(top1)
e2.grid(row=0, column=2)
e3 = Entry(top1)
e3.grid(row=0, column=3)
e4 = Entry(top1)
e4.grid(row=0, column=4)
e5 = Entry(top1)
e5.grid(row=0, column=5)
fn(E1,E2,B1,E3,E4,B2,E5,E6,E7,e1,e2,e3,e4,e5)
BUT = Button(top1, text="Generate", command=pri)
BUT.grid(row=10, column=2)

#------------------------------------------------------------------------------------------------
#---------MondayY2
top2 = Toplevel()
top2.title("Year2")
m12 = Entry(top2)
m12.grid(row=1,column=1)
m22 = Entry(top2)
m22.grid(row=2,column=1)
m32 = Entry(top2)
m32.grid(row=4,column=1)
m42 = Entry(top2)
m42.grid(row=5,column=1)
m52 = Entry(top2)
m52.grid(row=7,column=1)
m62 = Entry(top2)
m62.grid(row=8,column=1)
#----------TuesdayY2

t12 = Entry(top2)
t12.grid(row=1,column=2)
t22 = Entry(top2)
t22.grid(row=2,column=2)
t32 = Entry(top2)
t32.grid(row=4,column=2)
t42 = Entry(top2)
t42.grid(row=5,column=2)
t52 = Entry(top2)
t52.grid(row=7,column=2)
t62 = Entry(top2)
t62.grid(row=8,column=2)
#-----------WednesdayY2

w12 = Entry(top2)
w12.grid(row=1,column=3)
w22 = Entry(top2)
w22.grid(row=2,column=3)
w32 = Entry(top2)
w32.grid(row=4,column=3)
w42 = Entry(top2)
w42.grid(row=5,column=3)
w52 = Entry(top2)
w52.grid(row=7,column=3)
w62 = Entry(top2)
w62.grid(row=8,column=3)
#-----------ThursdayY2

th12 = Entry(top2)
th12.grid(row=1,column=4)
th22 = Entry(top2)
th22.grid(row=2,column=4)	
th32 = Entry(top2)
th32.grid(row=4,column=4)
th42 = Entry(top2)
th42.grid(row=5,column=4)
th52 = Entry(top2)
th52.grid(row=7,column=4)
th62 = Entry(top2)
th62.grid(row=8,column=4)
#-----------FridayY2

f12 = Entry(top2)
f12.grid(row=1,column=5)
f22 = Entry(top2)
f22.grid(row=2,column=5)
f32 = Entry(top2)
f32.grid(row=4,column=5)
f42 = Entry(top2)
f42.grid(row=5,column=5)
f52 = Entry(top2)
f52.grid(row=7,column=5)
f62 = Entry(top2)
f62.grid(row=8,column=5)

E12 = Entry(top2)
E12.grid(row=1,column=0)
E22 = Entry(top2)
E22.grid(row=2,column=0)
B12 = Entry(top2)
B12.grid(row=3, column=2)
E32 = Entry(top2)
E32.grid(row=4,column=0)
E42 = Entry(top2)
E42.grid(row=5,column=0)
B22 = Entry(top2)
B22.grid(row=6,column=2)
E52 = Entry(top2)
E52.grid(row=7,column=0)
E62 = Entry(top2)
E62.grid(row=8,column=0)
E72 = Entry(top2)
E72.grid(row=9,column=0)
e12 = Entry(top2)
e12.grid(row=0, column=1)
e22 = Entry(top2)
e22.grid(row=0, column=2)
e32 = Entry(top2)
e32.grid(row=0, column=3)
e42 = Entry(top2)
e42.grid(row=0, column=4)
e52 = Entry(top2)
e52.grid(row=0, column=5)
fn(E12,E22,B12,E32,E42,B22,E52,E62,E72,e12,e22,e32,e42,e52)

#------------------------------------------------------------------------------------------------
#---------MondayY3
top3 = Toplevel()
top3.title("Year3")
m13 = Entry(top3)
m13.grid(row=1,column=1)
m23 = Entry(top3)
m23.grid(row=2,column=1)
m33 = Entry(top3)
m33.grid(row=4,column=1)
m43 = Entry(top3)
m43.grid(row=5,column=1)
m53 = Entry(top3)
m53.grid(row=7,column=1)
m63 = Entry(top3)
m63.grid(row=8,column=1)
#----------TuesdayY3

t13 = Entry(top3)
t13.grid(row=1,column=2)
t23 = Entry(top3)
t23.grid(row=2,column=2)
t33 = Entry(top3)
t33.grid(row=4,column=2)
t43 = Entry(top3)
t43.grid(row=5,column=2)
t53 = Entry(top3)
t53.grid(row=7,column=2)
#-----------WednesdayY3

w13 = Entry(top3)
w13.grid(row=1,column=3)
w23 = Entry(top3)
w23.grid(row=2,column=3)
w33 = Entry(top3)
w33.grid(row=4,column=3)
w43 = Entry(top3)
w43.grid(row=5,column=3)
w53 = Entry(top3)
w53.grid(row=7,column=3)
#-----------ThursdayY3

th13 = Entry(top3)
th13.grid(row=1,column=4)
th23 = Entry(top3)
th23.grid(row=2,column=4)	
th33 = Entry(top3)
th33.grid(row=4,column=4)
th43 = Entry(top3)
th43.grid(row=5,column=4)
th53 = Entry(top3)
th53.grid(row=7,column=4)
th63 = Entry(top3)
th63.grid(row=8,column=4)
#-----------FridayY3

f13 = Entry(top3)
f13.grid(row=1,column=5)
f23 = Entry(top3)
f23.grid(row=2,column=5)
f33 = Entry(top3)
f33.grid(row=4,column=5)
f43 = Entry(top3)
f43.grid(row=5,column=5)
f53 = Entry(top3)
f53.grid(row=7,column=5)

E12 = Entry(top3)
E12.grid(row=1,column=0)
E22 = Entry(top3)
E22.grid(row=2,column=0)
B12 = Entry(top3)
B12.grid(row=3, column=2)
E32 = Entry(top3)
E32.grid(row=4,column=0)
E42 = Entry(top3)
E42.grid(row=5,column=0)
B22 = Entry(top3)
B22.grid(row=6,column=2)
E52 = Entry(top3)
E52.grid(row=7,column=0)
E62 = Entry(top3)
E62.grid(row=8,column=0)
E72 = Entry(top3)
E72.grid(row=9,column=0)
e12 = Entry(top3)
e12.grid(row=0, column=1)
e22 = Entry(top3)
e22.grid(row=0, column=2)
e32 = Entry(top3)
e32.grid(row=0, column=3)
e42 = Entry(top3)
e42.grid(row=0, column=4)
e52 = Entry(top3)
e52.grid(row=0, column=5)
fn(E12,E22,B12,E32,E42,B22,E52,E62,E72,e12,e22,e32,e42,e52)

root.mainloop()