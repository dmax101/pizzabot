import os
import discord
from discord import message

BOT_DESC = "PizzaBot é um serviço que permite conectar gamers famintos a pizzarias locais através do Discord."

client = discord.Client()


def get_text_channels():
    text_channel_list = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)
    return text_channel_list


def compose_message(message):
    message = "🍕 " + message
    return message


@client.event
async def on_ready():
    print("É hora da pizza!! {0.user}".format(client))

    text_channels = get_text_channels()
    await client.get_channel(text_channels[0].id).send(compose_message("É hora da pizza!!"))
    await client.get_channel(text_channels[0].id).send(compose_message(BOT_DESC))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message) and message.mention_everyone is False:
        if "desconectar" in message.content:
            print("É hora de dar tchau!! {0.user}".format(client))
            await message.channel.send(compose_message("É hora de dar tchau!!"))
            await client.logout()

        await message.channel.send(compose_message("Olá, gostaria de uma pizza?")) # responde mensagem

client.run(os.environ["TOKEN_PIZZA"])
