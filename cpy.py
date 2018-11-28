import random
A = []
copy = []
record1 = []
record2 = []
n1 = []
count = 0
flag = 0
n = int(input("Enter number of Subjects "))
for i in range(0,n):
	n = input("Name of the Faculty:	")
	n1.append(n)
	s = input("Subject taught:	")
	h = int(input("Number of hours alloted for the subject: "))
	t = input("Theory or Practical:	")
	records = [n,s,h,t]
	A.append(records)
	
for k in range(0,5):
	count=0
	record1 = []
	record2 = []
	copy = []
	for i in range(0,20):
		record1 = random.choice(A)
		if((record1[3] == "t" or record1[3] == "T") & (record1[2] > 0) & (count != 2)):
			print(record1)
			copy.append(record1)
			record1[2]-=1
			count+=1

	count = 0
	flag = 0
	for i in range(0,50):
		record2 = random.choice(A)
		if((record2 not in copy) & (count != 4)):
			#copy.append(record2)
			if((record2[3] == "p" or record2[3] == "P") & (flag == 0) & (record2[2] > 0) &((count == 0) or (count == 2))):
				copy.append(record2)
				print(record2)
				print(record2)
				count+=2
				flag = 1
				record2[2]-=2
			elif((record2[3] == "t" or record2[3] == "T") & (record2[2] > 0)):
				copy.append(record2)
				print(record2)
				count+=1
				record2[2]-=1
			
	print("---------------------")