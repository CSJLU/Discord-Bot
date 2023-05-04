import animec
import discord
from discord.ext import commands

class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("anime.py is ready")

    @commands.command()
    async def anime(self, ctx, query):

        animesong = animec.sagasu.Anilyrics(query)
        english_lyrics = animesong.english()

        
        #test = animesong.english()
        embed = discord.Embed(
            color=discord.Color.light_embed(),
            title=f"English song lyrics for {query}"
        )


        #print(english_lyrics)
        embed.add_field(name=f"{query}", value=english_lyrics)
        #await ctx.send(english_lyrics)
        await ctx.send(embed=embed)


        #await ctx.channel.send(test)
        #embed = discord.Embed()

    
async def setup(client):
    await client.add_cog(Anime(client))
