async def Register(Name:str, Dc:str, Ign:str, Id:str):
    print(Name)
    print(Dc)
    print(Ign)
    print(Id)
    with open("Player.txt", "a+") as f:
        f.seek(0)
        data = f.read(100)
        
        if len(data) > 0:
            f.write("\n")
            
        f.write(Name + "," + Dc + "," + Ign + "," + Id)
        f.close()

async def Edit(Player:str, attribute:str, param:str):
    
    player = Query(Player=player, attribute="name")

async def Query(Player:str, attribute=str):

    #0: name, 1: dc name, 2: IGN, 3: app id
    f = open("Player.txt")
    l = f.readlines()

    for c in l:
        line = c.strip()
        t = line.split(",")
        for k in t:
            if k ==  Player:

                if attribute == "name":
                    print(t[0])
                    return t[0]

                if attribute == "dc":
                    print(t[1])
                    return t[1]

                if attribute == "ign":
                    print(t[2])
                    return t[2]

                if attribute == 'id':
                    print(t[3])
                    return t[3]

    f.close()