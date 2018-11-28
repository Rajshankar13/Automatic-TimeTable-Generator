from tkinter import Tk,Label,Button,Entry,Frame,StringVar,IntVar,Toplevel
import sqlite3 as sql
import random

root = Tk()
A = []
copy = []
record1 = []
record2 = []
n1 = []
count = 0
flag = 0
y1 = []
y2 = []
y3 = []
y4 = []
monday0 = []
monday1 = []
monday2 = []
tuesday0 = []
tuesday1 = []
tuesday2 = []
wednesday0 = []
wednesday1 = []
wednesday2 = []
thursday0 = []
thursday1 = []
thursday2 = []
friday0 = []
friday1 = []
friday2 = []

conn = sql.connect('timetable2.db')

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
cntm4=0
cntt4=0
cntw4=0
cntth4=0
cntf4=0

def db():
	with conn:
		s = sname.get()
		st = staff.get()
		h1 = int(h.get())
		d1 = d.get()
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

def monday(record1):
	global cntm
	if(cntm == 0):
		m1.insert(0, record1[0])
		cntm+=1
	elif(cntm == 1):
		m2.insert(0, record1[0])
		cntm+=1
	elif(cntm == 2):
		m3.insert(0, record1[0])
		cntm+=1
	elif(cntm == 3):
		m4.insert(0, record1[0])
		cntm+=1
	elif(cntm == 4):
		m5.insert(0, record1[0])
		cntm+=1
	else:
		m6.insert(0, record1[0])
def mondayy2(record1):
	global cntm2
	if(cntm2 == 0):
		m12.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 1):
		m22.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 2):
		m32.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 3):
		m42.insert(0, record1[0])
		cntm2+=1
	elif(cntm2 == 4):
		m52.insert(0, record1[0])
		cntm2+=1
	else:
		m6.insert(0, record1[0])
def mondayy3(record1):
	global cntm3
	if(cntm3 == 0):
		m13.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 1):
		m23.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 2):
		m33.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 3):
		m43.insert(0, record1[0])
		cntm3+=1
	elif(cntm3 == 4):
		m53.insert(0, record1[0])
		cntm3+=1
	else:
		m63.insert(0, record1[0])
def mondayy4(record1):
	global cntm4
	if(cntm4 == 0):
		m14.insert(0, record1[0])
		cntm4+=1
	elif(cntm4 == 1):
		m24.insert(0, record1[0])
		cntm4+=1
	elif(cntm4 == 2):
		m34.insert(0, record1[0])
		cntm4+=1
	elif(cntm4 == 3):
		m44.insert(0, record1[0])
		cntm4+=1
	elif(cntm4 == 4):
		m54.insert(0, record1[0])
		cntm4+=1
	else:
		m64.insert(0, record1[0])

def tuesday(record1):
	global cntt
	if(cntt == 0):
		t1.insert(0, record1[0])
		cntt+=1
	elif(cntt == 1):
		t2.insert(0, record1[0])
		cntt+=1
	elif(cntt == 2):
		t3.insert(0, record1[0])
		cntt+=1
	elif(cntt == 3):
		t4.insert(0, record1[0])
		cntt+=1
	elif(cntt == 4):
		t5.insert(0, record1[0])
		cntt+=1
	else:
		t6.insert(0, record1[0])
def tuesdayy2(record1):
	global cntt2
	if(cntt2 == 0):
		t12.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 1):
		t22.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 2):
		t32.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 3):
		t42.insert(0, record1[0])
		cntt2+=1
	elif(cntt2 == 4):
		t52.insert(0, record1[0])
		cntt2+=1
	else:
		t62.insert(0, record1[0])
def tuesdayy3(record1):
	global cntt3
	if(cntt3 == 0):
		t13.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 1):
		t23.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 2):
		t33.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 3):
		t43.insert(0, record1[0])
		cntt3+=1
	elif(cntt3 == 4):
		t53.insert(0, record1[0])
		cntt3+=1
	else:
		t63.insert(0, record1[0])
