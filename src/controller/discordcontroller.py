import os
import discord
from discord import message
from random import randrange

class DiscordController:
    def __init__(self):
        bot_names = ["Sonny","David","Bumblebee","Ultron","Andrew","Gort","Ash","T-800","T-1000","Pris","Eva","Wall-E","Robby","Marvin","C3PO","R2D2","Rosie","HAL 9000","Gigolo Joe","Skynet","Johnny 5","Data","ED209","False Maria"]
        self.bot_name = bot_names[randrange(len(bot_names))]

        self.client = discord.Client()

        self.BOT_DESC = "PizzaBot é um serviço que permite conectar gamers famintos a pizzarias locais através do Discord."

    def run(self):
        self.on_ready()
        self.on_message()
        self.client.run(os.environ["TOKEN_PIZZA"])

    def get_text_channels(self):
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        return text_channel_list

    def compose_message(self, message):
        message = "🍕 " + message
        return message

    def on_ready(self):
        @self.client.event
        async def on_ready():
            print("É hora da pizza!! {0.user}".format(self.client))

            text_channels = self.get_text_channels()
            await self.client.get_channel(text_channels[0].id).send(self.compose_message("{}: É hora da pizza!!".format(self.bot_name)))
            await self.client.get_channel(text_channels[0].id).send(self.compose_message(self.BOT_DESC))

        return on_ready

    def on_message(self):
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if self.client.user.mentioned_in(message) and message.mention_everyone is False:
                if "desconectar" in message.content:
                    print("É hora de dar tchau!! {0.user}".format(self.client))
                    await message.channel.send(self.compose_message("É hora de dar tchau!!"))
                    await self.client.logout()

                await message.channel.send(self.compose_message("Olá, gostaria de uma pizza?")) # responde mensagem
        
        return on_message