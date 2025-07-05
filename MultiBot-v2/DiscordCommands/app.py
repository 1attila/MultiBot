import discord
from discord.ext import commands
import File
import Embed
import AppIndex
from discord.utils import get
import RegisterUtil
import HelpCommand as h
import Mcommands

#CAT -> applications/archived_applications + PERMS -> Members/Admins
class App(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sheet = AppIndex.Sheet
        self.status = "closed"
        self.OpenEmbed = discord.Embed
        self.CloseEmbed = discord.Embed

    @commands.Cog.listener()
    async def on_ready(self):
        print("App cog loaded")
    
    @commands.hybrid_group(fallback="", aliases=["a"], help="Forms, tickets and voting management")
    @commands.has_role(File.CommandRole)
    async def app(self, ctx):
        await ctx.message.delete()

    @app.command(help=h.A_List)
    @commands.has_role(File.CommandRole)
    async def list(self, ctx):

        await ctx.message.delete()
        await ctx.channel.send(embed=Embed.app_list(self.sheet))

    @app.command(help=h.A_Count)
    @commands.has_role(File.CommandRole)
    async def count(self, ctx):
        
        await ctx.message.delete()

        embed = Embed.embed("App count", str(AppIndex.Data() - 2))
        embed = Embed.end(embed)
        await ctx.channel.send(embed=embed)

    @app.command(help=h.A_Show)
    @commands.has_role(File.CommandRole)
    async def show(self, ctx, id):
        
        await ctx.message.delete()

        if str(id) == 'last':
            await ctx.channel.send(embed=Embed.app_embed(AppIndex.Get(AppIndex.Data())))
            
        if str(id) != 'last':

            if int(id) > 0:
                await ctx.channel.send(embed=Embed.app_embed(AppIndex.Get(int(id))))

            else:
                id = await RegisterUtil.Query(Player=id, attribute="id")
                if id != "/":
                    await ctx.channel.send(embed=Embed.app_embed(AppIndex.Get(int(id))))

    @app.command()
    @commands.has_role(File.CommandRole)
    async def process(self, ctx, id:int, name:str):
        await ctx.message.delete()

        bot = self.bot
        app = AppIndex.Get(id)
        app[File.NameIndex] = name

        guild = bot.get_guild(File.Guild)
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.get_role(File.AppRole): discord.PermissionOverwrite(read_messages=True),
        guild.get_member_named(app[File.NameIndex]): discord.PermissionOverwrite(read_messages=True)
        }
        name = app[File.NameIndex]
        
        appChannel = await ctx.channel.category.create_text_channel(name=name[0:-5],
            overwrites=overwrites
        )

        embed = Embed.app_embed(app) 

        await appChannel.send(embed=embed)
        appMessage = appChannel.last_message
        await appMessage.pin()

        Embed.log_embed("New applicant: " + name[0:-5])

    @app.command(help=h.A_Deny)
    @commands.has_role(File.CommandRole)
    async def deny(self, ctx, id=None):

        await ctx.message.delete()
        
        category = discord.CategoryChannel

        for c in ctx.guild.categories:
            if c.id == File.ArchiviedAppCategory:
                category = c

        channel = discord.TextChannel

        if id == None:
            channel = ctx.channel

        if id != None:
            name = await RegisterUtil.Query(Player=str(id), attribute="dc")
            n = await RegisterUtil.Query(Player=str(id), attribute="name")

            for chan in ctx.guild.channels:
                if chan.name == n:
                    channel = chan

        await channel.edit(category=category)
        Embed.log_embed("Denied " + name + "'s application")

    @app.command(help=h.A_Accept)
    @commands.has_role(File.CommandRole)
    async def accept(self, ctx, id=None):
        
        await ctx.message.delete()

        name = ""
        channel = discord.TextChannel

        category = discord.CategoryChannel

        for c in ctx.guild.categories:
            if c.id == File.ArchiviedAppCategory:
                category = c

        if id == None:
            name = await RegisterUtil.Query(Player=ctx.channel.name, attribute="dc")
            channel = ctx.channel

        if id != None:
            name = await RegisterUtil.Query(Player=str(id), attribute="dc")
            n = await RegisterUtil.Query(Player=str(id), attribute="name")

            for chan in ctx.guild.channels:
                if chan.name == n:
                    channel = chan
        
        user = ctx.guild.get_member_named(name)
        
        role = get(ctx.guild.roles, id=File.TrialRole)
        await user.add_roles(role)
        
        await channel.edit(category=category)

        await Whitelist(User = await RegisterUtil.Query(Player=str(id), Attribute="ign"))

        Embed.log_embed("Accepted " + name + "'s application")

    @app.command(help=h.A_Vote)
    @commands.has_role(File.CommandRole)
    async def vote(self, ctx, id=None):

        await ctx.message.delete()

        name = ""

        c = self.bot.get_channel(File.MemberVoting)

        if id == None :
            name = await RegisterUtil.Query(Player=ctx.channel.name, attribute="dc")

        if id != None:
            name = await RegisterUtil.Query(Player=str(id), attribute="dc")
        trial = ctx.guild.get_member_named(name)

        link = ""
        async for m in c.history(limit=100):
            em = m.embeds
            if len(em) > 0:
                e = em[0]
                tit = e.title
                if tit.__contains__(name):
                    link = m.jump_url
        
        clink = ""
        for channel in ctx.guild.text_channels:
            if channel.name == await RegisterUtil.Query(Player=name, attribute="name"):
                clink = channel.jump_url
        
        embed = discord.Embed(title = name + "'s trial", 
            description="\n [App](" + link + ") \n [Channel](" + clink + ")", 
            color=discord.Color.blue()
        )
        avatar = trial.avatar
        embed.set_thumbnail(url=avatar.url)
        embed.set_footer(text=File.Name)
        embed.add_field(name="👍", value="promote", inline=True)
        embed.add_field(name="🟨", value="keep trial", inline=True)
        embed.add_field(name="👎", value="kick", inline=True)

        await c.send(embed=embed)
        message = c.last_message
        await message.add_reaction("👍")
        await message.add_reaction("🟨")
        await message.add_reaction("👎")
        
    @app.command(help=h.A_Open)
    @commands.has_role(File.CommandRole)
    async def open(self, ctx):
        
        await ctx.message.delete()

        if self.OpenEmbed == None:
            await ctx.send(embed=Embed.err_embed("You must define an embed first!"))

        channel = self.bot.get_channel(File.AppChannel)
        try:
            await channel.purge(limit=1)
        except:
            pass
        await channel.send(embed=self.OpenEmbed)

        self.status = "open"
        Embed.log_embed("Apps are now open")

    @app.command(help=h.A_Close)
    @commands.has_role(File.CommandRole)
    async def close(self, ctx):
        
        await ctx.message.delete()

        if self.CloseEmbed == None:
            await ctx.send(embed=Embed.err_embed("You must define an embed first!"))

        channel = self.bot.get_channel(File.AppChannel)
        try:
            await channel.purge(limit=1)
        except:
            pass
        await channel.send(embed=self.CloseEmbed)
        
        self.status = "closed"
        Embed.log_embed("Apps are now closed")

    @app.command(help=h.A_Embed)
    @commands.has_role(File.CommandRole)
    async def embed(self, ctx, type:str, embed:discord.Message):
        
        await ctx.message.delete()
        
        if type == "open":

            if embed != None:
                self.CloseEmbed == embed
            else:
                ctx.send(embed=Embed.err_embed("There's no embed"))

        elif type == "close":

            if embed != None:
                self.CloseEmbed == embed
            else:
                ctx.send(embed=Embed.err_embed("There's no embed"))

        else:
            ctx.send(embed=Embed.err_embed("Incorrect type. Type could be: `open` or `closed`"))

    @app.command(help=h.A_Info)
    @commands.has_role(File.CommandRole)
    async def info(self, ctx):
        
        await ctx.message.delete()

        embed = Embed.embed("App info", "")
        embed = Embed.add_field(embed=embed, name="Total apps: ", value= AppIndex.Data() - 2)
        embed = Embed.add_field(embed=embed, name="Status: ", value=self.status)
        embed = Embed.end(embed)
        await ctx.channel.send(embed=embed)
    
async def Whitelist(User:str, Server=-1):
    
    for server in range(len(File.Servers)):
        if server != Server:
            await Mcommands.exe(server = Server, command="whitelist add" + User)

            s = File.Server[server]
            if s[2] == "true":
                await Mcommands.exe(server = Server, command="op " + User)

async def Unwhitelist(User:str, Server=-1):

    for server in range(len(File.Servers)):
        if server != Server:
            await Mcommands.exe(server = Server, command="whitelist remove " + User)

async def setup(bot):
    await bot.add_cog(App(bot))