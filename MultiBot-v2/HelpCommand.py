"""
Help commands
"""

import File
import discord
from discord.ext import commands

p = File.Prefix
server = File.Servers[0]
s = server[0]
#!help
#
# MultiBot commands, categories and functions help
# MultiBot contains loads of functions and categories, so to know some info about something type:
# `functions` to get the list of all avaiable functions
# `commands` to get the list of commands that aren't in a category
# `categories` to get the list of all avaiable categories
# `<command_name>` to get infos about a specific command
# `<category_name>` to get infos about a specific category
# `<function` to get infos about a specific function

#remember: quotes etc, parameters

ChatBridge = {
    "Name" : "ChatBridge",
    "Description" : "It links all your minecraft servers between them and BRIDGE-CHANNEL",
    "Notes" : "None"
}

ApplicationsHandling = {
    "Name" : "Application",
    "Description" : "It handles forms, voting, trials, members etc regarding applications",
    "Notes" : "None"
}

Register = {
    "Name" : "Register",
    "Description" : "Allows you to register someone so you can pass him as parameter in many ways",
    "Notes" : "Options: \n `ign`, \n `nick`, \n `Dc nick`, \n `app id`"
}

PluginsViaDicord = {
    "Name" : "Plugins via discord",
    "Description" : "It allows you to run some discord commands from minecraft",
    "Notes" : "None"
}

Functions = [ChatBridge, ApplicationsHandling, PluginsViaDicord]


app_list = {
    "Name" : "list",
    "Desc" : "It sends a list with all the applicant's name",
    "Usage" : p + "`app list`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "the message will be deleted after 30 seconds"
}

app_count = {
    "Name" : "count",
    "Desc" : "It returns the number of the applicantions you got",
    "Usage" : p + "`app count`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "the message will be deleted after 30 seconds"
}

app_show = {
    "Name" : "show",
    "Desc" : "It shows the form sent from a specific applicant in a embed",
    "Usage" : p + "`app show <applicant>`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "<applicant> is a parameter that could be: \n -nick of the applicant, \n -his ign \n his index \n -his discord name (no tag)",
}

app_process = {
    "Name" : "process",
    "Desc" : "Processes an application that wasn't processed due to a bad compilation of the form",
    "Usage" : p + "`app process <id> <Dc_nick>`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "<id> is the id of the app, <Dc_nick> is the applicant's discord nick (with his tag)"
}

app_deny = {
    "Name" : "deny",
    "Desc" : "Denies an applicant and archieves the channel",
    "Usage" : p + "`app deny <applicant>`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "<applicant> is could be: \n -applicant's nick, \n -his dc nick (no tag), \n -his ign, \n his index, \n None if you type this in his channel"
}

app_accept = {
    "Name" : "accept",
    "Desc" : "Gives to the applicant the trial-role, whitelists him everywhere with rigth permissions and archieves the channel",
    "Usage" : p + "`app accept <applicant>`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "<applicant> is could be: \n -applicant's nick, \n -his dc nick (no tag), \n -his ign, \n his index, \n None if you type this in his channel"
}

app_vote = {
    "Name" : "vote",
    "Desc" : "Creates a poll to vote for a trial in APP-VOTING",
    "Usage" : p + "`app vote <trial>`",
    "Perms" : "Amin-only",
    "Channels" : "full-member channels",
    "Notes" : "<trial> is could be: \n -trial's nick, \n -his dc nick (no tag), \n -his ign, \n his index, \n None if you type this in his channel"
}

app_embed = {
    "Name" : "embed",
    "Desc" : "Sets the embed to open or close applications",
    "Usage" : p + "`app embed <type> <applicant>`",
    "Perms" : "Admins-only",
    "Channels" : "full-member channels",
    "Notes" : "<type> could be `open` or `close`, <embed> is a link to the message that contains the embed"
}

app_open = {
    "Name" : "open",
    "Desc" : "Opens the applications by sending the `app open` embed in APP-CHANNEL (see `app embed` to set the embed)",
    "Usage" : p + "`app open`",
    "Perms" : "Amins-only",
    "Channels" : "full-member channels",
    "Notes" : "None"
}

