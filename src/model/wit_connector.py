from wit import Wit
import pprint as pp
import os

class Wit_Connector:
    def __init__(self):
        self.client = Wit(os.environ['WIT_TOKEN'])

    def send_test_message(self):
        resp = self.client.message("test message")
        pp.pprint('Yay, got Wit.ai response: ' + str(resp))
    
    def message(self, message):
        resp = self.client.message(message)
        return resp