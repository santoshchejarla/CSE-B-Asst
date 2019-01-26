import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import base64
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
client = gspread.authorize(creds)
url = 'https://aumshelper.herokuapp.com/api/aums/attendance'
sheet = client.open('AUMS-API').sheet1
row=str(sheet.findall(str()))
row = sheet.row_values(row.split()[1][1:2])
print(row[1])
print(row[2].encode())
uname = row[1]
pwd = row[2][2:-1].encode()
pwd = base64.b64decode(pwd)
print(uname+" "+pwd.decode())
data = {'username':uname,'password':pwd.decode(),'options':{'sem':'4'}}
content = requests.post(url,json=data)
print(content.json())
content = content.json()
for i in range (0,len(content['data'][0])):
    print(content['data'][i]['name']+" "+content['data'][i]['percentage'])

