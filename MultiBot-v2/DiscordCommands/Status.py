import discord
from discord.ext import commands
import File
import Embed
from rcon import Client
import socket
import Mcommands

#CAT -> Members + PERMS -> Trias
class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Status cog loaded")

    @commands.hybrid_command()
    @commands.has_role(File.CommandRole)
    async def status(self, ctx, thing:str="servers"):

        await ctx.message.delete()

        answer = ""

        for structure in range(len(File.CheckBlockCoords)):
            struc = File.CheckBlockCoords[structure]
            if thing == struc[0]:

                for state in struc[4]:
                    
                    try:
                        with Client("127.0.0.1", Mcommands.get(struc[1]), passwd=File.RconPass, timeout=15) as client:
                            response = client.run("execute in minecraft:" + struc[2], + " if block " + struc[3] + " minecraft:" + state[0])

                            if response == "Test passed":
                                answer = state[1]

                    except socket.timeout:
                        asnwer = "Couldn't reach the server in time"

                embed = discord.Embed(title=thing, description="Status: " + answer, color=discord.Color.blue())
                embed.set_footer(text=File.Name)
                await ctx.send(embed=embed)

        for server in File.Servers:
            
            if Mcommands.get(thing) is not None:
                s = File.Servers[Mcommands.get(thing)]

                try:
                    with Client("127.0.0.1", s[1], passwd=File.RconPass, timeout=15) as client:
                        response = None
                        response = client.run("ping")

                        if response == "":
                            answer = "Offline"
                        else:
                            answer = "Online"
                except socket.timeout:
                    answer = "Couldn't reach the server in time"

                embed = discord.Embed(title=thing, description="Status: " + answer, color=discord.Color.blue())
                embed.set_footer(text=File.Name)
                await ctx.send(embed=embed)

        if thing == "servers":

            servers = ""
            answ = []

            for server in File.ServersName:
                servers += File.ServersName + " | "
                try:
                    with Client("127.0.0.1", "port", passwd=File.RconPass, timeout=15) as client:
                            response = None
                            response = client.run("ping")

                            if response == "":
                                answ [server] = "Offline"
                            else:
                                answ [server] = "Online"
                except socket.timeout:
                    answ [server] = "Couldn't reach the server in time"

            embed = discord.Embed(title="Servers status", description="Servers: " + servers, color=discord.Color.blue())
            for s in File.ServersName:
                embed.add_field(name=File.ServersName[s], value=answ[s], inline=False)
            embed.set_footer(text=File.Name)

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Status(bot))