from utils.log import log
from controller.dbcontroller import DbController
from model.dbconnector import DbConnector
import os

def post_order(pedido):
  cnn = DbConnector("pizzabot", "jWIoo3QuWhP70RZD", "pizzabot")
  order_db = cnn.connect().orders
  order_handler = DbController([order_db])
  order_handler.post_one_doc(pedido)

def get_cardapio():
  cnn = DbConnector("pizzabot", "jWIoo3QuWhP70RZD", "pizzabot")
  pizzas_db = cnn.connect().pizzas
  pizzas_handler = DbController([pizzas_db])
  pizzas = pizzas_handler.find_all()
  return pizzas

def processar_mensagem_sem_wit(mensagem):
  pedido = {}
  pizzas = get_cardapio()
  for pizza in pizzas:
    if str(mensagem).upper() == str(pizza["sabor"]).upper():
        pedido["sabor"] = pizza["sabor"]
        pedido["preço"] = pizza["preço"]
  return pedido

def print_cardapio():
  cardapio = "CARDAPIO:\n"
  pizzas = get_cardapio()
  for pizza in pizzas:
    sabor = str(pizza["sabor"]).upper() + "   "
    sabor = sabor.ljust(30, "-")
    preco = "RS " + str(pizza["preço"])
    cardapio += sabor + "-----   " + preco + "\n"
  return cardapio

class Pipeline:
    def __init__(self):
        self.on_start = True
        self.on_greeting = True
        self.on_choosing_products = True
        self.on_transation_db = True
        self.on_canceling_operation = True
        self.on_end_operation = True
        self.pedidos = []

    def response(self, message, waiting_response, code=0) -> dict:
        log("\n\tSending Message: {}\n\tWaiting response: {}".format(message, waiting_response), location=[self])
        return {
            "message": message,
            "waiting_response": waiting_response,
            "code": code
        }
    
    def canceling_operation(self, user_message) -> dict:
        if self.on_canceling_operation:
            message = "Operação cancelada pelo usuário!"
            waiting_response = False

            self.on_canceling_operation = False
            return self.response(message, waiting_response, -1)

    def end_operation(self, user_message) -> dict:
        if self.on_end_operation:
            message = "Finalizando sessão! Obrigado pela preferência!"
            waiting_response = False

            self.on_start = False
            self.on_greeting = False
            self.on_choosing_products = False
            self.on_transation_db = False
            self.on_canceling_operation = False
            self.on_end_operation = False
            return self.response(message, waiting_response, -1)
    
    def transation_db(self, user_message) -> dict:
        if self.on_transation_db:
            message = "Inserindo pedido no Banco de Dados"

            valor_total = 0
            order = {"products": {}}
            for i in range(len(self.pedidos)):
                if "sabor" in self.pedidos[i]:
                    order["products"]["product"+str(i)] = self.pedidos[i]["sabor"]
                    valor_total = valor_total + float(self.pedidos[i]["preço"])
            order["total"] = valor_total

            post_order(order)

            message += "\n\nÚltimo pedido inserido: \n" + str(order)

            waiting_response = False
            self.on_transation_db = False
            return self.response(message, waiting_response)
        else:
            return self.end_operation(user_message)

    def choosing_products(self, user_message) -> dict:
        if self.on_choosing_products:
          if user_message.upper() == "CANCELAR":
              self.on_start = False
              self.on_greeting = False
              self.on_choosing_products = False
              self.on_transation_db = False
              self.on_canceling_operation = True
              self.on_end_operation = False
              return self.canceling_operation(user_message)

          elif user_message.upper() == "CARDAPIO":
              message = ""
              message += print_cardapio()
              message += "\n Para cancelar essa sessão, digite 'CANCELAR'"
              message += "\n Para mostrar o cardapio novamente, digite 'CARDAPIO'"
              message += "\n"
              message += "Qual sabor deseja pedir?"
              waiting_response = True
              return self.response(message, waiting_response)
              
          elif user_message.upper() == "FINALIZAR":
              valor_total = 0
              message = "Seu pedido final foi:"
              for pedido in self.pedidos:
                  if "sabor" in pedido:
                      message += "\n" + str(pedido["sabor"]).upper() + ": R$" + str(pedido["preço"])
                      valor_total = valor_total + float(pedido["preço"])
              valor_total = round(valor_total, 2)
              message += "\n\nValor final: R$" + str(valor_total) + "\n "

              self.on_choosing_products = False
              waiting_response = False
              return self.response(message, waiting_response)
          else:
              pedido = processar_mensagem_sem_wit(user_message)
              if pedido:
                  self.pedidos.append(pedido)
                  message = "Você pediu:"
                  for pedido in self.pedidos:
                      if "sabor" in pedido:
                          message += "\n" + str(pedido["sabor"]).upper() + ": R$" + str(pedido["preço"])
                  message += "\n\n Para cancelar essa sessão, digite 'CANCELAR'"
                  message += "\n Para mostrar o cardapio novamente, digite 'CARDAPIO'"
                  message += "\n\nQue outro sabor deseja adicionar? Digite 'FINALIZAR' para finalizar pedido ou entre com novo sabor"
              waiting_response = True
              return self.response(message, waiting_response)
        else:
            return self.transation_db(user_message)

    def greeting(self, user_message) -> dict:
        if self.on_greeting:
            message = ""
            message += print_cardapio()
            message += "\n Para cancelar essa sessão, digite 'CANCELAR'"
            message += "\n Para mostrar o cardapio novamente, digite 'CARDAPIO'"
            message += "\n"
            message += "Qual sabor deseja pedir?"
            
            waiting_response = False
            self.on_greeting = False
            return self.response(message, waiting_response)

        else:
            return self.choosing_products(user_message)

    def start(self, user_message) -> dict:
        if self.on_start:
            message = "Acionando minha rede positrônica! E iniciando novo pedido!"
            waiting_response = False

            self.on_start = False
            return self.response(message, waiting_response)
        else:
            return self.greeting(user_message)
