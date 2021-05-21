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
        self.con = sqlite3.connect('timeworked.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS activities
            (
             `job` VARCHAR(100) DEFAULT '',  
             `desc` VARCHAR(100) DEFAULT '',  
             `start_time` DATETIME NOT NULL,  
             `duration` INT NOT NULL
             )
        ''')

    def __del__(self):
        '''Close the connection to the database on deletion'''
        self.con.close()

    def add_activity(self, desc: str, start: datetime.datetime, duration: datetime.timedelta) -> bool:
        '''Creates an activity given a description, start time, and duration.

        Sample usage:
        >>> x = DatabaseManger("CIS 211 LA")
        >>> start = datetime.datetime(2021, 5, 4, 12, 0)
        >>> duration = datetime.timedelta(hours=4)
        >>> self.add_activitiy("Office hours", start, duration)
        '''
        try: 
            self.cur.execute('''INSERT INTO activities
                (job, desc, start_time, duration)
                values
                (?, ?, ?, ?)
            ''', (self.job, desc, start, duration.total_seconds()))

            self.con.commit()
            return True
        except:
            self.con.rollback()
            return False


    def debug_get_all(self):
        self.cur.execute('SELECT rowid,* FROM activities')
        return self.cur.fetchall()

    def get_activies_within_range(self, start: datetime.datetime, end: datetime.datetime):
        '''
        Returns a list of all activities within a certain range as a list of tuples of (
            rowid:int, job:str, description:str, start:datetime.datetime, duration:int
        )


        Sample usage:
        >>> x = DatabaseManager("CIS 211 LA")
        >>> now = datetime.datetime.now()
        >>> # Gets all activities within the last 3 hours
        >>> x.get_activies_within_range(now - datetime.timedelta(hours=3), now)
        '''
        self.cur.execute('''
                SELECT rowid,* FROM activities where not (start_time < ? or ? < start_time)''', 
                (start, end)
        )

        return self.cur.fetchall()
    
    def get_activity(self, rowid: int):
        '''
        Returns a single activity as a tuple of (
            rowid:int, job:str, description:str, start:datetime.datetime, duration:int
        )

        '''

        self.cur.execute('''
                Select rowid,* FROM activities where rowid=?''',
                (rowid)
        )

        return self.cur.fetchall()
        
        


    
