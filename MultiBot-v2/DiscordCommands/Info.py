import discord
from discord.ext import commands
import Embed
import File

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help cog loaded")

    @commands.hybrid_command()
    async def info(self, ctx):

        await ctx.message.delete()
        embed = Embed.embed(title="Infos", description="Bot of the " + File.Name + " server. Made by attila")
        embed = Embed.end(embed=embed)
        await ctx.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))