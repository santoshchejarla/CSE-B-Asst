import telebot
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

bot = telebot.TeleBot("642052925:AAHrCbgOuDPE2THSTZnpRYwpkBXDFtzxzeA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi, here are list of commands available:\n/hi,/about,/desc,/hallo,/ola - Greeting msg\n/tt - displays time-table\n/asgn - displays pending assignments\n/cinfo - displays course info\n/einfo - displays exams info\n/hinfo - displays holidays info\n - Heil CSE-B -")

@bot.message_handler(commands=['hi', 'about','desc','hallo','ola'])
def send_welcome(message):
	bot.reply_to(message, "Hie, I live to serve CSE-B")

#-------------- Time table---------------------------#
@bot.message_handler(commands=['tt'])
def send_welcome(message):
	if(datetime.datetime.today().isoweekday()==1):
		bot.reply_to(message, "Todays time-table:\n MATHS,OS,ELECTIVE,--,EMBEDDED SYSTEMS,ALGORITHMS,EMBEDDED SYSTEMS LAB\n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==2):
		bot.reply_to(message, "Todays time-table:\n ALGORITHMS,CIR-soft skills,OS,--,OS LAB,MATHS\n - Heil CSE-B - ")
	if(datetime.datetime.today().isoweekday()==3):
		 bot.reply_to(message, "Todays time-table:\n EMBEDDED SYSTEMS,ALGORITHMS,ALGORITHMS,--,MATHS,OS\n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==4):
		bot.reply_to(message, "Todays time-table:\n CIR(QA),CIR(VA)\n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==5):
		bot.reply_to(message, "Todays time-table:\n MATHS,EMBEDDED SYSTEMS,OS,--,ELECTIVE,AVP \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==6):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==7):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")

#---------------- cinfo ----------------------#	
@bot.message_handler(commands=['cinfo'])
def send_welcome(message):
	bot.reply_to(message, "Cousers info :\n-15MAT213 :- SATHI DEVI \n-15CSE213,15CSE286(OS) :- GAYATRI \n-15CSE285,15CSE212(EMBEDDED SYSTEMS) :- ANU\n15CSE211(ALGORITHMS) :- PADMAMALA")

#----------------Not implemented - einfo,hinfo---------#
@bot.message_handler(commands=['einfo', 'hinfo'])
def send_welcome(message):
	bot.reply_to(message, "Not implemented")
#----------------asgn---------#
@bot.message_handler(commands=['asgn'])
def send_welcome(message):
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('Bot_test').sheet1
	Bot_test = sheet.get_all_records()
	print_msg=""
	for i in range (0,len(Bot_test)):
		for x in Bot_test[i]:
			print_msg=print_msg+" "+Bot_test[i][x]
	if(print_msg.strip()==""):
		print_msg="No assignments " 
	bot.reply_to(message, print_msg)
bot.polling()
