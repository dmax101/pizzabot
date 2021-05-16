from .model.dbconnector import DbConnector
from .controller.dbcontroller import DbController
import os
import pprint as pp

cnn = DbConnector("pizzabot", os.environ["DB_PASSWORD"], "pizzabot")

order_db = cnn.connect().orders

order_handler = DbController([order_db])

order_handler.post_one_doc({"teste": "teste"})

pp.pprint(order_handler.get_one_doc({"teste": "teste"}))