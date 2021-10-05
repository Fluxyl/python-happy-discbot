import discord
import os
import requests
import json

# Tricky env import for VSC
from dotenv import load_dotenv

def get_quote():
    response = requests.get('https://zenquotes.io/api/quotes/')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

# start discord client
client = discord.Client()

# Sad Words List
sadWords = ['sad', 'depressed', 'depressing', 'unhappy', 'lonely', 'miserable']

# Encouraging messages list
encourageList = [
    "I love you!",
    "Don't be sad. Be glad.",
    "I know you feel bummed, but this discord bot loves you.",
    "Stay positive. :)"
]
@client.event
async def on_ready():
    print('{0.user} has logged into the matrix.'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == "!hello":
        await message.channel.send('Hello {}!'.format(message.author.name))

    if message.content.lower() == "!encourage":
        quote = get_quote()
        await message.channel.send(quote)

load_dotenv('secrets.env')
token = os.getenv('TOKEN')
client.run(token)