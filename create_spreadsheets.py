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
import xlrd
import openpyxl
from io import StringIO


def write_work_list(filename, number):
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    start_datetime = datetime.datetime.combine(start, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end, datetime.datetime.min.time())
    db = dbm.DatabaseManager('CIS 422 TA')
    work = db.get_activies_within_range(start_datetime, end_datetime)
    print(work)

    with open('timesheet.csv', 'w', newline='') as csvfile:
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
            if '.' in activity[3]:
                date_t = datetime.datetime.strptime(activity[3], '%Y-%m-%d %H:%M:%S.%f')
                date = date_t.strftime("%m/%d/%Y")
                start = date_t.strftime("%H:%M:%S.%f")
                print("date:", date)
                print("start:", start)
            else:
                date_t = datetime.datetime.strptime(activity[3], '%Y-%m-%d %H:%M:%S')
                date = date_t.strftime("%m/%d/%Y")
                start = date_t.strftime("%H:%M:%S")
                print("date", date)
                print("start:", start)

            duration = str(datetime.timedelta(seconds=activity[4]))
            duration_format = duration[:-3]
            print("duration:", duration_format)

            end = str(date_t + datetime.timedelta(seconds=activity[4]))
            end_time = end[11:]
            if end_time[0] == '0':
                end_time = end[12:]
            print("end", end_time)

            total += activity[4]
            tmp = [job_id, job, des, date, start, end_time, duration_format]
            writer.writerow(tmp)

            # writer.writerow({'Job_ID': job_id, "Job": job, "Description": des,
            #                  "Date": date, "Start": start, "End": end_time, "Duration": duration_format})

        total_time = str(datetime.timedelta(seconds=total))
        total_time_format = total_time[:-3]
        print("total time", total_time_format)
        writer.writerow([" ", " ", "total time", " ", " ", " ", total_time_format])




        # date = datetime.strptime(activity[3], '%Y-%m-%d %H:%M:%S.%f').strftime('%m/%d/%Y')
        # print("date", date)
        # duration is [4]
        # print("day", activity[3].strftime('%a %m/%d/%y'))
        # print("start", (activity[3]).strftime('%I:%M %p'))
        # print("end", (activity[3] + datetime.timedelta(seconds=activity[4])).strftime('%I:%M %p'))
        # duration = datetime.timedelta(seconds=activity[4])
        # print(f"duration {round(duration.seconds/3600, 3)}")
    #     total += activity[4]
    # total_time = round(total/3600, 2)


write_work_list(" ", 0)
