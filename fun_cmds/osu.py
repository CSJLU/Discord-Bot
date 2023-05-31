import discord
from discord.ext import commands
import requests
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

with open("client_id.txt", "r", encoding="utf-8") as f:
    client_id = f.read()


with open("client_secret.txt", "r", encoding="utf-8") as f:
    client_secret = f.read()


api = Ossapi(client_id, client_secret)



class Osu(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("osu.py is ready")

    #command
    @commands.command()
    async def osuinfo(self, ctx, user):
        embed = discord.Embed(color=discord.Color.light_embed(), title=f"Information on {user}")

        get_user = api.user(user, key=UserLookupKey.USERNAME)
        embed.set_thumbnail(url=get_user.avatar_url)
        #embed.add_field(name="")

        file = discord.File("C:/Users/lucou/OneDrive/Pictures/DiscordImage/meow.gif", filename="image.gif")
        embed.set_image(url="attachment://image.gif")

        embed.add_field(name="Global rank", value=get_user.statistics.global_rank, inline=False)
        embed.add_field(name="Date joined", value=get_user.join_date, inline=False)
        embed.add_field(name="Last time online", value=get_user.last_visit, inline=False)
        embed.add_field(name="Accuracy", value=get_user.statistics.hit_accuracy, inline=False)
        embed.add_field(name="Amount of 300s", value=get_user.statistics.count_300, inline=False)
        embed.add_field(name="Amount of 100s", value=get_user.statistics.count_100, inline=False)
        embed.add_field(name="Amount of 50s", value=get_user.statistics.count_50, inline=False)
        embed.add_field(name="Amount of misses", value=get_user.statistics.count_miss, inline=False)
        embed.add_field(name="Interests", value=get_user.interests, inline=False)
        embed.add_field(name="User Occupation", value=get_user.occupation, inline=False)

        
        await ctx.send(embed=embed, file=file)


    # @commands.command()
    # async def mapinfo(self, ctx, beatmap_name):
    #     embed = discord.Embed(color=discord.Color.light_embed(), title=f"Information on {beatmap_name}")
    #     get_beatmap = api.beatmap(filename=beatmap_name)
    #     #embed.set_thumbail(get_beatmap.url)
    #     embed.add_field(name="test", value=get_beatmap.difficulty_rating)

    #@commands.command()
    #async def recent(self, ctx)
    #osu_scores
    






async def setup(client):
    await client.add_cog(Osu(client))


