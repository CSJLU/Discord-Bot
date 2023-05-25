import discord
from discord.ext import commands
from discord import app_commands

class Emotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("emote.py is ready")

    @app_commands.command(
        name = "sadge",
        description = "Send a sadge emote"
    )
    
    async def sadge(self, interaction: discord.Interaction):
        sadge_path = "C:/Users/lucou/OneDrive/Pictures/DiscordImage/sadge.png"
        with open(sadge_path, 'rb') as f:
            sadge_image = discord.File(f)
        await interaction.response.send_message(file=sadge_image)
    
    @app_commands.command(
        name = "copium",
        description = "Send a copium emote"
    )

    async def copium(self, interaction: discord.Interaction):
        copium_path = "C:/Users/lucou/OneDrive/Pictures/DiscordImage/copium.png"
        with open(copium_path, 'rb') as f:
            copium_image = discord.File(f)
        await interaction.response.send_message(file=copium_image)
        

async def setup(client):
    await client.add_cog(Emotes(client))

