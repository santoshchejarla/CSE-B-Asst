import telebot
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
 

bot = telebot.TeleBot("642052925:AAHrCbgOuDPE2THSTZnpRYwpkBXDFtzxzeA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"start/help")
	F.close
	bot.reply_to(message, "Hi, here are list of commands available:\n/hi,/about,/desc,/hallo,/ola - Greeting msg\n/tt - displays time-table\n/asgn - displays pending assignments\n/cinfo - displays course info\n/einfo - displays exams info\n/hinfo - displays holidays info\n - Heil CSE-B -")

@bot.message_handler(commands=['hi', 'about','desc','hallo','ola'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(str(datetime.datetime.now())))+" "+"hi")
	F.close
	bot.reply_to(message, "Hie, I live to serve CSE-B")

#-------------- Time table---------------------------#
@bot.message_handler(commands=['tt'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"tt")
	F.close
	if(datetime.datetime.today().isoweekday()==1):
		bot.reply_to(message, "Todays time-table:\n Oops,CIR-SS,Elective,<lunch>,Maths,DS-lab \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==2):
		bot.reply_to(message, "Todays time-table:\n Maths,CIR-verbals,DS,<lunch>,ECE,Oops \n - Heil CSE-B - ")
	if(datetime.datetime.today().isoweekday()==3):
		 bot.reply_to(message, "Todays time-table:\n DS,Maths,ECE-Lab,<lunch>,CIR-Life skills,Oops \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==4):
		bot.reply_to(message, "Todays time-table:\n ECE-Lab,Oops-Lab,<lunch>,Elective,ECE \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==5):
		bot.reply_to(message, "Todays time-table:\n DS,ECE,DS,Maths,<lunch>,ECE \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==6):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==7):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")

#---------------- cinfo ----------------------#	
@bot.message_handler(commands=['cinfo'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"cinfo")
	F.close
	bot.reply_to(message, "Cousers info :\nDS -15CSE201,15CSE281- Krishnaveni\nOops -15CSE202,15CSE282- Kavita Kr\nMaths -15MAT201- \nECE -15ECE202- lakshmi\nECE lab -15ECE281- Pratima\n: CIR :\nManoj - ")

#----------------Not implemented - einfo,hinfo---------#
@bot.message_handler(commands=['einfo', 'hinfo'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"einfo/hinfo")
	F.close
	bot.reply_to(message, "Not implemented")
#----------------asgn---------#
@bot.message_handler(commands=['asgn'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"asgn")
	F.close
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
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"add")
	F.close
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	Bot_test = sheet.get_all_records()
	asgn_text=message.text.split()
	sheet.update_acell("A"+str(len(Bot_test)+2),asgn_text[1])
	sheet.update_acell("B"+str(len(Bot_test)+2),asgn_text[2])
	sheet.update_acell("C"+str(len(Bot_test)+2),asgn_text[3])
	bot.reply_to(message,"Assignment added successfully!")
#------------------delete--------#
@bot.message_handler(commands=['delete'])
def send_welcome(message):
	F = open("log.txt","a")
	F.write("\n"+message.chat.type+" "+message.chat.first_name+" "+message.chat.username+" "+str(str(datetime.datetime.now()))+" "+"delete")
	F.close
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	asgn_text=message.text.split()
	row=str(sheet.findall(asgn_text[1])[0]).split()[1][1]
	sheet.delete_row(int(row))
	bot.reply_to(message,"Assignment deleted successfully!")
bot.polling()
