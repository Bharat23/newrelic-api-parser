import unittest
import os

from NewRelic import Config
from NewRelic.REST.AlertsConditions import AlertsConditions

class AlertsConditionsTest(unittest.TestCase):

    def test_list(self):
        API_KEY = os.environ.get('NEWRELIC_API_KEY')
        application = AlertsConditions(API_KEY=API_KEY)
        self.assertNotEqual(application.get_list(policy_id=12334), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)