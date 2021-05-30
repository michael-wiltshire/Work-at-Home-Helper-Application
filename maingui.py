"""
CIS 422: Project 2: Work at home helper
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files.
"""

from tkinter import *
import preview
from database import dbm
import datetime
import timetracker

"""
Tkninter CONFIGURATION
"""
root = Tk()
root.title("WorkAtHomeHelper")
root.geometry("510x600")
root.configure(bg='white')
f=("Times", 20) 

"""
DATABASE CONFIGURATION
"""
Jobname = "Learning Assistant"
db = dbm.DatabaseManager(Jobname, 'JobDatabase.db')

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

Frame2 = Frame(root, width= 800, bg= F2_background_color)
Frame2.place(x =0,y=40, height=240, width = 800)
 
F2_preview_label = Label(Frame2, text="Click The Preview Module to Preview, Edit and Print Your spreadsheet 		")
F2_Time_label = Label(Frame2, text="Click The Time Manager Module To Automatically Track and Submit Time 	")

B_HEIGHT = 5
B_WIDTH = 15
B_Xvalue = 20
B_Yvalue = 40

F2_preview_label.place(x=0, y=0)
F2_Time_label.place(x=0, y=20)

#PREVIEW MODULE START AND END DATES

PSFRAME = Frame(Frame2, width= 140)
PSFRAME.place(x=200, y=45, height=95, width = 140)

P_START_LABEL = Label(PSFRAME, text="Start Date (M/D/Y)")
P_START_LABEL.place(x=0,y=0)


S_MONTH = Label(PSFRAME, text="Month:")
S_DAY   = Label(PSFRAME, text="Day:")
S_YEAR  = Label(PSFRAME, text="Year:")

S_MONTH.place(x=0,y=20)
S_DAY.place(x=0,y=40)
S_YEAR.place(x=0,y=60)

PS_M_ENTRY = Entry(PSFRAME,width = 10)
PS_D_ENTRY = Entry(PSFRAME,width = 10)
PS_Y_ENTRY = Entry(PSFRAME,width = 10)
PS_M_ENTRY.place(x=50,y=20)
PS_D_ENTRY.place(x=50,y=40)
PS_Y_ENTRY.place(x=50,y=60)
#END TIME ============================================
#PREVIEW MODULE START AND END DATES
PEFRAME = Frame(Frame2, width= 140)
PEFRAME.place(x=350, y=45, height=95, width = 140)

P_END_LABEL = Label(PEFRAME, text="END DATE (M/D/Y)")
P_END_LABEL.place(x=0,y=0)

E_MONTH = Label(PEFRAME, text="Month:")
E_DAY   = Label(PEFRAME, text="Day:")
E_YEAR  = Label(PEFRAME, text="Year:")

E_MONTH.place(x=0,y=20)
E_DAY.place(x=0,y=40)
E_YEAR.place(x=0,y=60)

PE_M_ENTRY = Entry(PEFRAME,width = 10)
PE_D_ENTRY = Entry(PEFRAME,width = 10)
PE_Y_ENTRY = Entry(PEFRAME,width = 10)
PE_M_ENTRY.place(x=50,y=20)
PE_D_ENTRY.place(x=50,y=40)
PE_Y_ENTRY.place(x=50,y=60)

#==============================================

def PreviewWindowOpener():
	#GET START DATE
	s_month = (PS_M_ENTRY.get()) #START MONTH
	print(s_month)
	s_day = (PS_D_ENTRY.get())	#START DAY
	s_year = (PS_Y_ENTRY.get())	#START YEAR
	#GET END DATE
	e_month = (PS_M_ENTRY.get()) #END MONTH
	e_day = (PS_D_ENTRY.get())	#END DAY
	e_year = (PS_Y_ENTRY.get())	#END YEAR
	if ((s_month or s_day or s_year or e_month or e_day or e_year) == ''):
		ps_default = datetime.date(1,1,1)
		pe_default = datetime.date(3000,1,1)
		preview.display_timesheet(db, ps_default, pe_default)
		return

	p_start = datetime.date(int(s_year),int(s_month), int(s_day))
	p_end = datetime.datetime(int(e_year),int(e_month), int(e_day))

	print(f"START DATE:{s_month}/{s_day}/{s_year}")
	print(f"END DATE:{e_month}/{e_day}/{e_year}")
	print("Preview Window Opener Button Pressed")
	preview.display_timesheet(db, p_start, p_end)
	#x = db.DatabaseManager("sample",'sample.db')
	#preview.display_timesheet(x,datetime.date(2021,5,1), datetime.date(2021,6,1))




def TimeManagerOpener():
	timetracker.tracktime(db)
	print("Time Manager Opener button pressed")

Preview = Button(Frame2, text="Preview Module", command = PreviewWindowOpener,height=B_HEIGHT, width=B_WIDTH)
Preview.place(x=50, y=B_Yvalue+2)

