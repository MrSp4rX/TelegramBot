#!/usr/bin/env python
# -- coding: utf-8 --

import logging
import os
from threading import Thread
import wikipedia
from tbomb import bomber
from api import Api
import scrap
from random import choice
from os import environ, popen
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from subprocess import getoutput

def nmap(target):
	open_ports = []
	services = []
	status = ''
	os = ''

	data = getoutput(f'./nmap/bin/nmap {target} -A').split('\n')
	for _ in data:
		if not _ == '' and _.split('/')[0].isdigit():
			open_ports.append(_.rstrip().split()[0].split('/')[0]+':'+_.split()[2])
			if len(_.split()) == 4:
				services.append(_.split()[3])
		elif 'Host is ' in _:
			status = _.split(' ')[2]
		elif 'Running ' in _:
			os = _.split(':')[1].lstrip()
	if not services:
		services = 'could not detect'
	if not os:
		os = 'could not detect'
	return status, open_ports, services, os



ispammer_reply = [
	'500 se Jada msgs uski gand me dalega???',
	'API tera baap lakar dega madarchod?',
	'Websites ka ghata hoga mt kr bro. We are Good not Bad.'
	'Gand maar dunga itne msgs bhejega to.',
	'Baap ka maal samjha hai?',
	'Ek baar me samajh jaya kr.',
	'Baap ke auzar ke sath chhedkhani nahi.'
	'Sare msgs tere number pr Daal du ga agar nahi maana to bhsdk.',
	'Kitni jawan chadhi hai beta?',
	'Bro yahi kam hai bs?? Muttha pelna chhod diya???',
	'Jakar Kapde dho le fr kr ye sab.',
	'Beta Tumse naa ho Payega',
	'Tu TikToker hai kya? Bhsdk slow motion me tha Ab kuch jada hi jaldi hai.'
	'Ruko Zara Sabar karo thoda',
	'Uski aj gand maar ke hi manega bhsdk???',
	'Mere lund ko aram de bhsdk thak gaya.'
]

# Defining Abuse Words
abuse = ['lavda','bhosadike','madarchod','bsdk', 'bhsdk', 'betichod', 'chod', 'lund', 'gand ', 'jerk', 'lode', 'loda', 'madarchod', 'mdrchod', 'madar', 'chut', 'bc', 'mkchut', 'mc','mkc','jhat','suwar','kutte','randi','bhosadi','m4drch0d','m4d4rch0d','mdrch0d','b#05adik3','bh05adik3','bh0sadike','bh0sad!ke','bho5adike','bh0sadike','bh0sad!ke','ch0d','m4d4rch0d','land','m@d@rc#0d','m@d@rch0d','m@d@rchod','l4nd','.bhosadike','.madarchod','.bsdk', '.bhsdk', '.betichod', '.chod', '.gand ', '.jerk', '.lode', '.loda', '.madarchod', '.mdrchod', '.madar', '.chut', '.bc', '.mkchut', '.mc','.mkc', '.jhat','.suwar','.kutte','.randi','.bhosadi','.m4drch0d','.m4d4rch0d','.mdrch0d','.b#05adik3','.bh05adik3','.bh0sadike','.bh0sad!ke','.bho5adike','.bh0sadike','.bh0sad!ke','.ch0d','.m4d4rch0d','.land','.m@d@rc#0d','.m@d@rch0d','.m@d@rchod','.l4nd','bhosadike.','madarchod.','bsdk.', 'bhsdk.', 'betichod.', 'chod.', 'gand ', 'jerk.', 'lode.', 'loda.', 'madarchod.', 'mdrchod.', 'madar.', 'chut.', 'bc.', 'mkchut.', 'mc.','mkc.','lund','jhat.','suwar.','kutte.','randi.','bhosadi.','m4drch0d.','m4d4rch0d.','mdrch0d.','b#05adik3.','bh05adik3.','bh0sadike.','bh0sad!ke.','bho5adike.','bh0sadike.','bh0sad!ke.','ch0d.','m4d4rch0d.','land.','m@d@rc#0d.','m@d@rch0d.','m@d@rchod.','l4nd.']

