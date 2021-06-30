from model.dbconnector import DbConnector
from controller.dbcontroller import DbController
import pprint as pp
import os

cnn = DbConnector("pizzabot", os.environ["DB_PASSWORD"], "pizzabot")

order_db = cnn.connect().orders

order_handler = DbController([order_db])

order_handler.post_one_doc({"teste": "teste"})

documentos = order_handler.find_all()

pp.pprint(order_handler.get_one_doc({"teste": "teste"}))

for documento in documentos:
    print(documento["teste"])