Time_manager = Button(Frame2, text="Time Manager", command = TimeManagerOpener,height=B_HEIGHT, width=B_WIDTH)
Time_manager.place(x= 50,y=141)


#----------------------FRAMES THREE OBJECTS--------------------------
Frame3= Frame(root, width= 800)
Frame3.place(x=0, y=300, height=250, width = 800)

F3_MANENTRY_LABEL = Label(Frame3, text="Enter A Work Session Manually")
F3_MANENTRY_LABEL.place(x= 0,y=0)


#Frame 3 Labels

F3_JOBNAME_LABEL=Label(Frame3, text="Job Name:")
F3_JOBNAME_LABEL.place(x=0,y=20)
F3_JOBDESC_LABEL=Label(Frame3, text="Description:")
F3_JOBDESC_LABEL.place(x=0,y=45)

#ENTRYS
F3_JOBENTRY = Entry(Frame3,width = 60)
F3_JOBENTRY.place(x=80,y=20)
F3_DESCENTRY = Entry(Frame3,width = 60)
F3_DESCENTRY.place(x=80,y=45)

#START DATE FRAME================================================
SDFrame = Frame(Frame3, width= 140)
SDFrame.place(x=0, y=90, height=80, width = 140)

F3_STARTDATE_LABEL = Label(SDFrame, text="Start Date (M/D/Y)")
F3_STARTDATE_LABEL.place(x=0,y=0)

SD_MONTH = Label(SDFrame, text="Month:")
SD_DAY   = Label(SDFrame, text="Day:")
SD_YEAR  = Label(SDFrame, text="Year:")

SD_MONTH.place(x=0,y=20)
SD_DAY.place(x=0,y=40)
SD_YEAR.place(x=0,y=60)

SD_M_ENTRY = Entry(SDFrame,width = 10)
SD_D_ENTRY = Entry(SDFrame,width = 10)
SD_Y_ENTRY = Entry(SDFrame,width = 10)
SD_M_ENTRY.place(x=50,y=20)
SD_D_ENTRY.place(x=50,y=40)
SD_Y_ENTRY.place(x=50,y=60)

#START TIME FRAME===============================================
STARTFrame = Frame(Frame3, width= 200)
STARTFrame.place(x=170, y=90, height=70, width = 200)

IST =Label(STARTFrame, text="Intial Start Time (H:M AM/PM)")
IST.place(x=0,y=0)

SF_min_sb = Spinbox(
    STARTFrame,
    from_=0,
    to=59,
    width=2,
    font=f,
    )

SF_sec_hour = Spinbox(
    STARTFrame,
    from_=0,
    to=12,
    font=f,
    width=2, 
    )


def show():
	AM_PM = clicked.get()
	print(AM_PM)


TIME = ["AM","PM"]
clicked = StringVar()
clicked.set(TIME[0])
drop = OptionMenu(STARTFrame, clicked, *TIME)
drop.place(x=120,y=20)

#NEED AM/PM meu 


colon_2 = Label(STARTFrame, text = ":", font = (f,20))
SF_min_sb.place(x=65,y=20)
colon_2.place(x=50,y=20)
SF_sec_hour.place(x=0,y=20)

#create_activity


#Time FRAME--------------------------
TFrame = Frame(Frame3, width= 120)
TFrame.place(x=400, y=90, height=100, width = 120)

F3_DURATION_LABEL=Label(TFrame, text="Time Worked")
F3_DURATION_LABEL.place(x=0,y=0)

min_sb = Spinbox(
    TFrame,
    from_=0,
    to=23,
    width=2,
    font=f,
    )

sec_hour = Spinbox(
    TFrame,
    from_=0,
    to=59,
    font=f,
    width=2, 
    )



T_HOURS = Label(TFrame, text="Hours")
T_MINS  = Label(TFrame, text="Mins")
T_HOURS.place(x=60,y=25)
T_MINS.place(x=60,y=55)


IST =Label(STARTFrame, text="Intial Start Time")
IST.place(x=0,y=0)

min_sb.place(x=0,y=20)
sec_hour.place(x=0,y=50)

def Submitbutton():
	print("SUBMIT BUTTON PRESSED")
	#Get The start date
	sub_jobdesc = F3_DESCENTRY.get()
	sub_sdem = SD_M_ENTRY.get()
	sub_sded = SD_D_ENTRY.get()
	sub_sdey = SD_Y_ENTRY.get()

	in_h = SF_min_sb.get()
	in_m = SF_sec_hour.get()

	t_m = min_sb.get()
	t_h = sec_hour.get()

	M_PM = clicked.get()

	print(f"{sub_jobdesc} {sub_sdey}/{sub_sdem}/{sub_sded} IT: {in_h}:{in_m} {M_PM} TW: {t_h}:{t_m} ")



F3_submit = Button(Frame3, text="Submit Time", command = Submitbutton,height=3, width=10)
F3_submit.place(x=0, y=180)

#Time FRAME------------------------------


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