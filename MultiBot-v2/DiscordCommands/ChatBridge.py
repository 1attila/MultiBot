"""
Python module to link minecraft servers and discord.
Made by attila
"""

import discord
from discord.ext import commands
import File
from rcon import Client
import socket
import asyncio
import pygtail
import json
from cleantext import clean
from MinecraftCommands.Handler.Command import Handler as h

file = open("Bridge.json", "r")
s = file.read()
Message = json.loads(s)
file.close()
Messages1 = Message["Messages1"]
Messages2 = Message["Messages2"]

class ChatBridge(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("ChatBridge cog loaded")
		
		for guild in self.bot.guilds:
			if guild.id == File.Guild:
				for channel in guild.text_channels:
					if channel.id == File.BridgeChannel:
						self.channel = channel
						self.guild = guild
		print("Bridge init")
		while True:
			for server in range(len(File.Servers)):
				s = File.Servers[server]
				
				for line in pygtail.Pygtail(s[3] + "logs/latest.log"):
					if line.__contains__("[Server thread/INFO]:"):
						message = await check(line, server)
						
						if len(message) > 0:
							try:
								await self.channel.send(content=await format(message, self.guild))
								await bridge(message=message, server=server)
							except:
								pass
							
				await asyncio.sleep(1)

async def check(line, server):
	
	Server = File.Servers[server]
	s = Server[0]
	message = str("")
	F = False
	sname = str("[" + s[0] + "] ")
        
	if line.__contains__("[Server thread/INFO]: <"):
		F = True        
		message += sname
		m = line.split(" ")

		l = m[3:]
		for item in l:
			message += item
			message += " "
        
		im = m[4]

		for prefix in File.CommandPrefix:
			if im.startswith(prefix):
				message = ""
	
	if line.__contains__("[Server thread/INFO]: [Server]") and F == False:
		F = True
		message += sname
		message += ("<Server>")
		l = line.split("]")
                
		m = l[3:]
		for item in m:
			message += item
			message += " "
                        
		im = m[0]
		
		for prefix in File.CommandPrefix:
			if im.startswith(prefix):
				message = ""
	
	if F == False:
		for msg in Messages1:
				if line.__contains__(msg):
					F = True
					message = ""
                                        
					m = line.split(" ")
					l = m[3:]
					message += sname
                                        
					for item in l:
						message += item
						message += " "
                
	if F == False:
		for msg in Messages2:
			if line.__contains__(msg):
				F = True
				message = ""
				
				m = line.split("]")
				l = m[2]
				message += sname
				message += l[3:]

	if h.process(message=line):
		message = ""

	return message

async def format(message, guild):
	if message.__contains__("@"):
		for member in guild.members:
			if message.__contains__("@" + member.name):
				message = message.replace("@" + member.name, "<@" + str(member.id) +">")
				
			elif message.__contains__("@" + member.display_name):
				message = message.replace("@" + member.display_name, "<@" + str(member.id) + ">")
	
	if message.__contains__("#"):
		for channel in guild.text_channels:
			s = clean(channel.name, no_emoji=True)
			if "#" + s in message and len(s) > 0:
				message = message.replace("#" + s, "<#" + str(channel.id) + ">")

			if s.startswith("-"):
				s = s.replace("-", "", 1)
				if "#" + s in message and len(s) > 0:
					message = message.replace("#" + s, "<#" + str(channel.id) + ">")
	
	return message

async def bridge(message, server=-1):
    
	for s in range(len(File.Servers)):
		if s != server:
			s1 = File.Servers[s]
			try:
				with Client("127.0.0.1", int(s1[1]), passwd=File.RconPass, timeout=15) as client:
					response = client.run('tellraw @e[type=minecraft:player] {"text":"' + message + '", "color":"gray"}')
			except socket.timeout:
				pass

async def link(message):
	if message.channel.id == File.BridgeChannel:
		await bridge(message="[DISCORD] <" + str(message.author.name) + "> " + str(message.content))

async def setup(bot):
    await bot.add_cog(ChatBridge(bot))