def tuesdayy4(record1):
	global cntt4
	if(cntt4 == 0):
		t14.insert(0, record1[0])
		cntt4+=1
	elif(cntt4 == 1):
		t24.insert(0, record1[0])
		cntt4+=1
	elif(cntt4 == 2):
		t34.insert(0, record1[0])
		cntt4+=1
	elif(cntt4 == 3):
		t44.insert(0, record1[0])
		cntt4+=1
	elif(cntt4 == 4):
		t54.insert(0, record1[0])
		cntt4+=1
	else:
		t64.insert(0, record1[0])

		
def wednesday(record1):
	global cntw
	if(cntw == 0):
		w1.insert(0, record1[0])
		cntw+=1
	elif(cntw == 1):
		w2.insert(0, record1[0])
		cntw+=1
	elif(cntw == 2):
		w3.insert(0, record1[0])
		cntw+=1
	elif(cntw == 3):
		w4.insert(0, record1[0])
		cntw+=1
	elif(cntw == 4):
		w5.insert(0, record1[0])
		cntw+=1
	else:
		w6.insert(0, record1[0])
def wednesdayy2(record1):
	global cntw2
	if(cntw2 == 0):
		w12.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 1):
		w22.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 2):
		w32.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 3):
		w42.insert(0, record1[0])
		cntw2+=1
	elif(cntw2 == 4):
		w52.insert(0, record1[0])
		cntw2+=1
	else:
		w62.insert(0, record1[0])
def wednesdayy3(record1):
	global cntw3
	if(cntw3 == 0):
		w13.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 1):
		w23.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 2):
		w33.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 3):
		w43.insert(0, record1[0])
		cntw3+=1
	elif(cntw3 == 4):
		w53.insert(0, record1[0])
		cntw3+=1
	else:
		w63.insert(0, record1[0])
def wednesdayy4(record1):
	global cntw4
	if(cntw4 == 0):
		w14.insert(0, record1[0])
		cntw4+=1
	elif(cntw4 == 1):
		w24.insert(0, record1[0])
		cntw4+=1
	elif(cntw4 == 2):
		w34.insert(0, record1[0])
		cntw4+=1
	elif(cntw4 == 3):
		w44.insert(0, record1[0])
		cntw4+=1
	elif(cntw4 == 4):
		w54.insert(0, record1[0])
		cntw4+=1
	else:
		w64.insert(0, record1[0])

		
def thursday(record1):
	global cntth
	if(cntth == 0):
		th1.insert(0, record1[0])
		cntth+=1
	elif(cntth == 1):
		th2.insert(0, record1[0])
		cntth+=1
	elif(cntth == 2):
		th3.insert(0, record1[0])
		cntth+=1
	elif(cntth == 3):
		th4.insert(0, record1[0])
		cntth+=1
	elif(cntth == 4):
		th5.insert(0, record1[0])
		cntth+=1
	else:
		th6.insert(0, record1[0])
def thursdayy2(record1):
	global cntth2
	if(cntth2 == 0):
		th12.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 1):
		th22.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 2):
		th32.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 3):
		th42.insert(0, record1[0])
		cntth2+=1
	elif(cntth2 == 4):
		th52.insert(0, record1[0])
		cntth2+=1
	else:
		th62.insert(0, record1[0])
def thursdayy3(record1):
	global cntth3
	if(cntth3 == 0):
		th13.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 1):
		th23.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 2):
		th33.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 3):
		th43.insert(0, record1[0])
		cntth3+=1
	elif(cntth3 == 4):
		th53.insert(0, record1[0])
		cntth3+=1
	else:
		th63.insert(0, record1[0])
def thursdayy4(record1):
	global cntth4
	if(cntth4 == 0):
		th14.insert(0, record1[0])
		cntth4+=1
	elif(cntth4 == 1):
		th24.insert(0, record1[0])
		cntth4+=1
	elif(cntth4 == 2):
		th34.insert(0, record1[0])
		cntth4+=1
	elif(cntth4 == 3):
		th44.insert(0, record1[0])
		cntth4+=1
	elif(cntth4 == 4):
		th54.insert(0, record1[0])
		cntth4+=1
	else:
		th64.insert(0, record1[0])

		
