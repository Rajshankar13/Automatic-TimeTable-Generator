from tkinter import Tk,Button,Frame,Label,Entry,Toplevel

class One():
	def __init__(self,master):
		self.master = master
		self.master.geometry('400x200+100+200')
		self.master.title("Add Details")
		
		self.b1 = Button(self.master,fg='red',bg='pink',text="Add Subject",command=self.goTwo).grid(row=0, column=2)
		self.b2 = Button(self.master,fg='red',bg='pink',text="Add Staff",command=self.goThree).grid(row=2, column=2)
		
	def goTwo(self):
		root2 = Toplevel(self.master)
		myGUI1 = Two(root2)
		#self.master.destroy()
		
	def goThree(self):
		root3 = Toplevel(self.master)
		myGUI2 = Three(root3)
		#self.master.destroy()
		
class Two():
	def __init__(self,master):
		self.master = master
		self.master.geometry('400x200+100+200')
		self.master.title("Subject Details")
		
		self.l1 = Label(self.master,fg='pink',text="Subject Name").grid(row=0,column=0)
		self.e1 = Entry(self.master).grid(row=0,column=2)
		self.l2 = Label(self.master,fg='pink',text="Subject Code").grid(row=2,column=0)
		self.e1 = Entry(self.master).grid(row=2,column=2)
		self.b1 = Button(self.master,fg='red',bg='pink',text='Add',command=self.goTwoT).grid(row=4,column=2)
		#self.master.destroy()
		
	def goTwoT(self):
		root4 = Toplevel(self.master)
		myGUI3 = TwoT(root4)
	
	
		
class Three():
	def __init__(self,master):
		self.master = master
		self.master.geometry('400x200+100+200')
		self.master.title("Staff Details")
		
		self.l1 = Label(self.master,fg='pink',text="Staff Name").grid(row=0,column=0)
		self.e1 = Entry(self.master).grid(row=0,column=2)
		self.l2 = Label(self.master,fg='pink',text="Staff ID").grid(row=2,column=0)
		self.e1 = Entry(self.master).grid(row=2,column=2)
		self.b1 = Button(self.master,fg='red',bg='pink',text='Add',command=self.goThreeT).grid(row=4,column=2)
		
		
	def goThreeT(self):
		root5 = Toplevel(self.master)
		myGUI4 = TwoT(root5)
		#data = self.e1.get()
		print(data)

		#self.master.destroy()

class TwoT():
	def __init__(self,master):
		self.master = master
		self.master.geometry('200x200+50+100')
		self.master.title('Acknowlegement')
	
		self.l1 = Label(self.master, fg='pink', text="Subject Added Successfully!").grid(row=2,column=2)
		self.b1 = Button(self.master,fg='red',bg='pink',text="Okay",command=self.goTwo).grid(row=4,column=2)
	
	def goTwo(self):
		root6 = Toplevel(self.master)
		myGUI5 = One(root6)

class ThreeT():
	def __init__(self,master):
		self.master = master
		self.master.geometry('200x200+50+100')
		self.master.title('Acknowlegement')
	
		self.l1 = Label(self.master, fg='pink', text="Staff Added Successfully!").grid(row=2,column=2)
		self.b1 = Button(self.master,fg='red',bg='pink',text="Okay",command=self.goThree).grid(row=4,column=2)
	
	def goThree(self):
		root7 = Toplevel(self.master)
		myGUI6 = One(root7)

def main():
	
	root=Tk();
	myGUIOne=One(root)
	root.mainloop()
	

main()