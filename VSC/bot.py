import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

def readValue():
    try:
        with open('main/value.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def readFlag():
    try:
        with open('main/flag.txt', 'r') as flag:
            flag_content = flag.read().strip().lower()
            return flag_content == 'true'
    except FileNotFoundError:
        return False 

def setFlag():
    with open('main/flag.txt', 'w') as edit:
        edit.write('False')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    print('--------------')

    web.start()

CHANNEL_ID = 'Channel ID'

@tasks.loop(seconds=3)
async def web():
    flag = readFlag()
    if flag:
        channel = bot.get_channel(CHANNEL_ID)
        value = readValue()
        print(f"Value: {value}")
        if not value: 
            print("Value is empty")
        else:
            await channel.send(f'**Sent from WEB**: {value}')
        setFlag() 


bot.run('Bot Token')