def friday(record1):
	global cntf
	if(cntf == 0):
		f1.insert(0, record1[0])
		cntf+=1
	elif(cntf == 1):
		f2.insert(0, record1[0])
		cntf+=1
	elif(cntf == 2):
		f3.insert(0, record1[0])
		cntf+=1
	elif(cntf == 3):
		f4.insert(0, record1[0])
		cntf+=1
	elif(cntf == 4):
		f5.insert(0, record1[0])
		cntf+=1
	else:
		f6.insert(0, record1[0])
def fridayy2(record1):
	global cntf2
	if(cntf2 == 0):
		f12.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 1):
		f22.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 2):
		f32.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 3):
		f42.insert(0, record1[0])
		cntf2+=1
	elif(cntf2 == 4):
		f52.insert(0, record1[0])
		cntf2+=1
	else:
		f62.insert(0, record1[0])
def fridayy3(record1):
	global cntf3
	if(cntf3 == 0):
		f13.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 1):
		f23.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 2):
		f33.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 3):
		f43.insert(0, record1[0])
		cntf3+=1
	elif(cntf3 == 4):
		f53.insert(0, record1[0])
		cntf3+=1
	else:
		f63.insert(0, record1[0])
def fridayy4(record1):
	global cntf4
	if(cntf4 == 0):
		f14.insert(0, record1[0])
		cntf4+=1
	elif(cntf4 == 1):
		f24.insert(0, record1[0])
		cntf4+=1
	elif(cntf4 == 2):
		f34.insert(0, record1[0])
		cntf4+=1
	elif(cntf4 == 3):
		f44.insert(0, record1[0])
		cntf4+=1
	elif(cntf4 == 4):
		f54.insert(0, record1[0])
		cntf4+=1
	else:
		f64.insert(0, record1[0])



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
		count=0
		record1 = []
		record2 = []
		copy = []
		for u in y1:
			u[5] = 0		
		while((count < 2) & (count > -1)):
			record1 = random.choice(y1)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				print(record1)
				record1[5]+=1
				if(k == 0):
					monday(record1)
					monday0.append(record1[1])
				elif(k == 1):
					tuesday(record1)
					tuesday0.append(record1[1])
				elif(k == 2):
					wednesday(record1)
					wednesday0.append(record1[1])
				elif(k == 3):
					thursday(record1)
					thursday0.append(record1[1])
				else:
					friday(record1)
					friday0.append(record1[1])
				copy.append(record1)
				record1[2]-=1
				count+=1

		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y1)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				continue			
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if(k == 0):
						monday(record2)
						monday(record2)
						monday0.append(record2[1])
						monday0.append(record2[1])
					elif(k == 1):
						tuesday(record2)
						tuesday(record2)
						tuesday0.append(record2[1])
						tuesday0.append(record2[1])
					elif(k == 2):
						wednesday(record2)
						wednesday(record2)
						wednesday0.append(record2[1])
						wednesday0.append(record2[1])
					elif(k == 3):
						thursday(record2)
						thursday(record2)
						thursday0.append(record2[1])
						thursday0.append(record2[1])
					else:
						friday(record2)
						friday(record2)
						friday0.append(record2[1])
						friday0.append(record2[1])
					print(record2)
					print(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					print(record2)
					record2[5]+=1					
					if(k == 0):
						monday(record2)
						monday0.append(record2[1])
					elif(k == 1):
						tuesday(record2)
						tuesday0.append(record2[1])
					elif(k == 2):
						wednesday(record2)
						wednesday0.append(record2[1])
					elif(k == 3):
						thursday(record2)
						thursday0.append(record2[1])
					else:
						friday(record2)
						friday0.append(record2[1])
					count+=1
					record2[2]-=1
			
		print("---------------------")
	print("==================================================================================================================================")		
#--------------------------------------------------------------------------------------------------------------------------------------------------		

	for k in range(0,5):
		count=0
		record1 = []
		record2 = []
		copy = []
		for u in y2:
			u[5] = 0		
		while((count < 2) & (count > -1)):
			record1 = random.choice(y2)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday0[count])):
					print(record1)
					mondayy2(record1)
					copy.append(record1)
					record1[2]-=1
					record1[5]+=1
					count+=1
					monday1.append(record1[1])
				elif((k == 1) & (record1[1] != tuesday0[count])):
					print(record1)
					tuesdayy2(record1)
					tuesday1.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday0[count])):
					print(record1)
					wednesdayy2(record1)
					wednesday1.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday0[count])):
					print(record1)
					thursdayy2(record1)
					thursday1.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday0[count])):
					print(record1)
					fridayy2(record1)
					friday1.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1

		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y2)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				continue			
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2])):
						mondayy2(record2)
						mondayy2(record2)
						monday1.append(record2[1])
						monday1.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 1) & (record2[1] != tuesday0[count+2])):
						tuesdayy2(record2)
						tuesdayy2(record2)
						tuesday1.append(record2[1])
						tuesday1.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 2) & (record2[1] != wednesday0[count+2])):
						wednesdayy2(record2)
						wednesdayy2(record2)
						wednesday1.append(record2[1])
						wednesday1.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 3) & (record2[1] != thursday0[count+2])):
						thursdayy2(record2)
						thursdayy2(record2)
						thursday1.append(record2[1])
						thursday1.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 4) & (record2[1] != friday0[count+2])):
						fridayy2(record2)
						fridayy2(record2)
						friday1.append(record2[1])
						friday1.append(record2[1])
						print(record2)
						print(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2])):
						print(record2)
						mondayy2(record2)
						monday1.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 1) & (record2[1] != tuesday0[count+2])):
						print(record2)
						tuesdayy2(record2)
						tuesday1.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 2) & (record2[1] != wednesday0[count+2])):
						print(record2)
						wednesdayy2(record2)
						wednesday1.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 3) & (record2[1] != thursday0[count+2])):
						print(record2)
						thursdayy2(record2)
						thursday1.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 4) & (record2[1] != friday0[count+2])):
						print(record2)
						fridayy2(record2)
						friday1.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
			
		print("---------------------")
	print("==================================================================================================================================")		
