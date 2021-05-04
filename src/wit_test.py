from model.wit_connector import Wit_Connector
from controller.analysis import Analysis

import pprint as pp

client = Wit_Connector()
resp = client.message(input("Faça seu pedido! \n"))

analysis = Analysis(resp)

pp.pprint(analysis.handle_message())