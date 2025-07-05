import discord
from discord.ext import commands
import Embed
import File
import Mcommands

class Execute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Execute cog loaded")

    @commands.hybrid_command()
    @commands.has_role(File.AdminRole)
    async def execute(self, ctx, command:str, server="0"):
        await ctx.message.delete()

        if File.Servers[Mcommands.get(Server=server)][2] == "true":

            r = await Mcommands.exe(server=server, command=command)

            embed = discord.Embed(
                title="Succesfully executed `" + command + "` on " + server,
                description=r,
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send(embed=Embed.err_embed("You can't execute commands on this server!"))

async def setup(bot):
    await bot.add_cog(Execute(bot))