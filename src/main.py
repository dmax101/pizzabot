import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print("É hora da pizza!! {0.user}".format(client))
  await client.get_channel(838882914724872295).send("É hora da pizza!!")  


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if client.user.mentioned_in(message):
    if message.mention_everyone is False and message.mention_here in False:
      await message.channel.send("Olá, gostaria de uma pizza?") #responde mensagem

client.run(os.environ['TOKEN_PIZZA'])