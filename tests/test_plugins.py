import unittest
import os

from NewRelicApiParser import Config
from NewRelicApiParser.REST.Plugins import Plugins

class PluginsTest(unittest.TestCase):

    def test_list(self):
        API_KEY = os.environ.get('NEWRELIC_API_KEY')
        plugins = Plugins(API_KEY=API_KEY)
        self.assertNotEqual(plugins.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)