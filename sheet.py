import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
client = gspread.authorize(creds)

sheet = client.open('AUMS-API').sheet1
row=str(sheet.findall('498938058'))
Bot_test = sheet.row_values(row.split()[1][1:2])
print(Bot_test)
