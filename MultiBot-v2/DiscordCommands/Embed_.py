import discord
from discord.ext import commands
import File
import Embed as emb
import ColorUtil

#PERMS -> Member
class Embed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.Embeds = []
        self.Users = []

    @commands.Cog.listener()
    async def on_ready(self):
        print("Embed cog loaded")
    
    @commands.command()
    @commands.has_role(File.CommandRole)
    async def qembed(self, ctx, *arg:str):

        await ctx.message.delete()

        tit = str(arg[0]) if arg[0] != "-" else "\u200b"
        desc = arg[1] if arg[1] != "-" else "\u200b"
        footer = str(arg[2]) if arg[2] != "-" else "\u200b"
        color = ColorUtil.Get(arg[3]) if arg[3] != '-' else discord.Color.Blue()

        if footer == "default":
            footer = File.Name

        embed = discord.Embed(title=tit, description=desc, color=color)
        l = (len(arg) - 4) / 3
        a = 4
        b = 5
        c = 6
        
        for i in range(int(l)):
            
            embed.add_field(name=str(arg[a]), value=str(arg[b]), inline=arg[c])
            a+=3
            b+=3
            c+=3
        
        embed.set_footer(text=footer)
        await ctx.channel.send(embed=embed)

    @commands.hybrid_group(fallback="", aliases=["e"], help="Edit/create embeds")
    @commands.has_role(File.CommandRole)
    async def embed(self, ctx):
        await ctx.message.delete()
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def create(self, ctx, title:str="\u200b", description:str="\u200b", color:str="blue", url:str=None):
        
        await ctx.message.delete()
        u = ctx.message.author.name

        if await check(self, ctx):
            return

        c = ColorUtil.Get(color)
        
        embed = discord.Embed(title=title, description=description, colour=c, url=url)
        self.Users.append(u)
        self.Embeds.append(embed)
        await ctx.send(embed=embed)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def cfrom(self, ctx, msg:str=None):
        
        await ctx.message.delete()
        u = ctx.message.author.name

        if await check(self, ctx):
            return
        
        link = msg.split("/")
        channel_id = int(link[5])
        message_id = int(link[6])
        message = discord.Message
        
        for c in ctx.guild.text_channels:
            if c.id == channel_id:
                message = await c.fetch_message(message_id)

        e = message.embeds[0]
        self.Users.append(u)
        self.Embeds.append(e)
        await ctx.send(embed=e)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def afield(self, ctx, name:str="\u200b", value:str="\u200b", inline:bool=False):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def rfield(self, ctx, pos:int=0):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.remove_field(pos)
        
        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def fielda(self, ctx, pos:int=0, name:str="\u200b", value:str="\u200b", inline:bool=False):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.insert_field_at(index=pos, name=name, value=value, inline=inline)
        
        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def sfield(self, ctx, pos:int=0, name:str="\u200b", value:str="\u200b", inline:bool=False):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.set_field_at(index=pos, name=name, value=value, inline=inline)
        
        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def cfields(self, ctx):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed = embed.clear_fields()
        
        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def thumbnail(self, ctx, url:str=None):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.set_thumbnail(url=url)

        await ctx.send(embed=embed)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def image(self, ctx, url:str=None):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.set_image(url=url)

        await ctx.send(embed=embed)
        
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def author(self, ctx, name:str="", url:str=None, icourl:str=None):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.set_author(name=name, url=url, icon_url=icourl)
        
        await ctx.send(embed=embed)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def footer(self, ctx, text:str="", image:str=None):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.set_footer(text=text, icon_url=image)

        await ctx.send(embed=embed)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def title(self, ctx, title:str=""):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.title = title

        await ctx.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def desc(self, ctx, desc:str=""):
        
        await ctx.message.delete()
        embed = await get(self, ctx)
        embed.description = desc

        await ctx.send(embed=embed)

    @embed.command()
    @commands.has_role(File.CommandRole)
    async def publish(self, ctx, channel:discord.TextChannel):
        
        await ctx.message.delete()
        embed = await get(self, ctx)

        await channel.send(embed=embed)
    
    @embed.command()
    @commands.has_role(File.CommandRole)
    async def delete(self, ctx):
        
        await ctx.message.delete()
        u = ctx.message.author.name

        value = 0
        for user in range(len(self.Users)):
            if self.Users[user] == u:
                value = user
        
        self.Embeds.pop(value)
        self.Users.pop(value)
        await ctx.send(embed=emb.err_embed("Embed removed!"))

async def setup(bot):
    await bot.add_cog(Embed(bot))

async def check(self, ctx):
    flag = False
    u = ctx.message.author.name
    
    for user in self.Users:
        if user == u:
            await ctx.send(embed=emb.err_embed("You can't work on 2 embeds at the same time!"))
            flag = True
    return flag

async def get(self, ctx):
    u = ctx.message.author.name
    
    for user in range(len(self.Users)):
        if self.Users[user] == u:
            return self.Embeds[user]