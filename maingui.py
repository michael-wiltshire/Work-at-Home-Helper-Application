from tkinter import *


HEIGHT = 800
WIDTH = 600
root = Tk()
root.title("WorkAtHomeHelper")
root.geometry("600x800")

f=("Times", 20)
#Date Options
def Submit_Date():
	Submitbutton = Label(root, text=clicked.get())
	Submitbutton.pack()

B_HEIGHT = 5
B_WIDTH = 15
mylabel = Label(root, text = "test")
myabel = grid(row=0, column = 0)

#--------------------------BUTTONS-----------------
Preview = Button(root, text="Preview Module", command = Submit_Date,height=B_HEIGHT, width=B_WIDTH)
Preview.grid(row=0, column = 0)
Time_manager = Button(root, text="Time Manager", command = Submit_Date,height=B_HEIGHT, width=B_WIDTH)
Time_manager.grid(row=0, column = 1)
Start_time = Button(root, text="Export ", command = Submit_Date, height=B_HEIGHT, width=B_WIDTH)
Start_time.grid(row=1, column = 0)
End_time = Button(root, text="Submit", command = Submit_Date, height=B_HEIGHT, width=B_WIDTH)
End_time.grid(row=1, column = 1)
"""
Months = ["01", "02", "03", "04", "05", "06", "07", "08", "09","10", "11", "12"]
Hours = []

#canvas = Canvas(root,height = HEIGHT, width = WIDTH)
#canvas.pack()


#frame = Frame(root, bg = '#80c1ff')
#frame.place(relx = 0.1, rely=0.1, relwidth=0.8, relheight=0.8)

clicked = StringVar()
clicked.set(Months[0])

drop = OptionMenu(root, clicked, *Months, command= Submit_Date)
drop.grid(row=1, column = 0, pady=(100,0))

min_sb = Spinbox(
    root,
    from_=0,
    to=23,
    width=2,
    font=f,
    )

sec_hour = Spinbox(
    root,
    from_=0,
    to=59,
    font=f,
    width=2, 
    )
sec = Spinbox(
    root,
    from_=0,
    to=59,
    width=2,
    font=f,
    )

#FOR ENTERING THE TIME
colon_1 = Label(root, text = ":", font = (f,20))
colon_2 = Label(root, text = ":", font = (f,20))
min_sb.grid(row =  3,column = 1, padx = (400,0))
colon_1.grid(row =  3,column = 2)
sec_hour.grid(row = 3,column = 3)
colon_2.grid(row =  3,column = 4)
sec.grid(row = 3,column = 5)




mybutton = Button(root, text="Submit", command = Submit_Date)
mybutton.grid(row = 8, column = 1)

"""
"""
clicked = StringVar()
clicked.set(Months[0])

drop = OptionMenu(root, clicked, *Months, command= Submit_Date)
drop.place(relx = 0.1, rely=0.05)

mybutton = Button(root, text="Submit", command = Submit_Date)
mybutton.place(relx = 0.1, rely=0.1)
"""



#enter a time menu







#frame = Frame(root, bg = '#80c1ff')
#frame.place(relx = 0.1, rely=0.1, relwidth=0.8, relheight=0.8)


"""
e = Entry(root, width = 35, borderwidth= 5)
e.grid(row =0, column=0, columnspan=3,padx=10,pady=10)


def button_add(number):
	return


button_1 = Button(root, text="1",padx=40, pady=20, command=button_add)
button_2 = Button(root, text="2",padx=40, pady=20, command=button_add)
button_3 = Button(root, text="3",padx=40, pady=20, command=button_add)
button_4 = Button(root, text="4",padx=40, pady=20, command=button_add)
button_5 = Button(root, text="5",padx=40, pady=20, command=button_add)
button_6 = Button(root, text="6",padx=40, pady=20, command=button_add)
button_7 = Button(root, text="7",padx=40, pady=20, command=button_add)
button_8 = Button(root, text="8",padx=40, pady=20, command=button_add)
button_9 = Button(root, text="9",padx=40, pady=20, command=button_add)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
"""
"""
def Buttonpress():
	mylabel = Label(root, text = e.get())
	mylabel.pack()
"""
#mybutton = Button(root, text = "Submit", command=Buttonpress)
#mybutton.pack()

root.mainloop()
"""

min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
    )
sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
    )

sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
    )
    """