import discord
from discord.ext import commands
import youtube_dl
from youtube_search import YoutubeSearch


paused = False
queues = {}
def check_queue(ctx, id):
    if queues[id] != []:
        #gets voice channel
        voice_chat = ctx.guild.voice_client
        #looks for server id and finds first entry which contains ffmpeg audio and removes from dictionary
        source = queues[id].pop(0)
        voice_chat.play(source)

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("music.py is ready")

    #command
    #@commands.command()
    #async def join(self, ctx):
        #if user running this command is in voice channel
        #if (ctx.author.voice):
            #gets channel name and joins
            #channel = ctx.message.author.voice.channel
            #await channel.connect()


        #else:
            #await ctx.send("Fool!")

    @commands.command()
    async def leave(self, ctx):
        #if bot is in the channel
        if (ctx.voice_client):
            #leaves the channel
            #guild is the server, so preceding line means go to server, go to the voice chat that the bot is in, and disconnect
            await ctx.guild.voice_client.disconnect()
            #await ctx.guild.voice_client.cleanup()  -< not sure if this is necessary
            await ctx.send("またね")
        else:
            await ctx.send("Idiot!")

    @commands.command()
    async def play(self, ctx, url):
        if (ctx.author.voice):
            if not (ctx.voice_client):
                channel = ctx.message.author.voice.channel
                await channel.connect()
        else:
            await ctx.send("Fool!")
        ctx.voice_client.stop()
        
        #settings for ytdl
        YTDL_OPTIONS = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'mp3',
                'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                'restrictfilenames': True,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'ytsearch',
                'source_address': '0.0.0.0',
            }

        #settings for ffmpeg
        FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'
            }
        

        voice_chat = ctx.voice_client
        
        #gets youtube url info and converts it so that its playable on discord
        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice_chat = ctx.voice_client
            source = discord.FFmpegOpusAudio(URL, options = FFMPEG_OPTIONS)
            #after first song is done playing, lambda allows for the check_queue function to run, which plays the next song if there is any
            voice_chat.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))



    @commands.command()
    async def pause(self, ctx):
        global paused
        if not paused:
            #potentially use await so that I can remove the global paused and instead create a relationship between the two async functions
            paused = True
            await ctx.send("Paused! ( • )( • ) ԅ(‾⌣‾ԅ)")
            await ctx.voice_client.pause()
        else:
            await ctx.send("Already paused!")


    @commands.command()
    async def resume(self, ctx):
        global paused
        if paused:
            paused = False
            await ctx.send("Resumed! ( • )( • ) ԅ(‾⌣‾ԅ)")
            await ctx.voice_client.resume()

        else:
            await ctx.send("Already playing!")


    @commands.command()
    async def queue(self, ctx, url):
        global queues

        #settings for ytdl
        YTDL_OPTIONS = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'mp3',
                'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                'restrictfilenames': True,
                'noplaylist': True,
                'nocheckcertificate': True,
                'ignoreerrors': False,
                'logtostderr': False,
                'quiet': True,
                'no_warnings': True,
                'default_search': 'ytsearch',
                'source_address': '0.0.0.0',
            }

        #settings for ffmpeg 
        FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'
            }
        
            
        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['url']
            source = discord.FFmpegOpusAudio(URL, options = FFMPEG_OPTIONS)

        voice_chat = ctx.guild.voice_client
        guild_id = ctx.message.guild.id
        #guild id is an integer that defines the server, basically has server data.
        #checks if theres a song currently in queue. if so, append additional songs.
        if guild_id in queues:
            #adds ffmpeg version of the audio, adds to queues dictionary
            queues[guild_id].append(source)
        #adds first song
        else:
            #if theres no guild id in dictionary, set it equal to ffmpeg audio
            queues[guild_id] = [source]
        
        await ctx.send("Queued")
    


async def setup(client):
    await client.add_cog(Join(client))

