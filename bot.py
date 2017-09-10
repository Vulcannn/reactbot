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
    

    
    
    
    
client.start(token)