app_close = {
    "Name" : "close",
    "Desc" : "Closes the applications by sending the `app close` embed in APP-CHANNEL (see `app embed` to set the embed)",
    "Usage" : p + "`app close`",
    "Perms" : "Amins-only",
    "Channels" : "full-member channels",
    "Notes" : "None"
}

app_info = {
    "Name" : "info",
    "Desc" : "Displays some useful infos about the applications",
    "Usage" : p + "`app info`",
    "Perms" : "Members-only",
    "Channels" : "full-member channels",
    "Notes" : "None"
}

Applications = {
    "Name" : "app",
    "Desc" : "applications handling",
    "Aliases" : p + "`a`",
    "Commands" : [app_info, app_count, app_list, app_show, app_embed, app_open, app_close, app_process ,app_accept, app_deny, app_vote],
    "Notes" : "None"
}

e_create = {
    "Name" : "create",
    "Desc" : "Allows you to create an embed",
    "Usage" : p + "`embed create <title> <description> <color> <url>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<color> must be a discord color (type: `color list` for infos about them), <url> must be a real url. \n Every parameter is not necessary"
}

e_title = {
    "Name" : "title",
    "Desc" : "Sets the embed title",
    "Usage" : p + "`embed title <title>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

e_desc = {
    "Name" : "desc",
    "Desc" : "Sets the embed description",
    "Usage" : p + "`embed desc <description>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

e_cfrom = {
    "Name" : "cfrom",
    "Desc" : "Creates an embed from a already existing one",
    "Usage" : p + "`embed create <message_link>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<message_link> must be a link to the message that contains the embed"
}

e_afield = {
    "Name" : "afield",
    "Desc" : "Appends a field to your embed",
    "Usage" : p + "`embed afield <name> <value> <inline>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<inline> parameter can be true or false only. \n Every parameter it's not necessary"
}

e_rfield = {
    "Name" : "afield",
    "Desc" : "Removes a field in a specific position in your embed",
    "Usage" : p + "`embed rfield <pos>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<pos> must be a number. \n Fields starts from 0. \n Default pos value is 0"
}

e_fielda = {
    "Name" : "fielda",
    "Desc" : "Adds a field in a specific position in your embed",
    "Usage" : p + "`embed fielda <pos> <name> <value> <inline>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<pos> must be a number. \n Fields starts from 0. \n Default pos value is 0. \n <inline> can be true or false only",
}

e_sfield = {
    "Name" : "sfielda",
    "Desc" : "Changes the field in a specific pos with the given arguments",
    "Usage" : p + "`embed sfielda <pos> <name> <value> <inline>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<pos> must be a number. \n Fields starts from 0. \n Default pos is 0. \n <inline> can be true or false only"
}

e_cfields = {
    "Name" : "cfields",
    "Desc" : "Clears all your fields from your embed",
    "Usage" : p + "`embed cfields`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

e_thumbnail = {
    "Name" : "thumbnail",
    "Desc" : "Sets the embed thumbnail with the given image",
    "Usage" : p + "`embed thumbnail <url>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<url> must be a real url"
}

e_image = {
    "Name" : "image",
    "Desc" : "Sets the embed image with the given image",
    "Usage" : p + "`embed image <url>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<url> must be a real url"
}

e_author = {
    "Name" : "author",
    "Desc" : "Sets the embed author with the given infos",
    "Usage" : p + "`embed author <name> <url> <icon_url>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<url> and <icon_url> must be a real urls"
}

e_footer = {
    "Name" : "footer",
    "Desc" : "Sets the embed footer with the given infos",
    "Usage" : p + "`embed footer <text> <image>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<image> must be a real url. \n Every parameter is not necessary"
}

e_publish = {
    "Name" : "publish",
    "Desc" : "Sends the embed in a channel",
    "Usage" : p + "`embed publish <channel>`",
    "Perms" : "Admin-only",
    "Channels" : "member channels",
    "Notes" : "<channel> must be a channel mention"
}

e_delete = {
    "Name" : "delete",
    "Desc" : "Deletes the embed from your list, so you can work on other ones",
    "Usage" : p + "`embed delete`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

e_qembed = {
    "Name" : "qembed",
    "Desc" : "Creates a embed quickly but with a few limitations",
    "Usage" : p + "`qembed <title> <desc> <footer> <color> <fields>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "<color must be a discord color (type `color list` for infos abotu them). \n <fields> must contain: `<name> <value> <inline>`, <inline> can be true or false only",
}

Embeds = {
    "Name" : "embed",
    "Desc" : "embeds editor",
    "Aliases" : p + "`e`",
    "Commands" : [e_qembed, e_create, e_title, e_desc, e_cfrom, e_afield, e_rfield, e_fielda, e_sfield, e_fielda, e_cfields, e_thumbnail, e_image, e_author, e_footer, e_publish, e_delete],
    "Notes" : "You can create/edit one embed per time."
}

m_propose = {
    "Name" : "propose",
    "Desc" : "Proposes an argument that will be discussed at the next meeting",
    "Usage" : p + "`meeting propose <argument_name> <argument_desc>`",
    "Perms" : "Members-only",
    "Channels" : "Meeting arguments",
    "Notes" : "None"
}

m_start = {
    "Name" : "start",
    "Desc" : "Use this when the meeting starts",
    "Usage" : p + "`meeting start <meeting_data> <next_meeting_data>`",
    "Perms" : "Admins-only",
    "Channels" : "Meeting logs",
    "Notes" : "None"
}

m_end = {
    "Name" : "end",
    "Desc" : "Use this when the meeting ends",
    "Usage" : p + "`meeting end <next_meeting_data>`",
    "Perms" : "Admins-only",
    "Channels" : "Meeting arguments",
    "Notes" : "None"
}

m_answer = {
    "Name" : "answer",
    "Desc" : "Use this command to answer an argument",
    "Usage" : p + "`meeting answer <argument_name> <argument_answer>`",
    "Perms" : "Admins-only",
    "Channels" : "Meeting logs",
    "Notes" : "None"
}

Meetings = {
    "Name" : "meeting",
    "Desc" : "meetings handler",
    "Aliases" : p + "`meeting`",
    "Commands" : [m_end, m_propose, m_start, m_start],
    "Notes" : "Commands order should be `end`, `propose`, `start`, `answer`"
}


p_poll = {
    "Name" : "poll",
    "Desc" : "Use this command to create a poll",
    "Usage" : p + "`poll <argument> <options>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "you can add as many <options> as you want. \n to create an option do: emoji that you want + space + option"
}

p_bpoll = {
    "Name" : "bpoll",
    "Desc" : "Use this command to create a poll with only 2 options: true or false",
    "Usage" : p + "`poll <argument>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

Polls = {
    "Name" : "poll",
    "Desc" : "polls handler",
    "Aliases" : p + "`poll`",
    "Commands" : [p_poll, p_bpoll],
    "Notes" : "None"
}


b_cchannel = {
    "Name" : "cchannel",
    "Desc" : "Use this command to create a new channel",
    "Usage" : p + "`bot cchannel <name>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

b_send = {
    "Name" : "send",
    "Desc" : "Send that message in that channel",
    "Usage" : p + "`bot send <message>`",
    "Perms" : "Kinda-Memebr",
    "Channels" : "member channels",
    "Notes" : "The message must contain only text"
}

b_stex = {
    "Name" : "cchannel",
    "Desc" : "Same of " + p + "`bot send <text>` but text is `like this`",
    "Usage" : p + "`bot cchannel <name>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "None"
}

Bot = {
    "Name" : "bot",
    "Desc" : "Random bot commands",
    "Aliases" : p + "`bot`",
    "Commands" : [b_cchannel, b_send, b_stex],
    "Notes" : "None"
}

Status = {
    "Name" : "status",
    "Desc" : "Use this command to get the status of a server",
    "Usage" : p + "`status <thing>`",
    "Perms" : "Members-only",
    "Channels" : "member channels",
    "Notes" : "if <thing> is leaved empty it will display the status of every server"
}

Ip = {
    "Name" : "ip",
    "Desc" : "Displays the server ip",
    "Usage" : p + "`ip`",
    "Perms" : "public",
    "Channels" : "public channels",
    "Notes" : "None"
}

Ping = {
    "Name" : "ping",
    "Desc" : "Displays the bot latency",
    "Usage" : p + "`ping`",
    "Perms" : "public",
    "Channels" : "public channels",
    "Notes" : "None"
}

Info = {
    "Name" : "info",
    "Desc" : "Displays some info's about the bot",
    "Usage" : p + "`info`",
    "Perms" : "public",
    "Channels" : "public channels",
    "Notes" : "None"
}

Color = {
    "Name" : "color",
    "Desc" : "Displays all the colors avaiable on discord",
    "Usage" : p + "`color <'list'>`",
    "Perms" : "public",
    "Channels" : "public channels",
    "Notes" : "if <list> is empty it will send every color"
}

Execute = {
    "Name" : "execute",
    "Desc" : "Execute something in a server",
    "Usage" : p + "`execute <command> <server>`",
    "Perms" : "Kinda-Member",
    "Channels" : "member channels",
    "Notes" : "default <command> is 'say hello world', default <server> is " + s[0]
}


CommandsCategory = [Embeds, Applications, Meetings, Polls, Bot]
Commands = [Status, Ip, Ping, Info, Color, Execute]

async def Help():

    embed = discord.Embed(title=File.Name + "'s bot help",
                          description= File.Name + "'s bot contains loads of functions, commands and categories, so to know any info about something type:",
                          color=discord.Color.blue(),
                          url="https://github.com/1attila/MultiBot-v1")
    
    embed.set_author(name="Attila", 
                     url="https://github.com/1attila", 
                     icon_url="https://avatars.githubusercontent.com/u/116733342?s=400&u=b6899757884244a6baf6c6f983182b8988966a6f&v=4")
    
    embed.set_footer(text=File.Name, icon_url="https://yt3.googleusercontent.com/D4YdYI7h8251ThUxsot8gVOPRr31oe4E5fA0hl7P5CgcroaHojfPpMGbmq0i0Yrr-74Owhwkiw=s88-c-k-c0x00ffffff-no-rj")

    Suggester = [
        "`" + p + "help functions` ",
        "`" + p + "help commands` ",
        "`" + p + "help categories` ",
        "`" + p + "help <command_name>` ",
        "`" + p + "help <category_name>` ",
        "`" + p + "help <function>` "
    ]

    Help = [
        "to get the list of all avaiable functions",
        "to get the list of commands that aren't in a category",
        "to get the list of all avaiable categories",
        "to get infos about a specific command",
        "to get infos about a specific category",
        "to get infos about a specific function"
    ]

    for item in range(len(Help)):
        embed.add_field(name=Suggester[item], value=Help[item], inline=False)

    return embed

async def Command(command, author):
    
    if command == "categories":

        embed = discord.Embed(
                title="Categories",
                description="Total categories: " + str(len(CommandsCategory)),
                color=discord.Color.blue()
        )
        embed.set_footer(text=File.Name)

        for item in CommandsCategory:
            embed.add_field(name=item["Name"], value=item["Desc"], inline=False)
        
        return embed

    elif command == "commands":

        embed = discord.Embed(
            title="Commands",
            description="\u200b",
            color=discord.Color.blue()
        )
        for item in Commands:
            embed.add_field(name = item["Name"], value=item["Usage"], inline=False)
        
        return embed
    
    elif command == "functions":
        
        embed = discord.Embed(
            title="Functions",
            description="\u200b",
            color=discord.Color.blue()
        )

        for item in Functions:
            v = item["Notes"] if item["Notes"] != "None" else "\u200b"
            embed.add_field(name=item["Name"], value=item["Description"] + v, inline=False)

        return embed
    
    else:
        for item in CommandsCategory:
            if item["Name"] == command:
            
                embed = discord.Embed(
                    title=item["Name"],
                    description=item["Desc"] + "\n Aliases: " + item["Aliases"],
                    color=discord.Color.blue()
                )
                
                for k in item["Commands"]:
                    embed.add_field(name=k["Name"], value=k["Usage"], inline=False)
                
                if item["Notes"] != "None":
                    embed.add_field(name="Notes", value=item["Notes"], inline=False)
            
                return embed

        for item0 in CommandsCategory:
            if command.startswith(item0["Name"]):
                
                for c in item0["Commands"]:
                    if command == item0["Name"] + " " + c["Name"]:
                        
                        embed = discord.Embed(
                            title=item0["Name"] + " " + c["Name"],
                            description=c["Desc"],
                            color=discord.Color.blue()
                        )
                        
                        embed.add_field(name="Usage", value=c["Usage"], inline=False)
                        embed.add_field(name="Perms", value=c["Perms"], inline=False)
                        embed.add_field(name="Channels", value=c["Channels"], inline=False)
                        
                        if c["Notes"] != "None":
                            embed.add_field(name="Notes", value=c["Notes"], inline=False)
                        
                        return embed
        
        for item1 in Commands:
            if command == item1["Name"]:
                
                embed = discord.Embed(
                    title=item1["Name"],
                    description=item1["Desc"],
                    color=discord.Color.blue()
                )
                embed.add_field(name="Usage", value=item1["Usage"], inline=False)
                embed.add_field(name="Perms", value=item1["Perms"], inline=False)
                embed.add_field(name="Channels", value=item1["Channels"], inline=False)

                if item1["Notes"] != "None":
                    embed.add_field(name="Notes", value=item1["Notes"], inline=False)
                        
                return embed

        for item2 in Functions:
            if command == item2["Name"]:
                
                n = item2["Notes"] if item2["Notes"] != "None" else " "

                embed = discord.Embed(
                    title=item2["Name"],
                    description=item2["Description"] + n,
                    color=discord.Color.blue()
                )

                return embed

#MEMBER
Member = "lists/counts the members with that role. Usage: `" + p +"member <role> <count/list>`"
#ROLE
Role = "adds/removes a role from a member. Usage: `" + p + "role <role> <add/remove> <@member>`"
#POLL
Poll = "creates a poll, it can handle more options. Usage: `" + p + "poll <argument> <options>`"
Bpoll = "creates a poll with only 2 options: yes or not. Usage: `" + p + "bpoll <argument>`"
#PING
Ping = "displays the bot ping. Usage: `" + p + "ping`"
#APP
A_List = "displays a list with all the applicants names. Usage: `" + p + "app list`"
A_Count = "displays the number of all the apps. Usage: `" + p + "app count`"
A_Show = "dislays the form of an applicant. Usage: `" + p + "app show <id/ign/name/ds name/last>`"
A_Deny =  "deny an applicant. Usage: `" + p + "app deny <id/ign/name/ds name/none (if you type this in the applicant's channel)>`"
A_Accept = "accepts an applicant. Usage: `" + p + "app accept <dc/ign/name/ds name/none (if you type this in the applicant's chanel)>`"
A_Vote = "votes for a trial. Usage: `" + p + "app vote <dc/ign/name/ds name/none (if you type this in the trial's channel)>`"
A_Open = "opens the applications. Usage: `" + p + "app open`"
A_Close = "closes the applications. Usage: `" + p + "app close`"
A_Embed = "sets the embed to close/open applications. Usage: `" + p + "app embed <open/close> <message_link>`"
A_Info = "displays some useful infos about applications. Usage: `" + p + "app info`"
#EMBED
E_Quick = "this commands allows you to create simple embeds quickly. Usage: `" + p + "qembed <title> <description> <footer> <color> <fields>`. \n You can add many fields, every field must have 3 parameters: `<name> <value> <inline>"
E_Create = ""
