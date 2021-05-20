import os
from utils.log import log
from controller.discordcontroller import DiscordController

def setup():
    log("🤖 Setting up!")

def main():
    log("Starting 🍕 PizzaBot!!!")
    log("Connecting to 🌎 Discord!")
    discord = DiscordController(os.environ["TOKEN_PIZZA"])
    discord.run()

def finish():
    log("🤖 Bye!")
    
if __name__ == "__main__":
    setup()
    main()
    finish()