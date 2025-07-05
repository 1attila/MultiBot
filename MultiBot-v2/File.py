import json

File = "Config.json"

f = open(File, "r")
s = f.read()
d = json.loads(s)
f.close()

## DISCORD
Token = str(d['Discord']['Token']) #Bot token
Name = str(d['Discord']['Name']) #Name of the server
Prefix = str(d['Discord']['Prefix']) #Prefix for the commands
AdminRole = int(d['Discord']['AdminRole']) #Id of the admin role
AppRole = int(d['Discord']['AppRole']) #Id of the app role
MemberRole = int(d['Discord']['MemberRole']) #Id of the member role
TrialRole = int(d['Discord']['TrialRole']) #Id of the trial member role
FriendRole = int(d['Discord']['FriendRole']) #Id of the friend role
CommandRole = int(d['Discord']['CommandRole']) #Id of the role that can use the commands
Guild = int(d['Discord']['Guild']) #Id of your guild

## APPLICATIONS
SheetName = str(d['Applications']['SheetName']) #Name of your google sheet
NameIndex = int(d['Applications']['NameIndex']) #Index of the app name
IgnIndex = int(d['Applications']['IgnIndex']) #Index of the app age
ArchiviedAppCategory = int(d['Applications']['ArchiviedAppCategory']) #Id of the category of the archivied tickets
TicketVoting = int(d['Applications']['TicketVoting']) #Channel to vote the tickets
MemberVoting = int(d['Applications']['MemberVoting']) #Channel to vote for trials / members
AppChannel = int(d['Applications']['AppChannel']) #Channel where display the announcements

## MINECRAFT
BridgeChannel = int(d['Minecraft']['BridgeChannel']) #Id of the channel for the chat 
CommandPrefix = list(d['Minecraft']['CommandPrefix']) #List of prefixs to call bot plugins
RconPass = str(d['Minecraft']['RconPass']) #Password of the server rcon
Servers = list(d['Minecraft']['Servers']) #Servers
MemberTeam = str(d['Minecraft']['MemberTeam']) #Members team in mc
TrialTeam = str(d['Minecraft']['TrialTeam']) #Trials team in mc
GuestTeam = str(d['Minecraft']['GuestTeam']) #Guests team in mc
CheckBlockCoords = list(d['Minecraft']['CheckBlockCoords']) # {Name, server, dim, coords, activity_on, activity_off}
PcprRecordingPath = str(d['Minecraft']['PcprRecordingPath']) #Pcpr recording path