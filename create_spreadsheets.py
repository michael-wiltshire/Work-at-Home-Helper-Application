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

def write_work_list(filename, number):

    start = datetime.date(2021, 5, 18)
    end = datetime.date(2021, 5, 31)
    start_datetime = datetime.datetime.combine(start, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(end, datetime.datetime.min.time())
    db = dbm.DatabaseManager('CIS 422 TA')
    work = db.get_activies_within_range(start_datetime, end_datetime)
    print(work)
    # with open(output_filename, mode='w') as csv_file:
    #     fieldnames = ['Full name', 'Phone', 'Email', 'Score']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #
    #     writer.writeheader()
    #     for vaccinee in vaccinees:
    #         writer.writerow({'Full name': vaccinee.fullname, "Phone": vaccinee.phone, "Email": vaccinee.email, "Score": vaccinee.score})

write_work_list(" ", 0)
