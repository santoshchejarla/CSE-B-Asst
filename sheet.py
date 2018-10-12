import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Bot_test').sheet1

Bot_test = sheet.get_all_records()
for i in range (0,len(Bot_test)):
    for x in Bot_test[i]:
        print(Bot_test[i][x])
