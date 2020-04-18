import unittest
import os

from NewRelic import Config
from NewRelic.REST.BrowserApplications import BrowserApplications

class BrowserApplicationTest(unittest.TestCase):

    def test_list(self):
        """Should not return None"""
        self.shortDescription()
        Config.API_KEY = os.environ.get('NEWRELIC_API_KEY')
        browser_application = BrowserApplications()
        self.assertNotEqual(browser_application.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)