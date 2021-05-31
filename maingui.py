"""
CIS 422: Project 2: Work at home helper
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This is the Main GUI File. It uses tkinter to display the user interface and uses 
the preview and timetracker modules to open new tkinter windows. 
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
root.title("WorkAtHomeHelper")	#Change the name of the window
root.geometry("510x600")		#This is to size the winodw
root.configure(bg='white')		#Background color = white
f=("Times", 20) 

"""
DATABASE CONFIGURATION
"""
	
Jobname = "Learning Assistant" 						#TO CHANGE THE NAME OF THE JOB/DATABASE
db = dbm.DatabaseManager(Jobname, 'JobDatabase.db')	#TO CHANGE NAME OF DATABASE

#============================FRAME ONE OBJECTS=============================
#Frame One is how the title is being oriented
Frame1 = Frame(root, width= 600)				#Set The Frame to be on the root
Frame1.place(x=0, y=0, height=40, width = 600)

TitleFont =("Times", 30) 
Title = Label(Frame1, text= "WorkAtHomeHelper", font=TitleFont)
Title.place(x=0,y=0)
#============================FRAME TWO OBJECTS=============================
# Frame Two contains the Time and Preview and preview buttons. IT also contains the 
# Start date and end date feilds which are also Frames inside of a frame

F2_Font = ("Times", 20)				#FONT
F2_background_color = 'white'		#Background COLOR

Frame2 = Frame(root, width= 800, bg= F2_background_color)	#Createion of frame using the root window
Frame2.place(x =0,y=40, height=240, width = 800)			#Placed the frame under Frame One
 
F2_preview_label = Label(Frame2, text="Click The Preview Module To Preview, Edit, And Print The spreadsheet 		")
F2_Time_label = Label(Frame2, text="Click The Time Manager Module To Automatically Track And Submit Time 	")
#The two labels show what each button does


F2_preview_label.place(x=0, y=0) #Place Labels
F2_Time_label.place(x=0, y=20)

#-------CREATION OF THE START DATE FRAME--------
#This frame is a child of frame2
PSFRAME = Frame(Frame2, width= 140)					#Create and place Frame
PSFRAME.place(x=200, y=45, height=95, width = 140)

P_START_LABEL = Label(PSFRAME, text="Start Date (M/D/Y)")	#Create a Label for the Start date & Place
P_START_LABEL.place(x=0,y=0)

#Create Labels to show what each entry will be
S_MONTH = Label(PSFRAME, text="Month:")		#MONTH
S_DAY   = Label(PSFRAME, text="Day:")		#DAY
S_YEAR  = Label(PSFRAME, text="Year:")		#YEAR

S_MONTH.place(x=0,y=20)	#PLACE Month Day Year LABELS
S_DAY.place(x=0,y=40)
S_YEAR.place(x=0,y=60)

#Create the entrys for the user to type into
PS_M_ENTRY = Entry(PSFRAME,width = 10)		#MONTH
PS_D_ENTRY = Entry(PSFRAME,width = 10)		#DAY
PS_Y_ENTRY = Entry(PSFRAME,width = 10)		#YEAR
PS_M_ENTRY.place(x=50,y=20)				#PLACE ENTRYS USING THE PSFRAME
PS_D_ENTRY.place(x=50,y=40)
PS_Y_ENTRY.place(x=50,y=60)

#-------CREATION OF THE END DATE FRAME--------
#This frame is a child of frame2
PEFRAME = Frame(Frame2, width= 140)
PEFRAME.place(x=350, y=45, height=95, width = 140)		#Create and Place Frame

P_END_LABEL = Label(PEFRAME, text="End Date (M/D/Y)")	#Create Frame Labale/place
P_END_LABEL.place(x=0,y=0)

#Create Labels for User
E_MONTH = Label(PEFRAME, text="Month:")		#MONTH
E_DAY   = Label(PEFRAME, text="Day:")		#DAY
E_YEAR  = Label(PEFRAME, text="Year:")		#YEAR

#Place the labels
E_MONTH.place(x=0,y=20)		#MONTH
E_DAY.place(x=0,y=40)		#DAY
E_YEAR.place(x=0,y=60)		#YEAR


#Create the entrys for the user to type into
PE_M_ENTRY = Entry(PEFRAME,width = 10)		#MONTH
PE_D_ENTRY = Entry(PEFRAME,width = 10)		#DAY
PE_Y_ENTRY = Entry(PEFRAME,width = 10)		#YEAR
PE_M_ENTRY.place(x=50,y=20)					#PLACE THE ENTRIES
PE_D_ENTRY.place(x=50,y=40)
PE_Y_ENTRY.place(x=50,y=60)

def PreviewWindowOpener():
	"""The preview window opener will GET() all the text that was inputed from the preview
	   Feilds. If no input is selected it will open up the enterity of the database up to the
	   year 10000AD. IF an input is spcified it will open the preview modul between the 2 dates.
	   IF the entry boxes are not filled out corretly, it will update the input handler box
	   to display that an error had occured"""
	#GET START DATE
	s_month = (PS_M_ENTRY.get()) #START MONTH
	s_day = (PS_D_ENTRY.get())	#START DAY
	s_year = (PS_Y_ENTRY.get())	#START YEAR
	#GET END DATE
	e_month = (PE_M_ENTRY.get()) #END MONTH
	e_day = (PE_D_ENTRY.get())	#END DAY
	e_year = (PE_Y_ENTRY.get())	#END YEAR
	if ((s_month == '') and (s_day == '') and (s_year == '') 
		and (e_month == '') and (e_day== '') and (e_year== '')):
		NoteLabel.config(text="Default Preview Window Opened")   #Check if all feilds are empty
		ps_default = datetime.date(1,1,1)						#Default times
		pe_default = datetime.date(9000,1,1)
		preview.display_timesheet(db, ps_default, pe_default)
		return

	#If there is atleast 1 input
	NoteLabel.config(text="Specific Dates Preview Window")  #Change the title 
	try:
		p_start = datetime.date(int(s_year),int(s_month), int(s_day))		#Get Start time 
		p_end = datetime.datetime(int(e_year),int(e_month), int(e_day))		#Get end time
		U_desc = "Start Date" + str(p_start)								#update descrption label to be SD
		U_date = "End date" + str(p_end)									#update the date label to be ED

		Update_label_desc.config(text= U_desc)		#Update the UI using configure
		Update_label_date.config(text=U_date)	
		


		#For Deguging purposes UNCOMMENT these lines
		#print(f"START DATE:{s_month}/{s_day}/{s_year}")
		#print(f"END DATE:{e_month}/{e_day}/{e_year}")
		#print("Preview Window Opener Button Pressed")
		preview.display_timesheet(db, p_start, p_end)
		return
	except:
		#If there is an error UPDATE the box and configure the labels
		U_desc = "ERROR: Couldn't Process Input"
		U_date = "Make Sure All Fields Are Filled or Empty"
		U_tw = "With Positive (>0) Integers"

		Update_label_desc.config(text= U_desc)		#update the labels in the input handler
		Update_label_date.config(text=U_date)		
		Update_label_timework.config(text=U_tw)
		return



def TimeManagerOpener():
	"""the TimeManagerOpener is called when the user clicks on the time manager button
	   The button is part of Frame2. When it is clicked this fucntion will open the 
	   time-tracker module using the database configured above. """
	timetracker.tracktime(db)
	#print("Time Manager Opener button pressed")  #Uncomment to Debug

#Creat the preview Button and time manager buttons inside Frame Two
Preview = Button(Frame2, text="Preview Module", command = PreviewWindowOpener,height=5, width=15)
Preview.place(x=50, y=42) #Place and call the PreviewWindowOpener() fucntion when clicked

Time_manager = Button(Frame2, text="Time Manager", command = TimeManagerOpener,height=5, width=15)
Time_manager.place(x= 50,y=141)  #Place and call the TimeManagerOpener() fucntion when clicked


#============================FRAME THREE OBJECTS=============================
#Frame 3 contians all the frames, labels and input feilds for entering work manually
Frame3= Frame(root, width= 600)						#Make A CHILD FRAME OF THE ROOT	
Frame3.place(x=0, y=300, height=250, width = 600)	#Place

#Frame 3 Labels
F3_MANENTRY_LABEL = Label(Frame3, text="Enter A Work Session Manually") #make the label
F3_MANENTRY_LABEL.place(x= 0,y=0)	#Place

F3_JOBDESC_LABEL=Label(Frame3, text="Description:")
F3_JOBDESC_LABEL.place(x=0,y=20)

#ENTRYS
F3_DESCENTRY = Entry(Frame3,width = 50)
F3_DESCENTRY.place(x=80,y=20)

#--------------------------Start date frame ------------------
SDFrame = Frame(Frame3, width= 140)						#Child of frame3
SDFrame.place(x=0, y=60, height=80, width = 140)

#create label for the startdate
F3_STARTDATE_LABEL = Label(SDFrame, text="Start Date (M/D/Y)") 	#Place
F3_STARTDATE_LABEL.place(x=0,y=0)
												#FOR THE SD- StartDate
SD_MONTH = Label(SDFrame, text="Month:")		#MONTH
SD_DAY   = Label(SDFrame, text="Day:")			#DAY
SD_YEAR  = Label(SDFrame, text="Year:")			#YEAR

SD_MONTH.place(x=0,y=20)		#Place
SD_DAY.place(x=0,y=40)
SD_YEAR.place(x=0,y=60)

#Create entries
SD_M_ENTRY = Entry(SDFrame,width = 10)
SD_D_ENTRY = Entry(SDFrame,width = 10)
SD_Y_ENTRY = Entry(SDFrame,width = 10)
SD_M_ENTRY.place(x=50,y=20)
SD_D_ENTRY.place(x=50,y=40)
SD_Y_ENTRY.place(x=50,y=60)

#--------------------------Start Time Frame------------------------
STARTFrame = Frame(Frame3, width= 200)				#create frame as child of frame three
STARTFrame.place(x=170, y=60, height=70, width = 200) 	#place

IST =Label(STARTFrame, text="Intial Start Time (H:M AM/PM)")	#create label
IST.place(x=0,y=0)		#PALCE

#Create Spin Boxes
SF_min_sb = Spinbox(			#For the Minute Box using the STARTFrame		
    STARTFrame,
    from_=0,
    to=59,						#Limit to 59 mins
    width=2,
    font=f,						#width set to 2 and font as times new roman
    )

SF_sec_hour = Spinbox(			#For the Hour Box using the STARTFrame
    STARTFrame,
    from_=1,					#start at 1 hour
    to=12,						#Limit to 12 hours
    font=f,
    width=2, 					#width set to 2 and font as times new roman
    )


def show():						#Show Fucntion is for debuging the AM/PM drop down menu
	AM_PM = clicked.get()
	print(AM_PM)

#Create the AM/PM Button
TIME = ["AM","PM"]				#Set MENU ITEMS
clicked = StringVar()
clicked.set(TIME[0])			#SEt Default menu item
drop = OptionMenu(STARTFrame, clicked, *TIME) 	#Create menu widgit
drop.place(x=120,y=20)			#place widgit
	
#create the colon and place buttons
colon_2 = Label(STARTFrame, text = ":", font = (f,20))  #create label
SF_min_sb.place(x=65,y=20)						#place items
colon_2.place(x=50,y=20)						
SF_sec_hour.place(x=0,y=20)




#-------------------------------Time FRAME--------------------------
TFrame = Frame(Frame3, width= 120)			#Create time frame as child of Frame3
TFrame.place(x=400, y=60, height=100, width = 120)			#place

F3_DURATION_LABEL=Label(TFrame, text="Time Worked")		#create label for the Timeworked
F3_DURATION_LABEL.place(x=0,y=0)

#Create Spin Boxes
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

#Create labels to display what spin box is what to thr user
T_HOURS = Label(TFrame, text="Hours")		#hours label
T_MINS  = Label(TFrame, text="Mins")		#mins label
T_HOURS.place(x=60,y=25)	#place
T_MINS.place(x=60,y=55)

#place the spin boxes
min_sb.place(x=0,y=50)
sec_hour.place(x=0,y=20)

def Submitbutton():
	"""The submit  button will GET() all the text that was inputed from the manually enterd
	   Feilds.If a entry is misssing a input it will thorw and error to the input handler.
	   If an input is spcified it will open the preview modul between the 2 dates.
	   If the entry boxes are not filled out corretly, it will update the input handler box
	   to displacy that an error had occured"""
	print("SUBMIT BUTTON PRESSED")
	#Get The start date
	sub_jobdesc = F3_DESCENTRY.get() 		#Get the desc
	sub_sdem = SD_M_ENTRY.get()				#get the Month
	sub_sded = SD_D_ENTRY.get()				#GEt the day
	sub_sdey = SD_Y_ENTRY.get()				#Get the year

	in_m = SF_min_sb.get()			#Get mins
	in_h = SF_sec_hour.get()		#get hours

	t_m = min_sb.get()				#get mins worked
	t_h = sec_hour.get()			#get hours worked

	M_PM = clicked.get()			#get AM/PM

	if(M_PM == "PM"):
		in_h = int(in_h)+12

	#Uncomment the debug
	#print(f"{sub_jobdesc} {sub_sdey}/{sub_sdem}/{sub_sded} IT: {in_h}:{in_m} {M_PM} TW: {t_h}:{t_m} ")
	#UPDATE THE STUFF
	NoteLabel.config(text="Manual Date Entered")  #update the config in the input handle box
	try:
		
		#Update the inputhandler with the new times
		U_desc = "Desc: " + str(sub_jobdesc)
		U_date = "Date: " + str(datetime.datetime(int(sub_sdey), int(sub_sdem), int(sub_sded),int(in_h), int(in_m)))
		U_tw = "Timeworked: " + str(datetime.timedelta(hours=int(t_h) ,minutes=int(t_m))) 

		Update_label_desc.config(text= U_desc) 	#update the config
		Update_label_date.config(text=U_date)
		Update_label_timework.config(text=U_tw)


		db.add_activity(sub_jobdesc , datetime.datetime(int(sub_sdey), int(sub_sdem), int(sub_sded),int(in_h), int(in_m)),
	 	 datetime.timedelta(hours=int(t_h) ,minutes=int(t_m)))

	except:
		#If there was an error thrown while getting the datetimes
		U_desc = "ERROR: Couldn't Process Input"
		U_date = "Make Sure All Fields Are Filled"
		U_tw = "& Start Date has positive (>0) Integers"

		Update_label_desc.config(text= U_desc) 	#update the config
		Update_label_date.config(text=U_date)
		Update_label_timework.config(text=U_tw)

#Create the submit button and use the Submitbutton() fucntion once pressed
F3_submit = Button(Frame3, text="Submit Time", command = Submitbutton,height=3, width=10)
F3_submit.place(x=200, y=150) #Place

#create the input handler box
NoteFrame = Frame(Frame2, width= 290, borderwidth = 2, relief = "ridge") 	#set inital size
NoteFrame.place(x=200, y= 143, height=97, width = 290) 	#palce

NoteLabel = Label(NoteFrame, text="Input Display Handler") 	#create inital label
NoteLabel.place(x=0,y=0)

#The following are used to make the lines inside the handler
Update_label_desc = Label(NoteFrame, text="")
Update_label_desc.place(x=0,y =20)
Update_label_date = Label(NoteFrame, text="")
Update_label_date.place(x=0,y =40)
Update_label_timework = Label(NoteFrame, text="")
Update_label_timework.place(x=0,y=60)

#Open the window 
root.mainloop()
