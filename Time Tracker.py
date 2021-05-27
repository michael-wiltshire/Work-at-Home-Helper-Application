from tkinter import *
from _datetime import datetime
from database import dbm
import time

#def calculate time(string job, date date, datetime)->timedelta:

#def clock_in(string job, datetime time)->bool:

#def clock_out(string job, datetime time)->bool:

#def create_window(string job):

def main():
    root = Tk()
    root.geometry("500x200")
    root.title('Time Tracker')



    class time():
        def __init__(self):
            self.job = "job"
            self.start_time = datetime.now()
            self.stop_time = datetime.now()
            self.description = "job"
            self.elapsed_time = 0


    my_time = time()
    my_time.description = StringVar()



    def clock_in():
        my_time.start_time = datetime.now()
        Button(root, text="Stop Time", command=clock_out,height=5,width=20,bg="red").place(relx=0.5, rely=0.5, anchor=CENTER)

    def clock_out():
        my_time.stop_time = datetime.now()
        #print(my_time.stop_time)
        calculate_time()

    def calculate_time():
        print(my_time.description.get(),"start time:", my_time.start_time,"\n","stop time:", my_time.stop_time, "\n")
        #calculates elapsed time
        my_time.elapsed_time = (my_time.stop_time - my_time.start_time)
        print("total time:",my_time.elapsed_time, "\n")
        db = dbm.DatabaseManager(my_time.job)
        id = db.add_activity(my_time.description.get(), my_time.start_time, my_time.elapsed_time)
        thisJob = db.get_activity(id)
        print(id, thisJob)

    Label(root, text="Job Description").place(anchor=NW)  #label
    Entry(root, textvariable = my_time.description, width=50).place(relx=0.5, anchor=N) #entry textbox

    Button(root, text="Start Time", command=clock_in,height=5,width=20,bg="green").place(relx=0.5, rely=0.5, anchor=CENTER)


    root.mainloop()
    
if __name__ == '__main__':
    main()
