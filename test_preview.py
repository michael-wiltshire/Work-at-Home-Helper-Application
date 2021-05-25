from database.dbm import DatabaseManager
import preview
import datetime
import unittest

class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.jobname = "test job"
        self.dbm = DatabaseManager(self.jobname, "test.db")

    def test_display_spreadsheet(self):
        # start and end dates
        start = datetime.date(2021, 5, 18)
        end = datetime.date(2021, 5, 31)

        # add sample data
        self.dbm.add_activity("Office Hours 2", datetime.datetime(2021, 5, 19), datetime.timedelta(hours=3))
        self.dbm.add_activity("Office Hours 3", datetime.datetime(2021, 5, 20), datetime.timedelta(hours=3))
        self.dbm.add_activity("Office Hours 4", datetime.datetime(2021, 5, 21), datetime.timedelta(hours=3))

        self.assertTrue(preview.display_timesheet(self.dbm, start, end))

if __name__=='__main__':
    # run the tests
    unittest.main()