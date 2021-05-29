from tkinter.constants import DISABLED
from database import dbm
from create_spreadsheets import *
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

def display_timesheet(db: dbm.DatabaseManager, start_date: datetime.date, end_date: datetime.date) -> bool:
    # create the interface for the preview module
    window = tk.Tk()
    window.title("Preview Module")
    
    tree = ttk.Treeview(window, height=25)
    tree['show'] = 'headings'
    
    # function to delete a certain activity
    def delete_activity():
        selected = tree.selection()[0]
        id = tree.item(selected)["values"][0]
        db.delete_activity(id)
        tree.delete(selected)


    # function to edit a certain activity
    def edit_activity():
        edit_window = tk.Toplevel(window)
        edit_window.title("Edit Activity Window")

        # description label
        desc_label = tk.Label(edit_window, text="description:", font="none 12 bold")
        desc_label.grid(row=0, column=0)

        # start label
        start_label = tk.Label(edit_window, text="start (format: 00:00 AM/PM):", font="none 12 bold")
        start_label.grid(row=1, column=0)

        # duration label
        duration_label = tk.Label(edit_window, text="duration (decimal hours)", font = "none 12 bold")
        duration_label.grid(row=2, column=0)

        # textbox to enter description
        description_box = tk.Entry(edit_window, width=50)
        description_box.grid(row=0, column=1)

        # textbox to enter start time
        start_box = tk.Entry(edit_window, width=20)
        start_box.grid(row=1, column=1)

        # textbox to enter duration
        duration_box = tk.Entry(edit_window, width=20)
        duration_box.grid(row=2, column=1)

        # grab selected activity
        selected = tree.focus()
        # grab the values of the selected activity
        selected_values = tree.item(selected, 'values')

        # add corresponding value to their proper entry boxes
        description_box.insert(0, selected_values[2])
        start_box.insert(0, selected_values[4])
        duration_box.insert(0, selected_values[6])

        def edit_activity_helper():
            # get id and job of selected activity
            selected_id = selected_values[0]
            selected_job = selected_values[1]

            # get the new description of the selected activity
            new_desc = description_box.get()

            # get date of selected activity
            date = selected_values[3] 

            # convert string date to actual date object
            date_object = datetime.datetime.strptime(date, "%m/%d/%y").date()

            # get new start time of activity
            new_start = start_box.get() 
            
            # convert new start time to a time object
            new_start_object = datetime.datetime.strptime(new_start, "%I:%M %p").time()

            # combine date and new start to single datetime object
            combined_datetime = datetime.datetime.combine(date_object, new_start_object)

            # get new duration in hours and seconds
            new_dur_hours = duration_box.get()
            new_dur_seconds = datetime.timedelta(seconds=(float(new_dur_hours) * 3600))

            # calculate new end time, and convert to a string time
            new_end = combined_datetime + datetime.timedelta(hours=float(new_dur_hours))
            new_end_str = new_end.strftime("%I:%M %p")

            # update activity in table
            tree.item(selected, text="", values=(selected_id, selected_job, new_desc, date, new_start, new_end_str, new_dur_hours))
            
            # update activity in database
            did_edit = db.edit_activity(rowid=selected_id, job=selected_job, description=new_desc, start=combined_datetime, duration=new_dur_seconds)

            # determine if the activity was also edited in the database
            if did_edit:
                # close the edit window
                edit_window.destroy()

                # message that shows the activity was edited successfully
                messagebox.showinfo("Edit Success", "Edited activity succesfully.")
            else:
                # close the edit window
                edit_window.destroy()

                # message that shows the activity failed to be edited in the database
                messagebox.showerror("Edit Failure", "Failure to edit activity in database")

        # confirm button to update activity
        confirm_button = tk.Button(edit_window, text = "Confirm", command = edit_activity_helper, height = 3, width = 15)
        confirm_button.grid(row=4, column=0)


    def exportToSpreadsheet():
        # export the data to a csv file
        write_work_list('timesheet.csv', db, start_date, end_date)

        # Show messagebox indicating export was successful
        messagebox.showinfo("Export Success", "Exported to spreadsheet file 'timesheet.csv'")


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
        deleteButton = tk.Button(window, text = "Delete", command=delete_activity, height=3, width=15, bg="red", fg="white")
        deleteButton.pack(side=tk.LEFT, padx=10)

        # edit activity to edit a certain activity
        editButton = tk.Button(window, text="Edit", command=edit_activity, height=3, width=15, bg="blue", fg="white")
        editButton.pack(side=tk.LEFT, padx = 10)

        exportButton = tk.Button(window, text="export", command=exportToSpreadsheet, height=3, width=15, bg="green", fg="white")
        exportButton.pack(side=tk.RIGHT, padx=10)

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
    end = datetime.date(2021, 6, 1)

    # add sample data
    entries = db.debug_get_all()
    if len(entries) == 0:
        db.add_activity("Office Hours 1", datetime.datetime(2021, 5, 18, 11, 0), datetime.timedelta(hours=1))
        db.add_activity("Office Hours 2", datetime.datetime(2021, 5, 19, 11, 0), datetime.timedelta(hours=2))
        db.add_activity("Office Hours 3", datetime.datetime(2021, 5, 20, 11, 0), datetime.timedelta(hours=5))
        db.add_activity("Office Hours 4", datetime.datetime(2021, 5, 21, 9, 0), datetime.timedelta(hours=3))
        db.add_activity("Office Hours 5", datetime.datetime(2021, 5, 22, 13, 0), datetime.timedelta(hours=3))
        db.add_activity("Office Hours 6", datetime.datetime(2021, 5, 23, 14, 0), datetime.timedelta(hours=3))
        db.add_activity("Office Hours 7", datetime.datetime(2021, 5, 24, 12, 0), datetime.timedelta(hours=2))
        db.add_activity("Office Hours 8", datetime.datetime(2021, 5, 25, 10, 0), datetime.timedelta(hours=3))
        db.add_activity("Office Hours 9", datetime.datetime(2021, 5, 26, 8, 0), datetime.timedelta(hours=4))
        db.add_activity("Office Hours 10", datetime.datetime(2021, 5, 27, 9, 0), datetime.timedelta(hours=5))
        db.add_activity("Office Hours 11", datetime.datetime(2021, 5, 28, 8, 0), datetime.timedelta(hours=6))
        db.add_activity("Office Hours 12", datetime.datetime(2021, 5, 29, 10, 0), datetime.timedelta(hours=6))
        db.add_activity("Office Hours 13", datetime.datetime(2021, 5, 30, 11, 0), datetime.timedelta(hours=2))
        db.add_activity("Office Hours 14", datetime.datetime(2021, 5, 31, 11, 0), datetime.timedelta(hours=5))

    display_timesheet(db, start, end)


if __name__ == '__main__':
    main()
