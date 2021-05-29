"""
CIS 422: Project 2: Work at home helper
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files.
"""

from database import dbm
import datetime
import csv


def write_work_list(filename, db, start, end):
    start_datetime = datetime.datetime.combine(start, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end, datetime.datetime.min.time())
    work = db.get_activities_within_range(start_datetime, end_datetime)
    #print(work)

    with open(filename, 'w', newline='') as csv_file:
        """Create a csv file and write its first row with the elements we want"""
        fieldnames = ['Job_ID', 'Job', 'Description', 'Date', 'Start', 'End', 'Duration']
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)

        total = 0
        for activity in work:
            """to get the information in database and then put them into the spreadsheet"""
            #print(activity)
            job_id = activity[0]
            #print("job id:", job_id)
            job = activity[1]
            #print("job:", job)
            des = activity[2]
            #print("description", des)
            date_t = activity[3]
            date = date_t.strftime("%m/%d/%Y")
            start = date_t.strftime("%I:%M %p")
            #print("date", date)
            #print("start:", start)

            duration = str(round(activity[4] / 3600, 2))

            end = (date_t + datetime.timedelta(seconds=activity[4]))
            end_time = end.strftime("%I:%M %p")
            #print("end", end_time)

            total += activity[4]
            tmp = [job_id, job, des, date, start, end_time, duration]
            writer.writerow(tmp)

        total_time_format = str(round(total / 3600, 2))
        #print("total time", total_time_format)
        writer.writerow([" ", " ", "total time", " ", " ", " ", total_time_format])


def main():
    """main"""
    jobname = "sample job"
    db = dbm.DatabaseManager(jobname, 'sample.db')
    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    write_work_list('timesheet.csv', db, start, end)


if __name__=='__main__':
    main()
