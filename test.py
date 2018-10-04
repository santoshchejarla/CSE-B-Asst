import telebot
import datetime

bot = telebot.TeleBot("642052925:AAHrCbgOuDPE2THSTZnpRYwpkBXDFtzxzeA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi, here are list of commands available:\n\\hi,\\about,\\desc,\\hallo,\\ola - Greeting msg\n\\tt - displays time-table\n\\asgn - displays pending assignments\n\\cinfo - displays course info\n\\einfo - displays exams info\n\\hinfo - displays holidays info\n - Heil CSE-B -")

@bot.message_handler(commands=['hi', 'about','desc','hallo','ola'])
def send_welcome(message):
	bot.reply_to(message, "Hie, I live to serve CSE-B")

#-------------- Time table---------------------------#
@bot.message_handler(commands=['tt'])
def send_welcome(message):
	if(datetime.datetime.today().isoweekday()==1):
		bot.reply_to(message, "Todays time-table:\n DS,CIR-SS,Elective,--,Maths,DS-lab \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==2):
		bot.reply_to(message, "Todays time-table:\n Maths,CIR-verbals,Oops,--,ECE,DS \n - Heil CSE-B - ")
	if(datetime.datetime.today().isoweekday()==3):
		 bot.reply_to(message, "Todays time-table:\n DS,Maths,ECE-Lab,--,CIR-Life skills,Oops \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==4):
		bot.reply_to(message, "Todays time-table:\n ECE-Lab,Oops-Lab,--,Elective,ECE \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==5):
		bot.reply_to(message, "Todays time-table:\n Oops,ECE,DS,Maths,--,Oops,ECE \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==6):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")
	if(datetime.datetime.today().isoweekday()==7):
		bot.reply_to(message, "Sorry, I don't work on weekends :P \n - Heil CSE-B -")

#---------------- cinfo ----------------------#	
@bot.message_handler(commands=['cinfo'])
def send_welcome(message):
	bot.reply_to(message, "Cousers info :\nDS -15CSE201,15CSE281- Krishnaveni\nOops -15CSE202,15CSE282- Kavita Kr\nMaths -15MAT201- \nECE -15ECE202- lakshmi\nECE lab -15ECE281- Pratima\n: CIR :\nManoj - ")

#----------------Not implemented - einfo,hinfo---------#
@bot.message_handler(commands=['einfo', 'hinfo'])
def send_welcome(message):
	bot.reply_to(message, "Not implemented")

bot.polling()