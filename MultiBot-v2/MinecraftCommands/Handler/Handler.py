import File

class MinecraftContext:

    """
    MinecraftContext (class)
    Represent a context that contains all the command infos

    Methods:

    `reply(message:str)` : sends a private msg on mc to the user
    `send(message:str)` : sends a channel in the server where the command was called

    Attributes:

    `Server` : server (ip, rcon_port, name, perms, dir, bakup_dir)
    `Player` : all player infos
    `Time` : the time when the command was called
    `Guild` : the discord guild of the server
    `Settings` : the settings of the `Config.json` file
    """

    Server = []
    Player = []
    Time = []

    def __init__(self, message):
        pass
    
    def reply(self, message):
        pass

    def send(self, message):
        pass

class MinecraftCommand:
    
    """
    MinecraftCommand (class)
    Represent a bot command that can be sent via MC
    You can declare commands by overwriting the `on_command(self, ctx, *params)` method
    Don't overwrite anything else except for the `on_command` method
    """

    name = ""
    perm = ""
    aliases = []
    help = ""

    def __init__(self, handler=None, name=None, perm=None, aliases:list=None, help=None):

        if name is not None:
            self.name = name
        
        if perm is not None:
            self.perm = perm

        if aliases is not None:
            for alias in aliases:
                self.aliases.append(alias)

        if help is not None:
            self.help = help

        if handler is not None:
            handler.add_command(self)

    def on_command(self, ctx, *param):
        pass

class MinecraftCommandTree(MinecraftCommand):

    """
    MinecraftCommandTree (class)
    Represent a list of `MinecraftCommand`
    You can declare command tree by creating an istance of this class.
    Don't overwrite ths class.
    """
    
    CommandList = []

    def __init__(self, handler=None, name=None, help=None, aliases=None, *commands):

        if name is not None:
            self.name = name

        if help is not None:
            self.help = help

        if aliases is not None:
            for alias in aliases:
                self.aliases.append(alias)

        for command in commands:
                self.CommandList.append(command)

        if handler is not None:
            handler.add_command(self)

    def on_command(self, ctx, *param):
        
        for command in self.CommandList:
            if command.name.startswith(param[0]):
                command.on_command(ctx, param[1:0])

class HelpCommand(MinecraftCommandTree):

    """
    HelpCommand (class)
    It's the default help command that is called with `prefix + help` in a MC chat
    By default it sends a list with all `MinecraftCommandTree` and `MinecraftCommand` with their helpl.

    Usage: `prefix + help` : replies the user with a list of all `MinecraftCommandTree` and `MinecraftCommand`.
    or `prefix + help <MinecraftCommandTree/MinecraftCommand`> : replies the user with the help you set for each command

    Don't overwrite if you want to create a new `HelpCommand`, just code it in your own
    """

    def __init__(self, name="help", help="Displays all the bot commands avaiable on minecraft.", aliases=None, *commands):
        super().__init__(*commands)

    def on_command(self, ctx, *param):
        
        HelpMessage = ""

        if len(param) != 0:
            for command in self.CommandList:
                if command.name == param[0]:
                    
                    HelpMessage.append(command.help)
                    HelpMessage.append("\n")

                    try:
                        list = command.CommandList
                        for c in list:
                            HelpMessage.append(c.help)
                            HelpMessage.append("\n")
                    except:
                        pass

        else:
            for command in self.CommandList:
                HelpMessage.append(command.help)
                HelpMessage.append("\n")

            ctx.reply(HelpMessage)

class CommandHandler:

    """
    CommandHandler (class)
    It handles and processes all `MinecraftCommand` and `MinecraftCommandTree`
    To handle commands just create an istance of this class, and then remember to pass it in the constructor
    """

    CommandList = []
    
    def __init__(self, clist):
        
        for command in clist:
            self.CommandList.append(clist)

    def add_command(self, command):
        self.CommandList.append(command)

    def process(self, message):

        for p in File.CommandPrefix:
            if message.startswith(p):
                for command in self.CommandList:
                    if message.startswith(p + command.name):

                        ctx = MinecraftContext(message=message)
                        param = message[2:] #TODO
                        command.on_command(ctx=ctx, param=param)
                        return True