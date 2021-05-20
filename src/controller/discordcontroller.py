import os
import discord
from discord import message
from random import randrange
from utils.log import log
from controller.pipeline import Pipeline

class DiscordController:
    def __init__(self, token):
        bot_names = ["Sonny","David","Bumblebee","Ultron","Andrew","Gort","Ash","T-800","T-1000","Pris","EVA","Wall-E","Robby","Marvin","C3PO","R2D2","Rosie","HAL 9000","Gigolo Joe","Skynet","Johnny 5","Data","ED209","False Maria"]
        self.bot_name = bot_names[randrange(len(bot_names))]
        log("The bot 🤖 {} is the attendant.".format(self.bot_name), location=[self])
        self.BOT_DESC = "PizzaBot é um serviço que permite conectar gamers famintos a pizzarias locais através do Discord."

        self.client = discord.Client()
        self.token = token

        self.pipeline = Pipeline()

        self.user = {
            "name": "",
            "message": ""
        }

    def run(self):
        log("Starting Discord listener.", location=[self])
        self.on_ready()
        self.on_message()
        self.client.run(self.token)

    def get_text_channels(self):
        text_channel_list = []
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        return text_channel_list

    def compose_message(self, message) -> str:
        message = "🍕 " + message
        return message

    def on_ready(self):
        @self.client.event
        async def on_ready():
            message = "É hora da 🍕 pizza!! {0.user}".format(self.client)
            log(message, location=[self], type_of="success")

            text_channels = self.get_text_channels()
            channel = self.client.get_channel(text_channels[0].id)

            welcome_message = "Fala aí galera! Eu sou {}, e vou te atender hoje: É hora da pizza!!! Uhul! \n {}".format(
                self.bot_name,
                self.BOT_DESC
            )

            await channel.send(self.compose_message(welcome_message))

        return on_ready

    def on_message(self):
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return on_message

            if self.client.user.mentioned_in(message) and message.mention_everyone is False:
                if "desconectar" in message.content:
                    print("É hora de dar tchau!! {0.user}".format(self.client))
                    await message.channel.send(
                        self.compose_message(
                            "É hora de dar tchau!!"
                        )
                    )
                    await self.client.logout()
                else:
                    user_response = message.content.split()
                    user_response = message.content.replace(user_response[0] + " ", "")

                    iterations = 0
                    while True:
                        iterations += 1
                        log("Level {}".format(iterations), location=[self])

                        flow = self.pipeline.start(user_response)
                        await message.channel.send(
                            self.compose_message(
                                flow["message"]
                            )
                        )
                        if flow["waiting_response"]:
                            break
        
        return on_message