import discord
from discord.ext import commands
import File
import Embed
from HelpCommand import Poll, Bpoll
#PERMS -> Member
class PollCategory(commands.Cog):

    def __init__(self, bot):
        self.bot =  bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Poll cog loaded")

    @commands.command(help=Poll)
    @commands.has_role(File.CommandRole)
    async def poll(self, ctx, argument, *options):

        await ctx.message.delete()
        if argument == '':
            await ctx.channel.send(embed=Embed.err_embed(err="There is no argument"))

        if len(options) == 0:
            await ctx.channel.send(embed=Embed.err_embed(err="There are no options"))

        opa = []
        top = str("")

        embed = Embed.embed(title="POLL", description="Argument: " + str(argument))
        embed = Embed.end(embed)

        for option in range(len(options)):
            opt = str(options[option])
            f = len(opt) - 1
            opa.append(opt[0:-f])
            top += opt + "\n"
            
        embed = Embed.add_field(embed=embed, name="Options: ", value=top)
        await ctx.channel.send(embed=embed)
        message = ctx.channel.last_message

        for t in range(len(options)):
            await message.add_reaction(str(opa[t]))

    @commands.hybrid_command(help=Bpoll)
    @commands.has_role(File.CommandRole)
    async def bpoll(self, ctx, arg:str):
        
        await ctx.message.delete()
        embed = Embed.embed(title="POLL", description=arg)
        embed = Embed.end(embed)
        embed = Embed.add_field(embed=embed, name="Options: ", value="👍: yes,\n \n 👎: no.")
        await ctx.send(embed=embed)

        message = ctx.channel.last_message
        await message.add_reaction("👍")
        await message.add_reaction("👎")

async def setup(bot):
    await bot.add_cog(PollCategory(bot))