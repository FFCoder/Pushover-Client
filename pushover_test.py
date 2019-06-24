import unittest
import os
from pushover import PushoverClient

class TestPushoverClient(unittest.TestCase):
    def setUp(self):
        self.APP_KEY = os.environ['PUSHOVER_APP_KEY']
        self.TEST_USER = os.environ['TEST_USER_KEY']
        if "PUSHOVER_MESSAGE" in os.environ:
            self.MESSAGE = os.environ["PUSHOVER_MESSAGE"]
        else:
            self.MESSAGE = "UNITESTING PUSHOVER CLIENT"

        assert (self.TEST_USER != "") and (self.APP_KEY !="")
        self.client = PushoverClient(self.APP_KEY)
    def test_MessagePlain(self):
        assert(self.client.sendMessage(self.TEST_USER, self.MESSAGE) is True)
if __name__ == "__main__":
    unittest.main()