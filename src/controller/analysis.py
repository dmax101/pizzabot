import pprint as pp

def first_value(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]['value']
    if not val:
        return None
    return val

class Analysis:
    def __init__(self, response):
        self.response = response

    def handle_message(self):
        response = self.response

        traits = response['traits']
        get_pizza = first_value(traits, 'get_pizza')
        get_beverage = first_value(traits, 'get_beverage')

        if get_pizza and get_beverage:
            return "Pizza going well with a beverage!"

        if get_pizza:
            return "Pizza time!"
        
        if get_beverage:
            return "Let's drink!"
        else:
            return "Maybe next time!"