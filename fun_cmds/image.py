from discord.ext import commands
import discord
import os
import random

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("image.py is ready")

    @commands.command()
    async def random(self, ctx):
        #directory of where the random images are stored
        path = "C:/Users/lucou/OneDrive/Desktop/Pics/random"
        images = os.listdir(path)
        #grabs one random image from within this directory
        selected_image = random.choice(images)
        #opens the image file so it can be modified, opened in binary mode for reading
        with open(os.path.join(path, selected_image), 'rb') as f:
            #converts to file object that is uploadable to discord
            final_image = discord.File(f)
            await ctx.channel.send(file=final_image) 
                    

    @commands.command()
    async def quintuplet(self, ctx):
        #same comments/functions as the random command
        path = "C:/Users/lucou/OneDrive/Desktop/Pics/quintuplets"
        images = os.listdir(path)
        selected_image = random.choice(images)
        with open(os.path.join(path, selected_image), 'rb') as f:
            final_image = discord.File(f)
            await ctx.channel.send(file=final_image) 
                    


async def setup(client):
    await client.add_cog(Image(client))