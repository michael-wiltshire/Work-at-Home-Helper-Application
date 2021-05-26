from tkinter.constants import DISABLED
from database import dbm
import datetime
import tkinter as tk
from tkinter import ttk

def display_timesheet(db: dbm.DatabaseManager, start_date: datetime.date, end_date: datetime.date) -> bool:
    # create the interface for the preview module
    window = tk.Tk()
    tree = ttk.Treeview(window, height=25)
    tree['show']='headings'

    # function to delete a certain activity
    def delete_activity():
        selected = tree.selection()[0]
        id = tree.item(selected)["values"][0]
        db.delete_activity(id)
        tree.delete(selected)

    # get start and end datetime 
    start_datetime = datetime.datetime.combine(start_date, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end_date, datetime.datetime.min.time())

    # Define columns
    tree["columns"] = ("job ID", "job", "description", "date", "start", "end", "duration")

    # Assign width, minwidth, and anchor to respective columns
    tree.column("job ID", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("job", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("description", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("date", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("start", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("end", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("duration", width=180, minwidth=180, anchor=tk.CENTER)

    # Assign heading names to their respective columns
    tree.heading("job ID", text="Job ID", anchor=tk.CENTER)
    tree.heading("job", text = "Job", anchor=tk.CENTER)
    tree.heading("description", text="Description", anchor=tk.CENTER)
    tree.heading("date", text="Date", anchor=tk.CENTER)
    tree.heading("start", text="Start", anchor=tk.CENTER)
    tree.heading("end", text="End", anchor=tk.CENTER)
    tree.heading("duration", text="Duration", anchor=tk.CENTER)

    # insert activities into table
    i = 0
    activity_range = db.get_activities_within_range(start_datetime, end_datetime)
    
    try:
        for activity in activity_range:
            try:
                # get the date
                date = activity[3].strftime("%m/%d/%y")

                # get startime for activity
                start_time = activity[3].strftime("%I:%M %p")

                # get endtime for activity
                end = (activity[3] + datetime.timedelta(seconds=activity[-1]))
                end_time = end.strftime("%I:%M %p")

                # get duration (in hours)
                duration = round(activity[-1]/3600, 2)

                # insert activity into table
                new_act = activity[:3] + (date, start_time, end_time, duration)
                tree.insert('', i, text="", values=new_act)
                i = i + 1
            except:
                return False
        tree.pack()

        # delete button to delete a certain activity
        deleteButton = tk.Button(window, text = "Delete", command = delete_activity, height = 3, width = 15)
        deleteButton.pack(side=tk.LEFT)

        # used to run the window
        window.mainloop()

        # returns True on success
        return True
    except:
        # returns False on failure
        return False

def main():
    jobname = "sample job"
    db = dbm.DatabaseManager(jobname, 'sample.db')
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)

    # add sample data
    db.add_activity("Office Hours 4", datetime.datetime(2021, 5, 27), datetime.timedelta(hours=5))
    db.add_activity("Office Hours 3", datetime.datetime(2021, 5, 26), datetime.timedelta(hours=4))
    db.add_activity("Office Hours 2", datetime.datetime(2021, 5, 25), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 1", datetime.datetime(2021, 5, 24), datetime.timedelta(hours=2))

    display_timesheet(db, start, end)


if __name__ == '__main__':
    main()
