import unittest
import os

from NewRelic import Config
from NewRelic.REST.Plugins import Plugins

class PluginsTest(unittest.TestCase):

    def test_list(self):
        Config.API_KEY = os.environ.get('NEWRELIC_API_KEY')
        plugins = Plugins()
        self.assertNotEqual(plugins.get_list(), None) 

if __name__ == "__main__":
    unittest.main(verbosity=2)