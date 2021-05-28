from database.dbm import DatabaseManager
import preview
import datetime
import unittest

class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.jobname = "test job"
        self.dbm = DatabaseManager(self.jobname, "test.db")

    def test_display_timesheet(self):
        # start and end dates
        start = datetime.date(2021, 5, 18)
        end = datetime.date(2021, 5, 31)

        # add sample data
        entries = self.dbm.debug_get_all()
        if len(entries) == 0:
            self.dbm.add_activity("Office Hours 1", datetime.datetime(2021, 5, 18), datetime.timedelta(hours=2))
            self.dbm.add_activity("Office Hours 2", datetime.datetime(2021, 5, 19), datetime.timedelta(hours=3))
            self.dbm.add_activity("Office Hours 3", datetime.datetime(2021, 5, 20), datetime.timedelta(hours=4))

        self.assertTrue(preview.display_timesheet(self.dbm, start, end))

if __name__=='__main__':

    # run the tests
    unittest.main()