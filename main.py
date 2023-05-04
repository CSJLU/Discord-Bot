import discord
from discord.ext import commands, tasks
import os
import asyncio

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

#sets bot activity, can change the "Game" part as well
bot_status = discord.Game(name="with you! :)")

#other statuses: DND, idle
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), activity=bot_status, status=discord.Status.online)

#checks if working
@bot.event
async def on_ready():
    print("Success: Bot connected")

@bot.event
async def on_member_join(member, client):
    system_channel = member.guild.system_channel
    welcome_message = f"Welcome {member}"
    if system_channel:
        try:
            await system_channel.send(welcome_message[:-5])
            with open('miku_welcome.gif', 'rb') as f:
                welcome_image = discord.File(f)
                await system_channel.send(file=welcome_image)
        except Exception as error:
            print(error)



#cogs are added
async def load():
    for filename in os.listdir("./fun_cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"fun_cmds.{filename[:-3]}")
            #print(f"{filename[:-3]} is loaded")



async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())



'''
import os
import discord

# Create a Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

# Watch the directory for new files
directory = 'path/to/directory'
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        filepath = os.path.join(directory, filename)
        # Send the file to the chat
        with open(filepath, 'rb') as fp:
            await client.get_channel(channel_id).send(file=discord.File(fp, 'file.png'))

# Start the Discord bot
client.run('your_discord_bot_token')
'''