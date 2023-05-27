import discord
from discord.ext import commands

class serverInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("serverinfo.py is ready")

    #command
    @commands.command()
    async def serverinfo(self, ctx):
        server_embed = discord.Embed(
            color=discord.Color.light_embed(),
            title=f"Information for {ctx.guild.name}",
            description="Specific information about current server"
        )
        server_embed.set_thumbnail(url=ctx.guild.icon)
        server_embed.add_field(name="Total members: ", value=ctx.guild.member_count, inline=False)
        #server_embed.add_field(name="Your permissions: ", value=ctx.guild.permissions, inline=False) - not working
        server_embed.add_field(name="Date joined: ", value=ctx.author.joined_at, inline=False)
        #server_embed.add_field(name="Server roles: ", value=ctx.guild.roles, inline=False)
        await ctx.send(embed=server_embed)

async def setup(client):
    await client.add_cog(serverInfo(client))