#---------------------------------------------------------------------------------------------------------------------------------------------

	for k in range(0,5):
		count=0
		record1 = []
		record2 = []
		copy = []
		for u in y3:
			u[5] = 0		
		while((count < 2) & (count > -1)):
			record1 = random.choice(y3)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday0[count]) & (record1[1] != monday1[count])):
					print(record1)
					mondayy3(record1)
					copy.append(record1)
					record1[2]-=1
					record1[5]+=1
					count+=1
					monday2.append(record1[1])
				elif((k == 1) & (record1[1] != tuesday0[count]) & (record1[1] != tuesday1[count])):
					print(record1)
					tuesdayy3(record1)
					tuesday2.append(record1[1])
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday0[count]) & (record1[1] != wednesday1[count])):
					print(record1)
					wednesdayy3(record1)
					wednesday2.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday0[count]) & (record1[1] != thursday1[count])):
					print(record1)
					thursdayy3(record1)
					thursday2.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday0[count]) & (record1[1] != friday1[count])):
					print(record1)
					fridayy3(record1)
					friday2.append(record1[1])
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1

		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y3)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				continue			
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2]) & (record2[1] != monday1[count+2])):
						mondayy3(record2)
						mondayy3(record2)
						monday2.append(record2[1])
						monday2.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 1) & (record2[1] != tuesday0[count+2]) & (record2[1] != tuesday1[count+2])):
						tuesdayy3(record2)
						tuesdayy3(record2)
						tuesday2.append(record2[1])
						tuesday2.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record2[1] != wednesday1[count+2])):
						wednesdayy3(record2)
						wednesdayy3(record2)
						wednesday2.append(record2[1])
						wednesday2.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 3) & (record2[1] != thursday0[count+2]) & (record2[1] != thursday1[count+2])):
						thursdayy3(record2)
						thursdayy3(record2)
						thursday2.append(record2[1])
						thursday2.append(record2[1])
						print(record2)
						print(record2)
					elif((k == 4) & (record2[1] != friday0[count+2]) & (record2[1] != friday1[count+2])):
						fridayy3(record2)
						fridayy3(record2)
						friday2.append(record2[1])
						friday2.append(record2[1])
						print(record2)
						print(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2]) & (record2[1] != monday1[count+2])):
						print(record2)
						mondayy3(record2)
						monday2.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 1) & (record2[1] != tuesday0[count+2]) & (record2[1] != tuesday1[count+2])):
						print(record2)
						tuesdayy3(record2)
						tuesday2.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record2[1] != wednesday1[count+2])):
						print(record2)
						wednesdayy3(record2)
						wednesday2.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 3) & (record2[1] != thursday0[count+2]) & (record2[1] != thursday1[count+2])):
						print(record2)
						thursdayy3(record2)
						thursday2.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 4) & (record2[1] != friday0[count+2]) & (record2[1] != friday1[count+2])):
						print(record2)
						fridayy3(record2)
						friday2.append(record2[1])
						count+=1
						record2[2]-=1
						record2[5]+=1					
			
		print("---------------------")

	print("==================================================================================================================================")		
