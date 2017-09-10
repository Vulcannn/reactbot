#python3.5
import discord
from discord.ext import commands #run in cmd: pip install discord.py

token = 'botoken' #enter bot token in here
client = discord.Client()

@client.event
async def on_ready():
    print('---------------------------------------------')
    print('Bot has started!')
    print('Bot Logged in as:', client.user.name)
    print('Bot User ID:', client.user.id)
    print('---------------------------------------------')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-test'):
        msg = 'I am online and working, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    

    
    
    
    
client.start(token)
