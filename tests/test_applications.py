import unittest
import os

from NewRelic import Config
from NewRelic.REST.Applications import Applications

class ApplicationTest(unittest.TestCase):

    def test_list(self):
        API_KEY = os.environ.get('NEWRELIC_API_KEY')
        application = Applications(API_KEY=API_KEY)
        self.assertNotEqual(application.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)