import discord
from discord.ext import commands
import asyncio
import os
import File
import Embed
from DiscordCommands import ChatBridge
import HelpCommand

bot = commands.Bot(command_prefix=File.Prefix, intents=discord.Intents.all())

@bot.event
async def on_message(message):
    
    await ChatBridge.link(message=message)
    await bot.process_commands(message)

    if message.content.startswith(File.Prefix + "help"):
        await message.delete()

@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.errors.CommandNotFound):
        error_msg = 'Command not found'
    elif isinstance(error, commands.errors.CheckFailure):
        error_msg = 'Insufficient permission'
    elif isinstance(error, commands.errors.UserInputError):
        error_msg = 'Invalid usage'
    else:
        raise error

    await ctx.channel.send(embed=Embed.err_embed(error_msg))

@bot.event
async def on_ready():
    await bot.tree.sync()

""" class Help(commands.MinimalHelpCommand):

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(description=page, color=discord.Colour.blue())
            await destination.send(embed=embed)
 """
class Helpcommand(commands.HelpCommand):

    async def prepare_help_command(self, ctx, command:str=None):
        await ctx.message.delete()
        
        if command is None:
            Embed = await HelpCommand.Help()
            await ctx.send(embed=Embed, delete_after=15)
        
        else:
            Embed = await HelpCommand.Command(command, ctx.author)
            await ctx.send(embed=Embed, delete_after=15)

async def load():
    for filename in os.listdir(os.path.abspath(os.getcwd()) + '/DiscordCommands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'DiscordCommands.{filename[:-3]}')

async def main():
    await load()
    await bot.start(File.Token)

bot.help_command = Helpcommand()
asyncio.run(main())