#-------------------------------------------------------------------------------------------------------------------------------------
	for k in range(0,5):
		count=0
		record1 = []
		record2 = []
		copy = []
		for u in y4:
			u[5] = 0		
		while((count < 2) & (count > -1)):
			record1 = random.choice(y4)
			if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2) & (record1[5] != 2)):
				if((k == 0) & (record1[1] != monday0[count]) & (record1[1] != monday1[count]) & (record1[1] != monday2[count])):
					print(record1)
					mondayy4(record1)
					copy.append(record1)
					record1[2]-=1
					record1[5]+=1
					count+=1
				elif((k == 1) & (record1[1] != tuesday0[count]) & (record1[1] != tuesday1[count]) & (record1[1] != tuesday2[count])):
					print(record1)
					tuesdayy4(record1)
					record1[5]+=1
					copy.append(record1)
					record1[2]-=1
					count+=1
				elif((k == 2) & (record1[1] != wednesday0[count]) & (record1[1] != wednesday1[count]) & (record1[1] != wednesday2[count])):
					print(record1)
					wednesdayy4(record1)
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 3) & (record1[1] != thursday0[count]) & (record1[1] != thursday1[count]) & (record1[1] != thursday2[count])):
					print(record1)
					thursdayy4(record1)
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1
				elif((k == 4) & (record1[1] != friday0[count]) & (record1[1] != friday1[count]) & (record1[1] != friday2[count])):
					print(record1)
					fridayy4(record1)
					copy.append(record1)
					record1[5]+=1
					record1[2]-=1
					count+=1

		count = 0
		flag = 0
		while((count < 4) & (count > -1)):
			record2 = random.choice(y4)
			if((record2[3] != "P") & (count == 2) & (flag == 0)):
				continue			
			if((count < 4)):
				if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2)) & (record2 not in copy)):
					copy.append(record2)
					if((k == 0) & (record1[1] != monday0[count+2]) & (record1[1] != monday1[count+2]) & (record1[1] != monday2[count+2])):
						mondayy4(record2)
						mondayy4(record2)
						print(record2)
						print(record2)
					elif((k == 1) & (record2[1] != tuesday0[count+2]) & (record1[1] != tuesday1[count+2]) & (record1[1] != tuesday2[count+2])):
						tuesdayy4(record2)
						tuesdayy4(record2)
						print(record2)
						print(record2)
					elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record1[1] != wednesday1[count+2]) & (record1[1] != wednesday2[count+2])):
						wednesdayy4(record2)
						wednesdayy4(record2)
						print(record2)
						print(record2)
					elif((k == 3) & (record2[1] != thursday0[count+2]) & (record1[1] != thursday1[count+2]) & (record1[1] != thursday2[count+2])):
						thursdayy4(record2)
						thursdayy4(record2)
						print(record2)
						print(record2)
					elif((k == 4) & (record2[1] != friday0[count+2]) & (record1[1] != friday1[count+2]) & (record1[1] != friday2[count+2])):
						fridayy4(record2)
						fridayy4(record2)
						print(record2)
						print(record2)
					count+=2
					flag = 1
					record2[2]-=2
				elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0) & (record2[5] != 2)):
					copy.append(record2)
					if((k == 0) & (record2[1] != monday0[count+2]) & (record1[1] != monday1[count+2]) & (record1[1] != monday2[count+2])):
						print(record2)
						mondayy4(record2)
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 1) & (record2[1] != tuesday0[count+2]) & (record1[1] != tuesday1[count+2]) & (record1[1] != tuesday2[count+2])):
						print(record2)
						tuesdayy4(record2)
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 2) & (record2[1] != wednesday0[count+2]) & (record1[1] != wednesday1[count+2]) & (record1[1] != wednesday2[count+2])):
						print(record2)
						wednesdayy4(record2)
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 3) & (record2[1] != thursday0[count+2]) & (record1[1] != thursday1[count+2]) & (record1[1] != thursday2[count+2])):
						print(record2)
						thursdayy4(record2)
						count+=1
						record2[2]-=1
						record2[5]+=1					
					elif((k == 4) & (record2[1] != friday0[count+2]) & (record1[1] != friday1[count+2]) & (record1[1] != friday2[count+2])):
						print(record2)
						fridayy4(record2)
						count+=1
						record2[2]-=1
						record2[5]+=1					
			
		print("---------------------")
	print("==================================================================================================================================")		
