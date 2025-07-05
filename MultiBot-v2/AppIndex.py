import gspread
from oauth2client.service_account import ServiceAccountCredentials
import File

#file = "D:\py\MultiBot v2\Code/AppIndex.txt"
file = "AppIndex.txt"
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("D:\py\MultiBot v2\Code/creds.json", scope)
client = gspread.authorize(creds)
Sheet = client.open(File.SheetName).sheet1

def Data():
    f = open(file, "r")
    D = f.read()
    f.close()
    return int(D)

def Update(Index):
    f = open(file, "w")
    f.write(str(Index))
    f.close()

def Get(Index:int):
    return Sheet.row_values(Index)