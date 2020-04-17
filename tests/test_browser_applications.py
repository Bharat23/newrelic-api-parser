import unittest

from NewRelic import Config
from NewRelic.REST.BrowserApplications import BrowserApplications

class BrowserApplicationTest(unittest.TestCase):

    def test_list(self):
        Config.API_KEY = 'decb73771a6fc514b98ca9ba594b1accd305b3412884db6'
        browser_application = BrowserApplications()
        self.assertNotEqual(browser_application.get_list(), None) 

if __name__ == "__main__":
    unittest.main()