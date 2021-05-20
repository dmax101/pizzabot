def log(message, location="main", type_of=None):
    pizza = "🍕"

    if location == "main":
        loc = location
    else:
        loc = location[0].__class__.__name__

    if type_of == None:
        print("{} [ {} ] {}".format(pizza, loc, message))
    elif type_of == "error":
        print("{} [ {} ] 💥 {}".format(pizza, loc, message))
    elif type_of == "warning":
        print("{} [ {} ] ⚠ {}".format(pizza, loc, message))
    elif type_of == "success":
        print("{} [ {} ] 🙌 {}".format(pizza, loc, message))