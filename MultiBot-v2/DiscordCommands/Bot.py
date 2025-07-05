import discord
from discord.ext import commands
import File
import Embed
#PERMS -> Members / Trials Cat ->Members
class Bot(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot cog loaded")

    @commands.hybrid_group(fallback="", help="Extra utilities")
    @commands.has_role(File.CommandRole)
    async def bot(self, ctx):
        await ctx.message.delete()
        
    @bot.command()
    @commands.has_role(File.CommandRole)
    async def send(self, ctx, text):

        await ctx.message.delete()
        await ctx.send(str(text))

    @bot.command()
    @commands.has_role(File.CommandRole)
    async def stex(self, ctx, text):
        await ctx.message.delete()
        await ctx.send("`" + str(text) + "`")

    @bot.command()
    @commands.has_role(File.CommandRole)
    async def cchannel(self, ctx, name):
        await ctx.message.delete()
        await ctx.guild.create_text_channel(name=str(name))

async def setup(bot):
    await bot.add_cog(Bot(bot))