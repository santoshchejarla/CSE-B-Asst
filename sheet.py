import gspread
from oauth2client.service_account import ServiceAccountCredentials

#scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Bot_test').sheet1

Bot_test = sheet.get_all_records()

print(Bot_test)