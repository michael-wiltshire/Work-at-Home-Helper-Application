from tkinter.constants import DISABLED
from database import dbm
import datetime
import tkinter as tk


root = tk.Tk()


def previewPress():
    label = tk.Label(root, text = "Preview button pressed")
    label.pack()

def exportPress():
    label = tk.Label(root, text = "Export button pressed")
    label.pack()

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

    activity_range = db.get_activies_within_range(start_datetime, end_datetime)
    
    num_rows = len(activity_range)
    num_cols = len(activity_range[0])
    for i in range(num_rows):
        for j in range(num_cols):
            e = tk.Entry(root, width = 25, fg = "blue", font = ('Arial', 16, 'bold'))
            e.grid(row = i, column = j)
            e.insert(0, activity_range[i][j])

def main():
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    display_timesheet('CIS 422 TA', start, end)
    exportButton = tk.Button(root, text = "Export", command = exportPress, height = 3, width = 15)
    exportButton.place(x=1500, y=25)
    root.mainloop()

if __name__ == '__main__':
    main()