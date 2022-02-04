import unittest
import os

from NewRelicApiParser import Config
from NewRelicApiParser.REST.BrowserApplications import BrowserApplications


class BrowserApplicationTest(unittest.TestCase):
    def test_list(self):
        """Should not return None"""
        self.shortDescription()
        API_KEY = os.environ.get("NEWRELIC_API_KEY")
        browser_application = BrowserApplications(API_KEY=API_KEY)
        self.assertNotEqual(browser_application.get_list(), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
