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

        # Create the table if it doesn't already exist. Note the columns are defined here
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
        '''Creates an activity given a description, start time, and duration. Returns the row
        id of that insert if successful, -1 if not.

        Sample usage:
        >>> x = DatabaseManger("CIS 211 LA")
        >>> start = datetime.datetime(2021, 5, 4, 12, 0)
        >>> duration = datetime.timedelta(hours=4)
        >>> self.add_activitiy("Office hours", start, duration)
        '''
        try: 
            # Attempt to insert the requested activity into the database. We insert using the job, description, start_time, and duration
            self.cur.execute('''INSERT INTO activities
                (job, desc, start_time, duration) 
                values 
                (?, ?, ?, ?)
            ''', (self.job, desc, start, duration.total_seconds()))

            # Commit that statement to the database
            self.con.commit()

            # We return the id of the row that we just created
            return self.cur.lastrowid
        except Exception as e:
            print(e)
            # If we fail somewhere in the above try statement, we must rollback (reset) the
            # transaction and return -1, meaning that we failed.
            self.con.rollback()
            return -1

    def delete_activity(self, id: int) -> bool:
        '''Deletes an actvity given an ID. Returns true if successful and false if not'''
        try:
            # Attempt to delete from the database where the rowid matches
            self.cur.execute('DELETE FROM activities where (rowid = ?)',
                    (id,) # Note that the comma after id causes this to be a tuple, which is requried
            )
            self.con.commit()

            # If there was a row that was changed (deleted) we return true: successful
            if self.cur.rowcount == 1:
                return True
            else:
                # Otherwise, we didn't delete anything, return false
                return False
        except:
            # We also return false if there was an error
            # TODO: We may want to do some further error handling here. Either
            # printing that there is an error or re-init'ing the database
            return False


    def debug_get_all(self) -> list:
        '''Returns every single element from the database with a rowid. See 
        get_activities_within_range() docstring for details on formatting

        Not supposed to be used in production. Very helpful for testing.
        '''
        self.cur.execute('SELECT rowid,* FROM activities order by start_time')
        return self.cur.fetchall()

    def get_activities_within_range(self, start: datetime.datetime, end: datetime.datetime):
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

        # We execute a select statement that selects activities that _start_ in the
        # specified range and then return what it yields
        self.cur.execute('''
                SELECT rowid,* FROM activities where not (start_time < ? or ? < start_time)
                and (job=?)
                order by start_time
                ''', 
                (start, end, self.job)
        )

        return self.cur.fetchall()
    
    def get_activity(self, rowid: int) -> tuple:
        '''
        Returns a single activity as a tuple of (
            rowid:int, job:str, description:str, start:datetime.datetime, duration:int
        )

        Returns None if the object doesn't exist. 
        '''

        # We select a row based on the rowid and return what that statement yields
        # NOTE: This is not bound by self.job.
        self.cur.execute('Select rowid,* FROM activities where rowid=?',
                (rowid,)
        )

        return self.cur.fetchone()

    def edit_activity(self, rowid: int, job: str = None, description :str = None, 
            start: datetime.datetime = None, duration: datetime.timedelta = None) -> bool:
        '''
        Edits fields of a activity. Only edits fields that are not None.

        >>> edit_activity(3, description="Help hours")
        >>> edit_activity(3, duration=datetime.timedelta(hours=1.10))
        '''

        # Keep track of how many rows get updated
        max_rowcount = 0

        # Convert duration to seconds or None (if unspecified) for the following line
        dur = None if duration is None else duration.seconds

        # Store all of the fields in tuples, formatted as (field_name, value). Note that
        # field_name must exactly match what it is in the SQL database
        fields = [('job', job), ('desc', description), ('start_time', start), ('duration', dur)]

        # we loop through each field
        for field in fields:
            if field[1] is None:
                # Skipping the ones where the value is None
                continue
            # And update the field of that rowid with the value
            self.cur.execute(f'UPDATE activities SET {field[0]} = ? WHERE rowid = ?', 
                    (field[1], rowid))
            self.con.commit()

            # And, whenever we make a change, we track the total number of rows modified.
            # Remember that the rowid is the same each time, so we want to track if the
            # number of rows modified is 0 or 1.
            max_rowcount = max(max_rowcount, self.cur.rowcount)

        # if in our tracking of modified rows we modified a row, we return True, otherwise False
        if max_rowcount == 1:
            return True
        else:
            return False


    def reset_db(self, sure: str=''):

        # If we got a sure response, we delete everything in the database and re-create it
        if sure == 'yes':
            self.cur.execute('''
                drop table activities;
            ''')
            self.con.commit()
            self.__init__(self.job, self.filename)
        else:
            # Otherwise, print out some warning and instructions to delete everything
            print("Are you sure you'd like to delete this database and everything")
            print("in it? If so, call this function with 'yes' as an argument")
            print("example: db.reset_db('yes')")

