import os
from utils.log import log
from controller.discordcontroller import DiscordController

def setup():
    pass

def main():
    log("Starting 🍕 PizzaBot!!!")
    log("Connecting to 🌎 Discord!")
    discord = DiscordController(os.environ["TOKEN_PIZZA"])
    discord.run()

    # log("Connecting to 🌎 database!")
    # db_handler = DbController([
    #     DbConnector(
    #         user="pizzabot",
    #         pw=os.environ["DB_PASSWORD"],
    #         database="pizzabot"
    #     ).connect()
    # ])

    # log("Creating order instance")

def finish():
    log("🤖 Bye!")
    
if __name__ == "__main__":
    setup()
    main()
    finish()