#-------------------------------------------------------------------------------------------------------------------------------

root.title("TT")

'''frame = Frame(root, height=720, width=720, bd=4)
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
'''
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
m1 = Entry(root)
m1.grid(row=1,column=1)
m2 = Entry(root)
m2.grid(row=2,column=1)
m3 = Entry(root)
m3.grid(row=4,column=1)
m4 = Entry(root)
m4.grid(row=5,column=1)
m5 = Entry(root)
m5.grid(row=7,column=1)
m6 = Entry(root)
m6.grid(row=8,column=1)
#----------TuesdayY1

t1 = Entry(root)
t1.grid(row=1,column=2)
t2 = Entry(root)
t2.grid(row=2,column=2)
t3 = Entry(root)
t3.grid(row=4,column=2)
t4 = Entry(root)
t4.grid(row=5,column=2)
t5 = Entry(root)
t5.grid(row=7,column=2)
t6 = Entry(root)
t6.grid(row=8,column=2)
#-----------WednesdayY1

w1 = Entry(root)
w1.grid(row=1,column=3)
w2 = Entry(root)
w2.grid(row=2,column=3)
w3 = Entry(root)
w3.grid(row=4,column=3)
w4 = Entry(root)
w4.grid(row=5,column=3)
w5 = Entry(root)
w5.grid(row=7,column=3)
w6 = Entry(root)
w6.grid(row=8,column=3)
#-----------ThursdayY1

th1 = Entry(root)
th1.grid(row=1,column=4)
th2 = Entry(root)
th2.grid(row=2,column=4)	
th3 = Entry(root)
th3.grid(row=4,column=4)
th4 = Entry(root)
th4.grid(row=5,column=4)
th5 = Entry(root)
th5.grid(row=7,column=4)
th6 = Entry(root)
th6.grid(row=8,column=4)
#-----------FridayY1

f1 = Entry(root)
f1.grid(row=1,column=5)
f2 = Entry(root)
f2.grid(row=2,column=5)
f3 = Entry(root)
f3.grid(row=4,column=5)
f4 = Entry(root)
f4.grid(row=5,column=5)
f5 = Entry(root)
f5.grid(row=7,column=5)
f6 = Entry(root)
f6.grid(row=8,column=5)

E1 = Entry(root)
E1.grid(row=1,column=0)
E2 = Entry(root)
E2.grid(row=2,column=0)
B1 = Entry(root)
B1.grid(row=3, column=2)
E3 = Entry(root)
E3.grid(row=4,column=0)
E4 = Entry(root)
E4.grid(row=5,column=0)
B2 = Entry(root)
B2.grid(row=6,column=2)
E5 = Entry(root)
E5.grid(row=7,column=0)
E6 = Entry(root)
E6.grid(row=8,column=0)
E7 = Entry(root)
E7.grid(row=9,column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=0, column=2)
e3 = Entry(root)
e3.grid(row=0, column=3)
e4 = Entry(root)
e4.grid(row=0, column=4)
e5 = Entry(root)
e5.grid(row=0, column=5)
fn(E1,E2,B1,E3,E4,B2,E5,E6,E7,e1,e2,e3,e4,e5)
BUT = Button(root, text="Generate", command=pri)
BUT.grid(row=10, column=2)

