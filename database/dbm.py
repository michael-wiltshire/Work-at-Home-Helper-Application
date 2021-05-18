'''
CIS 422 Group 1


'''

import sqlite3
import datetime

class DatabaseManager:

    def __init__(self, job: str, filename: str='timeworked.db') -> sqlite3.Cursor:
        '''Creates a connection to a database that will be interacted with for the rest
        of the lifespan of the class'''

        # Jobs should be managed one at a time
        self.job = job

        # Connect to the timeworked database file and get it's cursor
        # which is required to operate on the file
        self.con = sqlite3.connect('timeworked.db')
        self.cur = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS activities
            (
             `job` VARCHAR(100) DEFAULT '',  
             `desc` VARCHAR(100) DEFAULT '',  
             `start_time` DATETIME NOT NULL,  
             `durration` INT NOT NULL
             )
        ''')

    def __del__(self):
        '''Close the connection to the database on deletion'''
        self.con.close()

    def add_activity(self, desc: str, start: datetime.datetime, durration: datetime.timedelta):
        self.cur.execute('''INSERT INTO activities
            (job, desc, start_time, durration)
            values
            (?, ?, ?, ?)
        ''', (self.job, desc, start, durration.total_seconds()))

        self.con.commit()

    def debug_get_all(self):
        self.cur.execute('SELECT * FROM activities')
        print(self.cur.fetchall())
        

        
        


    
