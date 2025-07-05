import discord
from discord.ext import commands
import File
import Embed
#PERMS -> Members / Admins + CAT -> Meetings
class Meetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Meeting cog loaded")

    @commands.hybrid_group()
    @commands.has_role(File.CommandRole)
    async def meeting(self, ctx):
        await ctx.message.delete()

    @meeting.command()
    @commands.has_role(File.CommandRole)
    async def propose(self, ctx, argName:str, arg:str):
        
        h = ctx.channel.history(limit=2)

        emb = discord.Embed
        msg = discord.Message
        mlist = [message async for message in h]
        
        for m in range(len(mlist)):
            
            mes = mlist[m]
            if len(mes.embeds) > 0:
                embeds = mes.embeds
                emb = embeds[0]
                msg = mes

        await ctx.message.delete()
        emb.add_field(name=argName, value=arg, inline=False)
        await ctx.send(embed=emb)
        await msg.delete()

    @meeting.command()
    @commands.has_role(File.CommandRole)
    async def answer(self, ctx, argName:str, answ:str):
        
        h = ctx.channel.history(limit=2)

        emb = discord.Embed
        msg = discord.Message
        mlist = [message async for message in h]
        
        for m in range(len(mlist)):
            
            mes = mlist[m]
            if len(mes.embeds) > 0:
                embeds = mes.embeds
                emb = embeds[0]
                msg = mes

        await ctx.message.delete()
        emb.add_field(name=argName, value=answ, inline=False)
        await ctx.send(embed=emb)
        await msg.delete()


    @meeting.command()
    @commands.has_role(File.CommandRole)
    async def start(self, ctx, mDate:str, nDate:str):
        await ctx.message.delete()

        embed = Embed.embed(title="Meeting " + mDate, description="Next meeting will be `" + nDate + "`")
        embed = Embed.end(embed=embed)
        await ctx.send(embed=embed)
        Embed.log_embed("Meeting started!")

    @meeting.command()
    @commands.has_role(File.CommandRole)
    async def end(self, ctx, mDate:str):
        await ctx.message.delete()

        embed = Embed.embed(title="Meeting " + mDate + " arguments", description="Add an argument typing: `.meeting propose <name of the arg> <desc of the arg>`")
        embed = Embed.end(embed=embed)
        await ctx.send(embed=embed)
        Embed.log_embed("Meeting finished!")

async def setup(bot):
    await bot.add_cog(Meetings(bot))