#------------------------------------------------------------------------------------------------
#---------MondayY2
top2 = Toplevel()
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
t63 = Entry(top3)
t63.grid(row=8,column=2)
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
w63 = Entry(top3)
w63.grid(row=8,column=3)
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
f63 = Entry(top3)
f63.grid(row=8,column=5)

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

#------------------------------------------------------------------------------------------------
#---------MondayY4
top4 = Toplevel()
m14 = Entry(top4)
m14.grid(row=1,column=1)
m24 = Entry(top4)
m24.grid(row=2,column=1)
m34 = Entry(top4)
m34.grid(row=4,column=1)
m44 = Entry(top4)
m44.grid(row=5,column=1)
m54 = Entry(top4)
m54.grid(row=7,column=1)
m64 = Entry(top4)
m64.grid(row=8,column=1)
#----------TuesdayY4

t14 = Entry(top4)
t14.grid(row=1,column=2)
t24 = Entry(top4)
t24.grid(row=2,column=2)
t34 = Entry(top4)
t34.grid(row=4,column=2)
t44 = Entry(top4)
t44.grid(row=5,column=2)
t54 = Entry(top4)
t54.grid(row=7,column=2)
t64 = Entry(top4)
t64.grid(row=8,column=2)
#-----------WednesdayY4

w14 = Entry(top4)
w14.grid(row=1,column=3)
w24 = Entry(top4)
w24.grid(row=2,column=3)
w34 = Entry(top4)
w34.grid(row=4,column=3)
w44 = Entry(top4)
w44.grid(row=5,column=3)
w54 = Entry(top4)
w54.grid(row=7,column=3)
w64 = Entry(top4)
w64.grid(row=8,column=3)
#-----------ThursdayY4

th14 = Entry(top4)
th14.grid(row=1,column=4)
th24 = Entry(top4)
th24.grid(row=2,column=4)	
th34 = Entry(top4)
th34.grid(row=4,column=4)
th44 = Entry(top4)
th44.grid(row=5,column=4)
th54 = Entry(top4)
th54.grid(row=7,column=4)
th64 = Entry(top4)
th64.grid(row=8,column=4)
#-----------FridayY4

f14 = Entry(top4)
f14.grid(row=1,column=5)
f24 = Entry(top4)
f24.grid(row=2,column=5)
f34 = Entry(top4)
f34.grid(row=4,column=5)
f44 = Entry(top4)
f44.grid(row=5,column=5)
f54 = Entry(top4)
f54.grid(row=7,column=5)
f64 = Entry(top4)
f64.grid(row=8,column=5)

E12 = Entry(top4)
E12.grid(row=1,column=0)
E22 = Entry(top4)
E22.grid(row=2,column=0)
B12 = Entry(top4)
B12.grid(row=3, column=2)
E32 = Entry(top4)
E32.grid(row=4,column=0)
E42 = Entry(top4)
E42.grid(row=5,column=0)
B22 = Entry(top4)
B22.grid(row=6,column=2)
E52 = Entry(top4)
E52.grid(row=7,column=0)
E62 = Entry(top4)
E62.grid(row=8,column=0)
E72 = Entry(top4)
E72.grid(row=9,column=0)
e12 = Entry(top4)
e12.grid(row=0, column=1)
e22 = Entry(top4)
e22.grid(row=0, column=2)
e32 = Entry(top4)
e32.grid(row=0, column=3)
e42 = Entry(top4)
e42.grid(row=0, column=4)
e52 = Entry(top4)
e52.grid(row=0, column=5)
fn(E12,E22,B12,E32,E42,B22,E52,E62,E72,e12,e22,e32,e42,e52)

#------------------------------------------------------------------------------------------------
root.mainloop()