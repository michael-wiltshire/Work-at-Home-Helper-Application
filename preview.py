from tkinter.constants import DISABLED
from database import dbm
import datetime
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
tree = ttk.Treeview(root, height=25)
tree['show'] = 'headings'

def display_timesheet(job: str, start_date: datetime.date, end_date: datetime.date):
    db = dbm.DatabaseManager(job)
    start_datetime = datetime.datetime.combine(start_date, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end_date, datetime.datetime.min.time())
    
    # dummy data
    db.add_activity("Office Hours 1", datetime.datetime.now(), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 2", datetime.datetime(2021, 5, 19), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 3", datetime.datetime(2021, 5, 20), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 4", datetime.datetime(2021, 5, 21), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 5", datetime.datetime(2021, 5, 22), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 6", datetime.datetime(2021, 5, 23), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 7", datetime.datetime(2021, 5, 24), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 8", datetime.datetime(2021, 5, 25), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 9", datetime.datetime(2022, 5, 25), datetime.timedelta(hours=3))
    db.add_activity("Office Hours 10", datetime.datetime(2021, 5, 26), datetime.timedelta(hours=3))

    # Define columns
    tree["columns"] = ("job ID", "job", "description", "date", "time")

    # Assign width, minwidth, and anchor to respective columns
    tree.column("job ID", width=50, minwidth=50, anchor=tk.CENTER)
    tree.column("job", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("description", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("date", width=180, minwidth=180, anchor=tk.CENTER)
    tree.column("time", width=180, minwidth=180, anchor=tk.CENTER)

    # Assign heading names to their respective columns
    tree.heading("job ID", text="Job ID", anchor=tk.CENTER)
    tree.heading("job", text = "Job", anchor=tk.CENTER)
    tree.heading("description", text="Description", anchor=tk.CENTER)
    tree.heading("date", text="Date", anchor=tk.CENTER)
    tree.heading("time", text="Time", anchor=tk.CENTER)

    # insert activities into table
    i = 0
    activity_range = db.get_activies_within_range(start_datetime, end_datetime)
    for activity in activity_range:
        tree.insert('', i, text="", values=activity)
        i = i + 1
    tree.pack()

def delete_activity():
    selected = tree.selection()[0]
    tree.delete(selected)

def main():
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    display_timesheet('CIS 422 TA', start, end)
    deleteButton = tk.Button(root, text = "Delete", command = delete_activity, height = 3, width = 15)
    deleteButton.pack(side=tk.LEFT)
    root.mainloop()

if __name__ == '__main__':
    main()