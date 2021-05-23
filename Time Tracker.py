from tkinter import *
import datetime
import time

#def calculate time(string job, date date, datetime)->timedelta:

#def clock_in(string job, datetime time)->bool:

#def clock_out(string job, datetime time)->bool:

#def create_window(string job):


root = Tk()
root.title('how to get text from textbox')



class time():
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.stop_time = datetime.datetime.now()
        self.description =""
global start_time
global stop_time
#date = datetime.datetime.now()
#print(date)

my_time = time()
my_time.description = StringVar()



def clock_in():
    my_time.start_time = datetime.datetime.now()
    #print(description.get(), start_time)
    #print(my_time.start_time)
    # print(date)
    # date = datetime.datetime.now()
    # print(date)

def clock_out():
    my_time.stop_time = datetime.datetime.now()
    #print(my_time.stop_time)

def calculate_time():
    print(my_time.description.get(), my_time.start_time, my_time.stop_time)

Label(root, text="Job Description").grid(row=0, sticky=W)  #label
Entry(root, textvariable = my_time.description).grid(row=0, column=1, sticky=E) #entry textbox

startbutton = Button(root, text="Start Time", command=clock_in).grid(row=3, column=0, sticky=W) #button
stopbutton = Button(root, text="Stop Time", command=clock_out).grid(row=3, column=1, sticky=W) #button
calculate_time = Button(root, text="Save", command=calculate_time).grid(row=3, column=2, sticky=W)
mainloop()