import random
A = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
y1 = []
y2 = []
y3 = []
y4 = []
copy = []
record1 = []
record2 = []
n1 = []
count = 0
flag = 0
n = int(input("Enter number of Subjects "))
#print("Hello")
for i in range(0,n):
	n = input("Name of the Faculty:	")
	n1.append(n)
	s = input("Subject taught:	")
	h = int(input("Number of hours alloted for the subject: "))
	t = input("Theory or Practical:	")
	y = int(input("Year: "))
	records = [n,s,h,t,y]
	if(y == 1):
		y1.append(records)
	elif(y == 2):
		y2.append(records)
	elif(y == 3):
		y3.append(records)
	else:
		y4.append(records)
	A.append(records)

'''print(A)
print(y1)
print(y2)
print(y3)
print(y4)'''

#-------------------------------------------------------------------------------------------------------------
for k in range(0,5):
	count=0
	record1 = []
	record2 = []
	copy = []
	for i in range(0,300):
		record1 = random.choice(y1)
		if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2)):
			print(record1)
			if(k == 0):
				monday.append(record1[0])
			elif(k == 1):
				tuesday.append(record1[0])
			elif(k == 2):
				wednesday.append(record1[0])
			elif(k == 3):
				thursday.append(record1[0])
			else:
				friday.append(record1[0])
			copy.append(record1)
			record1[2]-=1
			count+=1

	count = 0
	flag = 0
	for i in range(0,3000):
		record2 = random.choice(y1)
		if((record2 not in copy) & (count != 4)):
			#copy.append(record2)
			if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) & ((count == 0) or (count == 2))):
				copy.append(record2)
				if(k == 0):
					monday.append(record2[0])
					monday.append(record2[0])
				elif(k == 1):
					tuesday.append(record2[0])
					tuesday.append(record2[0])
				elif(k == 2):
					wednesday.append(record2[0])
					wednesday.append(record2[0])
				elif(k == 3):
					thursday.append(record2[0])
					thursday.append(record2[0])
				else:
					friday.append(record2[0])
					friday.append(record2[0])
				print(record2)
				print(record2)
				count+=2
				flag = 1
				record2[2]-=2
			elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
				copy.append(record2)
				print(record2)
				if(k == 0):
					monday.append(record2[0])
				elif(k == 1):
					tuesday.append(record2[0])
				elif(k == 2):
					wednesday.append(record2[0])
				elif(k == 3):
					thursday.append(record2[0])
				else:
					friday.append(record2[0])				
				count+=1
				record2[2]-=1
	else:
		if((count < 4) & (record2[2] > 0)):
			print(record2)
			if(k == 0):
				monday.append(record2[0])
			elif(k == 1):
				tuesday.append(record2[0])
			elif(k == 2):
				wednesday.append(record2[0])
			elif(k == 3):
				thursday.append(record2[0])
			else:
				friday.append(record2[0])
			record2[2]-=1	
			count+=1
		
	print("---------------------")

	
while(len(monday) < 6):
	monday.append("13")
while(len(tuesday) < 6):
	tuesday.append("13")
while(len(wednesday) < 6):
	wednesday.append("13")
while(len(thursday) < 6):
	thursday.append("13")
while(len(friday) < 6):
	friday.append("13")

#----------------------------------------------------------------------------------------------------------------------

print("--------------------------------------------------")
for k in range(1,6):
	count=0
	record1 = []
	record2 = []
	copy = []
	for i in range(0,300):
		record1 = random.choice(y2)
		if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2)):
			#print(record1)
			if((k == 1) & (record1[0] != monday[count])):
				print(record1)
			elif((k == 2) & (record1[0] != tuesday[count])):
				print(record1)
			elif((k == 3) & (record1[0] != wednesday[count])):
				print(record1)
			elif((k == 4) & (record1[0] != thursday[count])):
				print(record1)
			elif((k == 5) & (record1[0] != friday[count])):
				print(record1)
			copy.append(record1)
			record1[2]-=1
			count+=1

	count = 0
	flag = 0
	for i in range(0,3000):
		record2 = random.choice(y2)
		if((record2 not in copy) & (count != 4)):
			#copy.append(record2)
			if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2))):
				copy.append(record2)
				if((k == 1) & (record2[0] != monday[count+2])):
					print(record2)
					print(record2)
				elif((k == 2) & (record2[0] != tuesday[count+2])):
					print(record2)
					print(record2)
				elif((k == 3) & (record2[0] != wednesday[count+2])):
					print(record2)
					print(record2)
				elif((k == 4) & (record2[0] != thursday[count+2])):
					print(record2)
					print(record2)
				elif((k == 5) & (record2[0] != friday[count+2])):
					print(record2)
					print(record2)
				count+=2
				flag = 1
				record2[2]-=2
			elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
				copy.append(record2)
				if((k == 1) & (record2[0] != monday[count+2])):
					print(record2)
				elif((k == 2) & (record2[0] != tuesday[count+2])):
					print(record2)
				elif((k == 3) & (record2[0] != wednesday[count+2])):
					print(record2)
				elif((k == 4) & (record2[0] != thursday[count+2])):
					print(record2)
				elif((k == 5) & (record2[0] != friday[count+2])):
					print(record2)
				count+=1
				record2[2]-=1
	else:
		if((count < 4) & (record2[2] > 0)):
			#print(record2)
			if((k == 1) & (record2[0] != monday[count+2])):
				print(record2)
			elif((k == 2) & (record2[0] != tuesday[count+2])):
				print(record2)
			elif((k == 3) & (record2[0] != wednesday[count+2])):
				print(record2)
			elif((k == 4) & (record2[0] != thursday[count+2])):
				print(record2)
			elif((k == 5) & (record2[0] != friday[count+2])):
				print(record2)
			record2[2]-=1	
			count+=1
		
	print("---------------------")
