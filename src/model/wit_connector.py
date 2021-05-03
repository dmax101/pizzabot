from wit import Wit

class Wit_Connector:
  def __init__(self):
    self.client = Wit("$WIT_TOKEN")
    print("$WIT_TOKEN")

  def send_test_message(self):
    self.client.message('Olá! Gostaria de uma pizza!')
    return self.client

  
client = Wit_Connector()