import discord
from discord.ext import commands
import File

class AcceptButton(discord.ui.View):

    def __init__(self, *, timeout=180, app, channel):
        super().__init__(timeout=timeout)
        self.app = app
        self.channel = channel

    @discord.ui.button(label="ACCEPT", style=discord.ButtonStyle.green)
    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("Accept button pressed!")

        ruser = interaction.user.roles

        #after the check
        self.channel.edit(category=File.ArchiviedAppCategory)
        

class DenyButton(discord.ui.View):

    def __init__(self, *, timeout=180, app):
        super().__init__(timeout=timeout)
        self.app = app

    @discord.ui.button(label="DENY", style=discord.ButtonStyle.red)
    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        print("Deny button pressed!")