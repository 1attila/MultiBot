from rcon import Client
import socket
import File

async def get(Server:str=None):

    """
    get(Server -> your server name / index)
    It returns the index of that server.
    """
    
    if Server is not None and len(Server) > 0:

        for server in range(len(File.Servers)):
            s = File.Servers[server]

            try:
                if server == int(Server): #index
                    return server

	    except Exception:
		...

            for n in range(len(s[0])): #names
                if s[n] == Server:
                    return server

    else:
        return None

async def exe(server:int=0, command:str="say Hello world"):

    """
    exe(server -> your server(index/name), command -> your command (str))
    """

    Server = File.Servers[await get(server)]

    response = ""

    try:
        with Client("127.0.0.1", Server[1], passwd=File.RconPass, timeout=15) as client:
            response = client.run(command)

    except socket.timeout:
        response = "Couldn't reach the server in time"

    return response