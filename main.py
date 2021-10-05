import discord
import os

# Tricky env import for VSC
from dotenv import load_dotenv

# start discord client
client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} has logged into the matrix.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == "!hello":
        await message.channel.send('Hello {}!'.format(message.author.name))

load_dotenv('secrets.env')
token = os.getenv('TOKEN')
client.run(token)