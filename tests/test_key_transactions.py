import unittest
import os

from NewRelicApiParser import Config
from NewRelicApiParser.REST.KeyTransactions import KeyTransactions


class KeyTransactionsTest(unittest.TestCase):
    def test_list(self):
        API_KEY = os.environ.get("NEWRELIC_API_KEY")
        key_transactions = KeyTransactions(API_KEY=API_KEY)
        self.assertNotEqual(key_transactions.get_list(), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
