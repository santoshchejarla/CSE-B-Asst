import telebot
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import base64
 

bot = telebot.TeleBot("642052925:AAHrCbgOuDPE2THSTZnpRYwpkBXDFtzxzeA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	bot.reply_to(message, "Hi, here are list of commands available:\n/hi,/about,/desc,/hallo,/ola - Greeting msg\n/tt - displays time-table\n/asgn - displays pending assignments\n/cinfo - displays course info\n/einfo - displays exams info\n/hinfo - displays holidays info\n - Heil CSE-B -")

@bot.message_handler(commands=['hi', 'about','desc','hallo','ola'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	bot.reply_to(message, "Hie, I live to serve CSE-B")

#-------------- Time table---------------------------#
@bot.message_handler(commands=['tt'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	if(datetime.datetime.today().isoweekday()==1):
		bot.reply_to(message, "Todays time-table:\n Maths,OS,Elective,<lunch>,Embedded,algorithms,Embedded lab \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==2):
		bot.reply_to(message, "Todays time-table:\n Algorithms,CIR-SS,OS,<lunch>,OS lab,Maths \n - Heil CSE-B - ")
	if(datetime.datetime.today().isoweekday()==3):
		 bot.reply_to(message, "Todays time-table:\n Embedded,Algorithms,Algorithms,<lunch>,Maths,OS \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==4):
		bot.reply_to(message, "Todays time-table:\n CIR-QA,CIR-VA,Embedded lab \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==5):
		bot.reply_to(message, "Todays time-table:\n Maths,Embedded,OS<lunch>,Elective,AVP \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==6):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==7):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")

#---------------- cinfo ----------------------#	
@bot.message_handler(commands=['cinfo'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	bot.reply_to(message, "Cousers info :\nDS -15CSE201,15CSE281- Krishnaveni\nOops -15CSE202,15CSE282- Kavita Kr\nMaths -15MAT201- \nECE -15ECE202- lakshmi\nECE lab -15ECE281- Pratima\n: CIR :\nManoj - ")

#----------------Not implemented - einfo,hinfo---------#
@bot.message_handler(commands=['einfo', 'hinfo'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	bot.reply_to(message, "Not implemented")
#----------------asgn---------#
@bot.message_handler(commands=['asgn'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	Bot_test = sheet.get_all_records()
	print_msg=""
	for i in range (0,len(Bot_test)):
		for x in Bot_test[i]:
			print_msg=print_msg+" "+Bot_test[i][x]
	if(print_msg.strip()==""):
		print_msg="No assignments" 
	bot.reply_to(message, print_msg)
#----------------add---------#
@bot.message_handler(commands=['add'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	Bot_test = sheet.get_all_records()
	asgn_text=message.text.split()
	if (len(asgn_text)==4):
		sheet.update_acell("A"+str(len(Bot_test)+2),asgn_text[1])
		sheet.update_acell("B"+str(len(Bot_test)+2),asgn_text[2])
		sheet.update_acell("C"+str(len(Bot_test)+2),asgn_text[3])
		bot.reply_to(message,"Assignment added successfully!")
	else : 
		bot.reply_to(message,"Please follow the correct syntax : /add <subject> <date> <time>")	
#------------------delete--------#
@bot.message_handler(commands=['delete'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	asgn_text=message.text.split()
	if(len(asgn_text)==2):
		try:
			row=str(sheet.findall(asgn_text[1])[0]).split()[1][1]
			sheet.delete_row(int(row))
			bot.reply_to(message,"Assignment deleted successfully!")
		except:
			bot.reply_to(message,"Assignment Not found")
	else : 
		bot.reply_to(message,"Please follow the syntax correctly : /delete <subject>")

#-------------grades-----------#

@bot.message_handler(commands=['grades'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	url = 'https://aumshelper.herokuapp.com/api/aums/grades'
	sheet = client.open('AUMS-API').sheet1
	try:
		row=str(sheet.findall(str(message.json['from']['id'])))
		row = sheet.row_values(row.split()[1][1:2])
		uname = str(row[1])
		password = row[2][2:-1].encode()
		password = base64.b64decode(password)
		password = password.decode()
		data = {'username':uname,'password':password,'options':{'sem':'3'}}
		content = requests.post(url,json=data)
		content = content.json()
		print_msg = "SGPA : " + str(content['data']['SGPA']+"\n")
		for i in range (0,len(content['data']['grades'])):
			print_msg += content['data']['grades'][i]['name']+" "+content['data']['grades'][i]['grade']+"\n"
		bot.reply_to(message, print_msg)
	except :
		bot.reply_to(message, "Unable to request")

#-------------attendance-----------#
@bot.message_handler(commands=['attendance'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	url = 'https://aumshelper.herokuapp.com/api/aums/attendance'
	sheet = client.open('AUMS-API').sheet1
	try:
		row=str(sheet.findall(str(message.json['from']['id'])))
		row = sheet.row_values(row.split()[1][1:2])
		uname = str(row[1])
		password = row[2][2:-1].encode()
		password = base64.b64decode(password)
		password = password.decode()
		data = {'username':uname,'password':password,'options':{'sem':'4'}}
		content = requests.post(url,json=data)
		content = content.json()
		print_msg=""
		for i in range (0,len(content['data'][0])):
			print_msg+=content['data'][i]['name']+" "+content['data'][i]['percentage']+"\n"
		bot.reply_to(message,print_msg)
	except IndexError as e:
		print(e)
		bot.reply_to(message,'unable to process the request')


#------------register--------------_#

@bot.message_handler(commands=['register'])
def send_welcome(message):
	try:
		F = open("log.txt","a")
		F.write("\n")
		F.write(str(message))
		F.write("\n")
		F.close
	except:
		print("Error in logging the request")
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('AUMS-API').sheet1
	try:
		Bot_test = sheet.get_all_records()
		asgn_text=message.text.split()
		if (len(asgn_text)==3):
			sheet.update_acell("A"+str(len(Bot_test)+2),message.json['from']['id'])
			sheet.update_acell("B"+str(len(Bot_test)+2),asgn_text[1])
			password= base64.b64encode(bytes(asgn_text[2],'ascii'))
			sheet.update_acell("C"+str(len(Bot_test)+2),str(password))
			bot.reply_to(message,"User registered successfully!")
		else : 
			bot.reply_to(message,"Please follow the correct syntax : /register <username> <password>")	
	except IndexError as e:
		print(e)
		bot.reply_to(message,'Unable to process the request')

bot.polling()