import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py is ready")

    #command
    @commands.command()
    async def ping(self, ctx, query):
        embed = discord.Embed(
            color=discord.Color.light_embed(),
            title=f"English song lyrics for {query}"
        )

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Ping(client))


