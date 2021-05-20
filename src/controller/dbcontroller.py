from model.dbconnector import DbConnector
import os
import pprint as pp

class DbController:
    def __init__(self, collection):
        self.collection = collection[0]

    def post_one_doc(self, document):
        self.collection.insert_one(document)
    
    def get_one_doc(self, document):
        res = self.collection.find_one(document)
        return res

# cnn = DbConnector("pizzabot", os.environ["DB_PASSWORD"], "pizzabot")

# order_db = cnn.connect().orders

# order_handler = DbController([order_db])

# order_handler.post_one_doc({"teste": "teste"})

# pp.pprint(order_handler.get_one_doc({"teste": "teste"}))