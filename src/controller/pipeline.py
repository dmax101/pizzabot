from model.witconnector import WitConnector
from utils.log import log

class Pipeline:
    def __init__(self):
        self.on_start = True
        self.on_greeting = True
        self.on_choosing_products = True
        self.on_fullfilling_sc = True
        self.on_transation_db = True
        self.on_charging = True
        self.on_canceling_operation = True
        self.on_end_operation = True

    def response(self, message, waiting_response, code=0) -> dict:
        log("\n\tSending Message: {}\n\tWaiting response: {}".format(message, waiting_response), location=[self])
        return {
            "message": message,
            "waiting_response": waiting_response,
            "code": code
        }
    
    def canceling_operation(self, user_message) -> dict:
        if self.on_canceling_operation:
            message = "Operação cancelada pelo usuário"
            waiting_response = False

            self.on_canceling_operation = False
            
            return self.response(message, waiting_response, -1)

    def end_operation(self, user_message) -> dict:
        if self.on_end_operation:
            message = user_message
            waiting_response = True

            self.on_end_operation = False
            
            return self.response(message, waiting_response)

    def charging(self, user_message) -> dict:
        if self.on_charging:
            message = "charging"
            waiting_response = False

            self.on_charging = False
            
            return self.response(message, waiting_response)

        else:
            return self.end_operation(user_message)
    
    def transation_db(self, user_message) -> dict:
        if self.on_transation_db:
            message = "transation"
            waiting_response = False

            self.on_transation_db = False
            
            return self.response(message, waiting_response)

        else:
            return self.charging(user_message)

    def fullfilling_sc(self, user_message) -> dict:
        if self.on_fullfilling_sc:
            message = "fullfilling"
            waiting_response = False

            self.on_fullfilling_sc = False
            
            return self.response(message, waiting_response)

        else:
            return self.transation_db(user_message)

    def choosing_products(self, user_message) -> dict:
        if self.on_choosing_products:
            message = "choosing products"
            waiting_response = False

            self.on_choosing_products = False
            
            return self.response(message, waiting_response)

        else:
            return self.fullfilling_sc(user_message)

    def greeting(self, user_message) -> dict:
        if self.on_greeting:
            message = "greeting: " + user_message
            waiting_response = False

            self.on_greeting = False
            
            return self.response(message, waiting_response)

        else:
            return self.choosing_products(user_message)

    def start(self, user_message) -> dict:
        if self.on_start:
            message = "Acionando minha rede positrônica!"
            waiting_response = False

            self.on_start = False

            return self.response(message, waiting_response)

        else:
            return self.greeting(user_message)
