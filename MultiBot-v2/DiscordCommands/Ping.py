import discord
from discord.ext import commands
import File
from HelpCommand import Ping

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping cog loaded")

    @commands.hybrid_command(help=Ping)
    @commands.has_role(File.CommandRole)
    async def ping(self, ctx):

        await ctx.message.delete()
        embed = discord.Embed(title="Pong!", description= "Bot latency: " + str(round(self.bot.latency * 1000)) + " ms", color=discord.Color.blue())
        embed.set_footer(text=File.Name)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))