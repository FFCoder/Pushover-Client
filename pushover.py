import requests

class PushoverPriority:
    NOALERT = -2,
    QUIET = -1,
    HIGH = 1,
    CONFIRM_NEEDED = 2

class PushoverClient(object):
    API_ENDPOINT = "https://api.pushover.net/1/messages.json"
    def __init__(self, appToken: str):
        """ Constructor function that takes a Pushover Application Token """
        self.token = appToken
    def sendMessage(self, user: str, message: str, title: str=None, priority: PushoverPriority=None):
        """ Sends a message to a user.
        Parameters
        ----------
        user : str, 
            The user token for the user that you wish to send a message to.
        message : str, 
            The actual message that you wish to send.
        title : str, 
            Per PushoverAPI Docs: your message's title, otherwise your app's name is used 
        priority: str
        """"
