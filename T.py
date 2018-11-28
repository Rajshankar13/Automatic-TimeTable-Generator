from tkinter import Tk,Entry

root = Tk()

str1 = "R"
str2 = "A"
e1 = Entry(root)
e1.pack()
e1.insert(1, str1)
e1.insert(10, "%s" %str2)

root.mainloop()