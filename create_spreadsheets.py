"""
CIS 422: Project 2: Work at home helper
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files.
"""

from database import dbm
import datetime
import sys
import os
import csv
from io import StringIO


def write_work_list(filename, db, start, end):
    start_datetime = datetime.datetime.combine(start, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end, datetime.datetime.min.time())
    # db = dbm.DatabaseManager('CIS 422 TA')
    work = db.get_activities_within_range(start_datetime, end_datetime)
    print(work)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Job_ID', 'Job', 'Description', 'Date', 'Start', 'End', 'Duration']
        writer = csv.writer(csvfile)

        # writer.writeheader()
        writer.writerow(fieldnames)

        total = 0
        for activity in work:
            print(activity)
            job_id = activity[0]
            print("job id:", job_id)
            # job is [1]
            job = activity[1]
            print("job:", job)
            des = activity[2]
            print("description", des)
            #print(len(activity[3]))
            date_t = activity[3]
            date = date_t.strftime("%m/%d/%Y")
            start = date_t.strftime("%I:%M %p")
            print("date", date)
            print("start:", start)

            # duration = str(datetime.timedelta(seconds=activity[4]))
            # duration_format = duration[:-3]
            # print("duration:", duration_format)
            duration = str(round(activity[4] / 3600, 2))

            end = (date_t + datetime.timedelta(seconds=activity[4]))
            end_time = end.strftime("%I:%M %p")
            print("end", end_time)

            total += activity[4]
            tmp = [job_id, job, des, date, start, end_time, duration]
            writer.writerow(tmp)

            # writer.writerow({'Job_ID': job_id, "Job": job, "Description": des,
            #                  "Date": date, "Start": start, "End": end_time, "Duration": duration_format})

        total_time_format = str(round(total / 3600, 2))
        print("total time", total_time_format)
        writer.writerow([" ", " ", "total time", " ", " ", " ", total_time_format])

def main():
    jobname = "sample job"
    db = dbm.DatabaseManager(jobname, 'sample.db')
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    write_work_list('timesheet.csv', db, start, end)

if __name__=='__main__':
    main()
