from dbm import DatabaseManager
import datetime

import unittest

class DatabaseBasicTests(unittest.TestCase):
    def setUp(self):
        self.jobname = "test job"
        self.dbm = DatabaseManager(self.jobname, "test.db")
        self.dbm.reset_db(sure='yes')

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

    def test_update_activities(self):
        # Dates for testing
        start = datetime.datetime.now()
        duration = datetime.timedelta(minutes=30)
        new_start = datetime.datetime(2021, 5, 10, 12, 0)
        new_duration = datetime.timedelta(hours=1)

        # Add some sample events. Keep track of their id's
        ids = []
        ids.append(self.dbm.add_activity("activity 1", start, duration))
        ids.append(self.dbm.add_activity("activity 2", start, duration))
        ids.append(self.dbm.add_activity("activity 3", start, duration))
        ids.append(self.dbm.add_activity("activity 4", start, duration))
        ids.append(self.dbm.add_activity("activity 5", start, duration))

        # Make sure adding those activities didn't fail
        self.assertTrue(-1 not in ids)

        # Get the length of all activities before we begin editing them
        activityCount = len(self.dbm.debug_get_all())

        # Test that editing in a way that changes a row returns true
        self.assertTrue(self.dbm.edit_activity(ids[0], description="ACTIVITY 1") )
        self.assertTrue(self.dbm.edit_activity(ids[1], start=new_start))
        self.assertTrue(self.dbm.edit_activity(ids[2], duration=new_duration))
        self.assertTrue(self.dbm.edit_activity(ids[4], job=self.jobname + ' 2'))

        # No fields = no changed rows
        self.assertFalse(self.dbm.edit_activity(ids[3]))

        # Should be the exact same number of activities
        self.assertEqual(activityCount, len(self.dbm.debug_get_all()))

        # Changes an activity that doesn't (shouldn't) exist
        self.assertFalse(self.dbm.edit_activity(ids[4] + 1000, description="hello"))

        # Multiple edits
        self.assertTrue(self.dbm.edit_activity(ids[0], start=new_start, duration=new_duration))

        # Test that things are actually as we expect them to be
        acts = []
        acts += [(ids[0], self.jobname, "ACTIVITY 1", new_start, new_duration.seconds)]
        acts += [(ids[1], self.jobname, "activity 2", new_start, duration.seconds)]
        acts += [(ids[2], self.jobname, "activity 3", start, new_duration.seconds)]
        acts += [(ids[3], self.jobname, "activity 4", start, duration.seconds)]
        acts += [(ids[4], self.jobname + ' 2', "activity 5", start, duration.seconds)]
        for i in range(5):
            activity = self.dbm.get_activity(ids[i])
            self.assert_activities_equal(activity, acts[i])

    def test_range_select(self):
        # Reset the database. Check that it's empty
        self.dbm.reset_db(sure='yes')
        self.assertEqual(0, len(self.dbm.debug_get_all()))

        # Store the length of an hour for later user
        anhour = datetime.timedelta(seconds=3600)

        # Insert a few items into the database. See the first parameter for a
        # short description on what we're testing.
        ids = []
        ids.append(self.dbm.add_activity("clean in the middle of the month", datetime.datetime(2021, 5, 15, 12, 0), anhour))
        ids.append(self.dbm.add_activity("near start of month", datetime.datetime(2021, 5, 1, 12, 0), anhour))
        ids.append(self.dbm.add_activity("exact start of month", datetime.datetime(2021, 5, 1, 0, 0), anhour))
        ids.append(self.dbm.add_activity("before start of month", datetime.datetime(2021, 4, 30, 23, 59), anhour))
        ids.append(self.dbm.add_activity("near end of month", datetime.datetime(2021, 5, 30, 12, 0), anhour))
        ids.append(self.dbm.add_activity("minute before to end of month", datetime.datetime(2021, 5, 30, 23, 59), anhour))
        ids.append(self.dbm.add_activity("exact end of month", datetime.datetime(2021, 6, 1, 0, 0), anhour))
        ids.append(self.dbm.add_activity("after end of month", datetime.datetime(2021, 6, 2, 0, 0), anhour))

        # Confirm none of them failed
        self.assertTrue(-1 not in ids)

        # Helps to count how many there are
        self.assertEqual(len(ids), 8)

        # Define the range of time we're interested in: the month of may, 2021
        start_of_may = datetime.datetime(2021, 5, 1, 0, 0)
        start_of_june = datetime.datetime(2021, 6, 1, 0, 0)

        # Get activities within that range
        acts = self.dbm.get_activities_within_range(start_of_may, start_of_june)

        # Confirm that there are as many activities as we expect
        self.assertEqual(6, len(acts))

        # Create a list of ids from the list of activities
        acts_ids = [act[0] for act in acts]

        # Check that the ones that we expect to be in activities are in there,
        # that the ones that we do not expect to be in there are not in there
        self.assertTrue(ids[0] in acts_ids)
        self.assertTrue(ids[1] in acts_ids)
        self.assertTrue(ids[2] in acts_ids)
        self.assertTrue(ids[3] not in acts_ids)
        self.assertTrue(ids[4] in acts_ids)
        self.assertTrue(ids[5] in acts_ids)
        self.assertTrue(ids[6] in acts_ids)
        self.assertTrue(ids[7] not in acts_ids)
             
    
    def assert_activities_equal(self, act1, act2):
        '''Check if two activities are equal'''
        for i in range(len(act1)):
            self.assertEqual(act1[i], act2[i])

    def tearDown(self):
        self.dbm.reset_db(sure='yes')

if __name__=='__main__':
    # When we run this file, run the tests
    unittest.main()

