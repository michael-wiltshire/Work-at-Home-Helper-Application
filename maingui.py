from tkinter import *

root = Tk()

e = Entry(root)
e.pack()

def Buttonpress():
	mylabel = Label(root, text = "look its a button")
	mylabel.pack()

mybutton = Button(root, text = "Click Me!", command=Buttonpress)
mybutton.pack()

root.mainloop()