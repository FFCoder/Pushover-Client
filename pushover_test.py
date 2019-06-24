import unittest
import os
from pushover import PushoverClient, PushoverPriority

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
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE) is True)

    def test_Message_With_Title(self):
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE, "TEST TITLE") is True)

    def test_NOALERT_Message(self):
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE, 
                                        priority = PushoverPriority.NOALERT) is True)

    def test_QUIET_Message(self):
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE, 
                                        priority = PushoverPriority.QUIET) is True)  

    def test_HIGH_Message(self):
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE, 
                                        priority = PushoverPriority.HIGH) is True)
                            
    def test_CONFIRM_NEEDED_Message(self):
        assert(self.client.send_message(self.TEST_USER, self.MESSAGE, 
                                        priority = PushoverPriority.CONFIRM_NEEDED) is True)
if __name__ == "__main__":
    unittest.main()