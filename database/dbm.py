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

        self.filename = filename

        # Connect to the timeworked database file and get it's cursor
        # which is required to operate on the file
        self.con = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS activities
            (
             `job` VARCHAR(100) DEFAULT '',  
             `desc` VARCHAR(100) DEFAULT '',  
             `start_time` TIMESTAMP NOT NULL,  
             `duration` INT NOT NULL
             )
        ''')

    def __del__(self):
        '''Close the connection to the database on deletion'''
        self.con.close()

    def add_activity(self, desc: str, start: datetime.datetime, duration: datetime.timedelta) -> int:
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
            return self.cur.lastrowid
        except:
            self.con.rollback()
            return -1
    def delete_activity(self, id: int) -> int:
        try:
            self.cur.execute('DELETE FROM activities where (rowid = ?)',
                    (id,)
            )
            self.con.commit()
            if self.cur.rowcount == 1:
                return True
            else:
                return False
        except:
            return False


    def debug_get_all(self) -> list:
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

        self.cur.execute('Select rowid,* FROM activities where rowid=?',
                (rowid,)
        )

        return self.cur.fetchone()

    def edit_activity(self, rowid: int, job :str = None, description :str = None, 
            start: datetime.datetime = None, duration: datetime.timedelta = None) -> True:
        '''
        Edits fields of a activity. Only edits fields that are not None.

        >>> edit_activity(3, description="Help hours")
        >>> edit_activity(3, duration=datetime.timedelta(hours=1.10))
        '''

        max_rowcount = 0

        dur = None if duration is None else duration.seconds()
        fields = [('job', job), ('desc', description), ('start_time', start), ('duration', dur)]

        for field in fields:
            if field[1] is None:
                continue
            self.cur.execute(f'UPDATE activities SET {field[0]} = ? WHERE rowid = ?', (field[1], rowid))
            self.con.commit()
            max_rowcount = max(max_rowcount, self.cur.rowcount)

        if max_rowcount == 1:
            return True
        else:
            return False


    def reset_db(self):
        self.cur.execute('''
            drop table activities;
        ''')
        self.con.commit()
        self.__init__(self.job, self.filename)


        
        


    
