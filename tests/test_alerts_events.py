import unittest
import os

from NewRelicApiParser import Config
from NewRelicApiParser.REST.AlertsEvents import AlertsEvents

class AlertsEventsTest(unittest.TestCase):

    def test_list(self):
        API_KEY = os.environ.get('NEWRELIC_API_KEY')
        alerts_events = AlertsEvents(API_KEY=API_KEY)
        self.assertNotEqual(alerts_events.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)