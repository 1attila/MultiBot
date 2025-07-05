import discord
import File
from discord.ext import commands
from discord.ext import tasks
import asyncio
from AppIndex import Data, Update, Get
import AppIndex
import Embed
import RegisterUtil

IGN_INDEX = int(2)

class Applications(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Applications cog loaded")
        self.sheet = AppIndex.Sheet
        self.bot.loop.create_task(LoopThread(self.bot, self.sheet))
    
async def setup(bot):
    await bot.add_cog(Applications(bot))

async def LoopThread(bot, Sheet):

    while True:

        Index = Data()
        try:
            app = Get(Index + 1)
            name = app[File.NameIndex]
            await NewApp(bot, app)
            Update(Index + 1)
            print("New app")
        except:
            print("No apps")

        await asyncio.sleep(10)

async def NewApp(bot, app):
    
    embed = Embed.app_embed(app)
    channel = bot.get_channel(File.TicketVoting)
    await channel.send(embed=embed)
    
    message = channel.last_message
    await message.add_reaction("👍")
    await message.add_reaction("👎")
    
    guild = bot.get_guild(File.Guild)
    overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    guild.get_role(File.AppRole): discord.PermissionOverwrite(read_messages=True),
    guild.get_member_named(app[File.NameIndex]): discord.PermissionOverwrite(read_messages=True)
    }
    name = app[File.NameIndex]
    
    appChannel = await channel.category.create_text_channel(name=name[0:-5],
        overwrites=overwrites
    )
    
    await appChannel.send(embed=embed)
    appMessage = appChannel.last_message
    await appMessage.pin()

    await RegisterUtil.Register(Name=appChannel.name, Dc=str(name[0:-5]), Ign=str(app[2]), Id=str(Data()))
    Embed.log_embed("New applicant: " + name[0:-5])