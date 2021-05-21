from dbm import DatabaseManager
import datetime

import unittest

class DatabaseBasicTests(unittest.TestCase):
    def setUp(self):
        self.jobname = "test job"
        self.dbm = DatabaseManager(self.jobname, "test.db")
        self.dbm.reset_db()

    def test_add_activity(self):
        # Get activities before we start in case another test forgets to clean them up
        old_activities = self.dbm.debug_get_all()

        # Set up some times
        now = datetime.datetime.now()
        anhour = datetime.timedelta(seconds=3600)

        # Insert a sample activity that started an hour ago and ends now
        id = self.dbm.add_activity("Sample Activity", now-anhour, anhour)

        # Check was successful
        self.assertNotEqual(id, -1)

        # Check that there is exactly one more thing in the database
        activities = self.dbm.debug_get_all()
        self.assertEqual(len(old_activities) + 1, len(activities))

        # Retrieve the activity
        thisJob = self.dbm.get_activity(id)

        # Check exists
        self.assertIsNotNone(thisJob)

        # Check that this activity has the correct information 
        self.assertEqual(thisJob[0], id)
        self.assertEqual(thisJob[1], self.jobname)
        self.assertEqual(thisJob[2], "Sample Activity")
        self.assertEqual(thisJob[3], now-anhour)
        self.assertEqual(thisJob[4], 3600)

        self.assertTrue(self.dbm.delete_activity(id))

    def test_delete_activities(self):
        # Add some dates just so we can quickly add activies
        start = datetime.datetime.now()
        duration = datetime.timedelta(seconds=100)

        # Add some sample events, keep track of their id's
        ids = []
        ids.append(self.dbm.add_activity("activity 1", start, duration))
        ids.append(self.dbm.add_activity("activity 2", start, duration))
        ids.append(self.dbm.add_activity("activity 3", start, duration))
        ids.append(self.dbm.add_activity("activity 4", start, duration))
        ids.append(self.dbm.add_activity("activity 5", start, duration))

        # Make sure adding those activities didn't fail
        self.assertTrue(-1 not in ids)

        # Get the length of all activities before we begin deleting them
        activityCount = len(self.dbm.debug_get_all())

        # Try deleting some of them, double deleting one should return false
        self.assertTrue(self.dbm.delete_activity(ids[1]))
        self.assertFalse(self.dbm.delete_activity(ids[1]))
        self.assertTrue(self.dbm.delete_activity(ids[2]))

        # There should be 2 less activities
        self.assertEqual(activityCount-2, len(self.dbm.debug_get_all()))

    def tearDown(self):
        self.dbm.reset_db()

if __name__=='__main__':
    # When we run this file, run the tests
    unittest.main()

