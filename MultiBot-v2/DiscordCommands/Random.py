import discord
from discord.ext import commands
import File
#DESU + VITAMIN C
class Random(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Random cog loaded")

    @commands.hybrid_command()
    async def ip(self, ctx):

        await ctx.message.delete()
        ip = "`smp." + File.Name.lower() + ".mc`"
        await ctx.send(File.Name + " ip is: " + ip)

    @commands.command
    async def Vitamin(self, ctx):
        pass #i need a bit of time for dis

    @commands.command
    async def Desu(self, ctx):
        pass #i need a bit of time for dis

async def setup(bot):
    await bot.add_cog(Random(bot))