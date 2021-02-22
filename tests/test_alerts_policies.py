import unittest
import os

from NewRelic import Config
from NewRelic.REST.AlertsPolicies import AlertsPolicies

class AlertsPoliciesTest(unittest.TestCase):

    def test_list(self):
        API_KEY = os.environ.get('NEWRELIC_API_KEY')
        application = AlertsPolicies(API_KEY=API_KEY)
        self.assertNotEqual(application.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)