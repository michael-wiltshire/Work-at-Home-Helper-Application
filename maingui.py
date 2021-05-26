"""
CIS 422: Project 2: Work at home helper
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files.
"""

from tkinter import *
import preview
import database.dbm as db
import datetime

root = Tk()
root.title("WorkAtHomeHelper")
root.geometry("800x800")

root.configure(bg='white')

f=("Times", 20) 
#Date Options
#----------------------FRAME ONE OBJECTS--------------------------
#Frame One is how the title is being oriented
Frame1 = Frame(root, width= 800)
Frame1.place(x=0, y=0, height=40, width = 800)

TitleFont =("Times", 30) 
Title = Label(Frame1, text= "WorkAtHomeHelper-V1", font=TitleFont)
Title.place(x=0,y=0)
#----------------------FRAMES TWO OBJECTS--------------------------
# Freame Two is the Time module, and Preview.
F2_Font = ("Times", 20)
F2_background_color = 'white'
F2_preview_label = Label("")
Frame2 = Frame(root, width= 800, bg= F2_background_color)
Frame2.place(x =0,y=40, height=240, width = 800)

F2_preview_label = Label(Frame2, text="Click The Preview Module to Preview and Edit Your Spreadsheet")
F2_Time_label = Label(Frame2, text="Click The Preview Module to Preview and Edit Your Spreadsheet")

B_HEIGHT = 5
B_WIDTH = 15
B_Xvalue = 20
B_Yvalue = 40

F2_preview_label.place(x=0, y=20)

def PreviewWindowOpener():
	print("Preview Window Opener Button Pressed")
	x = db.DatabaseManager("sample job", 'sample.db')
	preview.display_timesheet(x,datetime.date(2021,5,1), datetime.date(2021,6,1))


def TimeManagerOpener():
	print("Time Manager Opener button pressed")


Preview = Button(Frame2, text="Preview Module", command = PreviewWindowOpener,height=B_HEIGHT, width=B_WIDTH)
Preview.place(x=0, y=B_Yvalue)

Time_manager = Button(Frame2, text="Time Manager", command = TimeManagerOpener,height=B_HEIGHT, width=B_WIDTH)
Time_manager.place(x= 500,y=B_Yvalue)


#----------------------FRAMES THREE OBJECTS--------------------------
# Freame Two is the Time module, and Preview.





"""

def Submit_Date():
	Submitbutton = Label(root, text=clicked.get())
	Submitbutton.pack()

B_HEIGHT = 5
B_WIDTH = 15
mylabel = Label(root, text = "test")
mylabel.grid(row=0, column = 1)

#--------------------------BUTTONS-----------------
def PreviewWindowOpener():
	print("Preview Window Opener Button Pressed")
	
def TimeManagerOpener():
	print("Time Manager Opener button pressed")

def EnterStartTime():
	print("hello")

def EnterEndTime():
	print("hello")




Preview = Button(root, text="Preview Module", command = PreviewWindowOpener,height=B_HEIGHT, width=B_WIDTH)
Preview.grid(row=0, column = 0)


Time_manager = Button(root, text="Time Manager", command = TimeManagerOpener,height=B_HEIGHT, width=B_WIDTH)
Time_manager.grid(row=1, column = 0)

Start_time = Button(root, text="Export ", command = Submit_Date, height=B_HEIGHT, width=B_WIDTH)
Start_time.grid(row=2, column = 0)


#End_time = Button(root, text="Submit a Time", command = Submit_Date, height=B_HEIGHT, width=B_WIDTH)
#End_time.grid(row=6, column = 5)

#Spin Boxes
InsertTime = Frame(root)
InsertTime.grid(row= 3, column = 0)
F1 = Frame(root)
F1.grid(row = 4, column = 0)



min_sb = Spinbox(
    F1,
    from_=0,
    to=23,
    width=2,
    font=f,
    )

sec_hour = Spinbox(
    F1,
    from_=0,
    to=59,
    font=f,
    width=2, 
    )
sec = Spinbox(
    F1,
    from_=0,
    to=59,
    width=2,
    font=f,
    )



#FOR ENTERING THE TIME
colon_1 = Label(F1, text = ":", font = (f,20))
colon_2 = Label(F1, text = ":", font = (f,20))
min_sb.grid(row =  0,column = 0)
colon_1.grid(row =  0,column = 1)
sec_hour.grid(row = 0,column = 2)
colon_2.grid(row = 0 ,column = 3)
sec.grid(row = 0, column = 4)
"""
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