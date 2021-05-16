'''
CIS 422 Group 1


'''

import sqlite3

def connect_and_create(filename='timeworked.db': str) -> sqlite3.Cursor:
    '''
    Connects to a database file and returns a 'cursor' to that database.
    This object is then thrown into other functions to do the various needed
    operations

    '''
    # Connect to the timeworked database file and get it's cursor
    # which is required to operate on the file
    con = sqlite3.connect('timeworked.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS activities
        (

    ''')
    return



    
