from model.dbconnector import DbConnector
import os
import pprint as pp

class DbController:
    def __init__(self, collection):
        self.collection = collection[0]

    #novo pedido
    def post_one_doc(self, document):
        self.collection.insert_one(document)
    
    #revisao pedido
    def get_one_doc(self, document):
        res = self.collection.find_one(document)
        return res

    #cardapio
    def find_all(self):
      res = self.collection.find({})
      return res

cnn = DbConnector("pizzabot", "jWIoo3QuWhP70RZD", "pizzabot")

def get_cardapio(self):
      cnn = DbConnector("pizzabot", "jWIoo3QuWhP70RZD", "pizzabot")
      pizzas_db = cnn.connect().pizzas
      pizzas_handler = DbController([pizzas_db])
      pizzas = pizzas_handler.find_all()
      for pizza in pizzas:
          print(pizza)


##### PEDIDO #####

# order_db = cnn.connect().orders

# order_handler = DbController([order_db])

# novo

# order_handler.post_one_doc({"teste": "teste"})

# revisao

# pp.pprint(order_handler.get_one_doc({"teste": "teste"}))


##### CARDAPIO #####

#pizzas_db = cnn.connect().pizzas

#pizzas_handler = DbController([pizzas_db])

#pizzas = pizzas_handler.find_all()

#for pizza in pizzas:
# print(pizza)