# Defining Reply for abuse words
abuse_reply = [
	'Bhosadi ke aisa thappad marunga tere muh ke dant gad se hoker girenge.',
	'Jija se bkchodi krta hai maderchod tamiz sikh lowde.',
	'Gand mei tere salayi ghusa ke swetter bna dunga.',
	'Jhant khayega mera behen ke lowda.',
	'Teri ammy ka asiq hun wo v khufiya asiq ati hai mujhse chummiya lene apne chut pe.',
	'Teri ammy ke gand ko mukka marke tod dunga maderchod baap se bakchodi',
	'Bhagg maderchod teri ammy toh nukkad ki randi hai re.',
	'300 rs wali randi ke aulad.',
	'Teri behn ko utha ke salwar ke sath hi pelunga.',
	'Hahahaha gandu tera baal pakad ke diwal se lada lada ke tera seer phod ke teri ammy ka mang bharunga',
	'Madarchod Zuban pe conrol karo warna gand faad denge',
	'Your Dady can only Abuse Samjha  Bhosadike'
]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def echo(update, context):
    string = update.message.text
    for word in abuse:
    	if word in string.lower() and update.message.from_user['username'] != 'MrSp4rX':
    		update.message.reply_text( choice(abuse_reply))
    	
    if string.startswith('/'):
    	if '/image' in string:
    		string = string.replace('/image', '')
    		update.message.reply_text(scrap.main(string))
    		
    	elif '/start' in string:
    		update.message.reply_text('''Hey, I am a Bot. I was created by Mr. SparX. He is my Owner. You can do these following things with me:
    			
1. /image category - Its used to get a Picture related to that Query.
2. /start - Its used to get this message.
3. /ping - Its used to check if Bot is Online or Offline.
4. /ispammer -m 10 -t 9999999999 - Its used to do SMS and Call Bombing on anyones Number but its for Indian Use only. Replace 10 with How many Number of Msgs you wanna bomb and Replace 9999999999 with the Mobile Number of Your Target.
5. /tbomb cc number msgs - It's used to do SMS Bombing Internationally and format is /tbomb 44 2657368944 150. Thanks to SpeedX for this.
6. /wikipedia query - Its used to Search anything on wikipedia.
''')
    	elif '/ping' in string:
    		if update.message.from_user['username'] == 'MrSp4rX':
    			update.message.reply_text('Pong Daddy!')
    		else:
    			update.message.reply_text('Pong!')
    	elif '/wikipedia' in string:
    		string = string.replace('/wikipedia','')
    		try:
    			result = wikipedia.summary(string, sentences=3)
    			update.message.reply_text(f'''According to Wikipedia: 
{result}''')
    		except:
    			update.message.reply_text(f'I can\'t find anything related to{string}.')
    	elif '/nmap' in string:
    		url = string.replace('/nmap','')
    		update.message.reply_text('Bot will not Respond for 10 to 15 second due to running Nmap command in Background...')
    		update.message.reply_text('Please wait...')
    		values = nmap(url)
    		update.message.reply_text('This Website is '+str(values[0]))
    		port = values[1]
    		result = ""
    		for item in port:
    			result = result+item + "\n"
    		update.message.reply_text('Open Ports are:\n'+result)
    		update.message.reply_text('Operating System is:\n'+values[3])
    		service = values[2]
    		services = ''
    		for serv in service:
    			if not serv in services:
    				services = services+serv+'\n'
    			else:
    				pass
    		update.message.reply_text('Running Services are: \n'+services)
    		
    		
    	
    	elif '/ispammer' in string:
    			string = string.replace('/ispammer', '')
    			string = string.replace('-t', '')
    			string = string.replace('-m','')
    			msgs,number = map(str, string.split())
    			if int(msgs)>500:
    				update.message.reply_text(choice(ispammer_reply))
    			elif int(msgs)<=500 and len(number) == 10:
    				update.message.reply_text('Bombing Started by iSpammer Successfully...')
    				Api.infinite(str(number), '',int(msgs))
    				update.message.reply_text(str(msgs)+ ' msgs Bombed Successfully!!!')
    			
    			else:
    				update.message.reply_text('Something Went Wrong!!! and Report this issue on https://github.com/MrSp4rX/TelegramBot/issues/new and you will get reply in 6 Hours maximum...')
    		
    	elif '/tbomb' in string:
    			string = string.replace('/tbomb','')
    			cc, number, msgs = map(str, string.split())
    			if cc == '91':
    				update.message.reply_text('Please use iSpammer for Indian Numbers and TBomb for International Numbers.')
    			elif int(msgs)>150:
    				update.message.reply_text(choice(ispammer_reply))
    			elif cc != '91':
    				update.message.reply_text('Bombing Started by TBomb Successfully...')
    				popen(f'nohup python3 bomb.py -c {cc} -t {number} -m {msgs} &')
    				update.message.reply_text(msgs+ ' msgs Bombed Successfully!!!')
    			else:
    				update.message.reply_text('Something Went Wrong!!! and Report this issue on https://github.com/MrSp4rX/TelegramBot/issues/new and you will get reply in 6 Hours maximum...')
    		
    		


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(environ['TOKEN_HERE'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__=="__main__":
	main()
