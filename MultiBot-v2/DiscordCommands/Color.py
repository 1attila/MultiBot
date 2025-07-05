import discord
from discord.ext import commands
import File
import ColorUtil
#Perms -> Members, Cat -> #member
class Color(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready():
        print("Color cog loaded")

    @commands.hybrid_command()
    @commands.has_role(File.CommandRole)
    async def color(self, ctx, color:str):

        await ctx.message.delete()
        
        if color == "list":
            for Color in ColorUtil.Colors:

                embed = discord.Embed(title= "COLORS", description=Color, color=ColorUtil.Get(Color))
                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="COLORS", description=color, color=ColorUtil.Get(color))
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Color(bot))