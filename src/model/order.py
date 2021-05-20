import uuid

class Order:
    def __init__(self, client, shopping_cart=[]):
        self.id = uuid.uuid1()
        self.client = client
        self.shopping_cart = shopping_cart
        self.total = 0

    def __del__(self):
        self.client = None
        self.shopping_cart = None
        self.total = None

    def add_item_sc(self, item):
        self.shopping_cart.append(item)

    def remove_item_sc(self, item):
        for item_sc in self.shopping_cart:
            if item in item_sc["name"]:
                self.shopping_cart.remove(item_sc)

    def calculate_total(self) -> float:
        total = 0
        for item_sc in self.shopping_cart:
            total += item_sc["value"]
    
        return total