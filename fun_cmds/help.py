import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is ready")

    @app_commands.command(
        name = "help",
        description = "Get a list of all available commands",
    )
    
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=discord.Color.light_embed(),
            title="List of Commands"
        )

        #file = discord.File("C:/Users/lucou/OneDrive/Pictures/DiscordImage/whiterain.jpg", filename="whiterain.jpg")
        #embed.set_image(url="attachment://whiterain.jpg")

        embed.add_field(name="play", value="Plays video with given Youtube link", inline=False)
        embed.add_field(name="queue", value="Adds youtube video to a queue", inline=False)
        embed.add_field(name="resume", value="Resumes the player", inline=False)
        embed.add_field(name="pause", value="Pauses the player", inline=False)
        embed.add_field(name="leave", value="Disconnects bot from voice channel", inline=False) 
        embed.add_field(name="random", value="Sends a random anime image to chat", inline=False)
        embed.add_field(name="quintuplet", value="Sends a random quintuplet image to the chat", inline=False)
        embed.add_field(name="generate", value="Generated image is moved to separate folder - **ONLY WORKS AFTER LOCAL AI IMAGE GENERATION**", inline=False)
        embed.add_field(name="send", value="Sends generated image to discord chat - **MUST FIRST USE GENERATE**", inline=False)

        await interaction.response.send_message(
            #file=file,
            embed=embed
        )

async def setup(client):
    await client.add_cog(Help(client))

