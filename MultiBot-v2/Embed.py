import discord
import File
import AppIndex
from discord.ext import commands

def embed(title: str, description: str):
    embed = discord.Embed(title=title, description=description, color = discord.Color.blue())
    return embed

def add_field(embed, name:str, value: str):
    return embed.add_field(name=name, value=value, inline=False)
    
def end(embed):
    embed.set_footer(text=str(File.Name))
    return embed

def app_embed(app):
    Name = app[File.NameIndex]
    Embed = embed(title=Name[0:-5] + "'s application", description="")
    Q = AppIndex.Get(1)

    for Quest in range(len(app)):
        Answer = app[Quest]
        if Answer == "":
            Answer = "/"  #File.Questions[Quest]
        Embed = add_field(Embed, name=Q[Quest], value=Answer)
    Embed = end(Embed)
    return Embed

def app_list(sheet):
    Embed = embed(title="Applications list", description="")
    
    for app in range(AppIndex.Data() - 2):
        App = AppIndex.Get(app + 3)
        print(app)
        Name = App[File.NameIndex]
        
        Embed = add_field(embed=Embed, name=Name[0:-5], value="INDEX: " + str(app + 3))
    Embed = end(Embed)
    return Embed

def err_embed(err:str):
    return discord.Embed(title="ERROR: ", description=err, color= discord.Color.red())

def log_embed(log):
    #channel = commands.Bot.get_channel()
    embed = discord.Embed(description=str(log), color=discord.Color.yellow())