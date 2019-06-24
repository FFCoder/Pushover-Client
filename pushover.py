""" Pushover Client 
    Author: Jonathon Chambers<jonathon@jonathonchambers.com>
"""

import sys
import requests
import logging

class PushoverPriority:
    """ Pushover Enums """
    NOALERT = -2
    QUIET = -1
    NORMAL = 0
    HIGH = 1
    CONFIRM_NEEDED = 2

class PushoverClient:
    API_ENDPOINT = "https://api.pushover.net/1/messages.json"
    def __init__(self, appToken: str):
        """ Constructor function that takes a Pushover Application Token """
        self.token = appToken
        self.setupLog()

    def setupLog(self):
        ## Setup Logging
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename = "PushOverClient.log",
                            level = logging.DEBUG,
                            format = LOG_FORMAT,
                            filemode = 'w')
        self.log = logging.getLogger("com.jonathonchambers.pushoverclient")


    def send_message(self, user: str, message: str, title: str = None, 
                     priority: PushoverPriority = None):
        """ Sends a message to a user.
        Parameters
        ----------
        user : str,
            The user token for the user that you wish to send a message to.
        message : str,
            The actual message that you wish to send.
        title : str, 
            Per PushoverAPI Docs: your message's title, otherwise your app's name is used 
        priority: PushoverPriority
            The Pushover Priority of the message
        """
        
        # Setup a dict for Pushover Variables
        d = {
            "token": self.token,
            "user": user,
            "message": message,
            "title": title,
            "priority": priority
        }
        self.log.debug("Data Variable: ")
        self.log.debug(d)
        req = requests.post(PushoverClient.API_ENDPOINT, data = d)

        if ((req.status_code == 200) or (req.status_code == 201)):
            return True
        else:
            self.log.error("Pushover Client Pushing Message Failed")
            self.log.debug(req.text)
            return False
