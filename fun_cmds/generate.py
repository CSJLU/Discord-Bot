import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import glob
import discord
from discord.ext import commands
import asyncio
import shutil



path = "C:/Stable Diffusion/stable-diffusion-webui/outputs/txt2img-images"
destination = "C:/Stable Diffusion/stable-diffusion-webui/outputs/txt2img-images/PushToDiscord"


class Generate(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("generate.py is ready")


    #command
    @commands.command()
    async def generate(self, ctx):
        def on_created(event):
            for file in os.listdir(path):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    #moves all files into the PushToDiscord folder
                    shutil.move(os.path.join(path, file), destination)

        #plan for tomorrow. on_created() will move the image into a folder called "PushToDiscord"
        #add another async def command that will take that image and send it to discord via bot. Then itll move the image to a folder called "Done"
        #so that the same image wont be sent again. 
    
        #once there is a creation event inside directory, on_created will be called
        event_handler = FileSystemEventHandler()
        event_handler.on_created = on_created


        observer = Observer()

        #only monitors specific path, nothing else
        observer.schedule(event_handler, path, recursive=False)
        observer.start()

        try:
            print("Monitoring")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Done")
        observer.join()
                    
    @commands.command()
    async def send(self, ctx):
        #all files within the directory
        for file in os.listdir(destination):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                #opens the images file so it can be modified, opened in binary mode for reading
                with open(os.path.join(destination, file), 'rb') as f:
                    image = discord.File(f)
                    #converts to file object that is uploadable to discord
                    await ctx.channel.send(file=image)
                done_directory = "C:/Stable Diffusion/stable-diffusion-webui/outputs/txt2img-images/Done"
                #moves all the files into the Done folder
                shutil.move(os.path.join(destination, file), done_directory)

    @commands.command()
    async def sendrandom(self, ctx):
        for file in os.listdir(destination):
            if file.lower().endswith(('.png', '.jpg', 'jpeg', '.gif')):
                with open(os.path.join(destination, file), 'rb') as f:
                    image = discord.File(f)
                    await ctx.channel.send(file=image)
                random_directory = "C:/Users/lucou/OneDrive/Desktop/Pics/random"
                shutil.move(os.path.join(destination, file), random_directory)

async def setup(client):
    await client.add_cog(Generate(client))



