#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os
from api import Api
import scrap
from random import choice
from os import environ
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Defining Abuse Words
abuse = ['bhosadike','madarchod','bsdk', 'bhsdk', 'betichod', 'chod', 'lund', 'gand ', 'jerk', 'lode', 'loda', 'madarchod', 'mdrchod', 'madar', 'chut', 'bc', 'mkchut', 'mc','mkc','jhat','suwar','kutte','randi','bhosadi','m4drch0d','m4d4rch0d','mdrch0d','b#05adik3','bh05adik3','bh0sadike','bh0sad!ke','bho5adike','bh0sadike','bh0sad!ke','ch0d','m4d4rch0d','land','m@d@rc#0d','m@d@rch0d','m@d@rchod','l4nd','.bhosadike','.madarchod','.bsdk', '.bhsdk', '.betichod', '.chod', '.gand ', '.jerk', '.lode', '.loda', '.madarchod', '.mdrchod', '.madar', '.chut', '.bc', '.mkchut', '.mc','.mkc', '.jhat','.suwar','.kutte','.randi','.bhosadi','.m4drch0d','.m4d4rch0d','.mdrch0d','.b#05adik3','.bh05adik3','.bh0sadike','.bh0sad!ke','.bho5adike','.bh0sadike','.bh0sad!ke','.ch0d','.m4d4rch0d','.land','.m@d@rc#0d','.m@d@rch0d','.m@d@rchod','.l4nd','bhosadike.','madarchod.','bsdk.', 'bhsdk.', 'betichod.', 'chod.', 'gand ', 'jerk.', 'lode.', 'loda.', 'madarchod.', 'mdrchod.', 'madar.', 'chut.', 'bc.', 'mkchut.', 'mc.','mkc.','lund','jhat.','suwar.','kutte.','randi.','bhosadi.','m4drch0d.','m4d4rch0d.','mdrch0d.','b#05adik3.','bh05adik3.','bh0sadike.','bh0sad!ke.','bho5adike.','bh0sadike.','bh0sad!ke.','ch0d.','m4d4rch0d.','land.','m@d@rc#0d.','m@d@rch0d.','m@d@rchod.','l4nd.']

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
'''def start(update, context):
    Send a message when the command /start is issued.
    update.message.reply_text('Hi!')'''

def echo(update, context):
    """Echo the user message."""
    string = update.message.text
    for word in abuse:
    	if word in string.lower() and update.message.from_user['username'] != 'MrSp4rX':
    		update.message.reply_text( choice(abuse_reply))
    	
    if string.startswith('/'):
    	if '/image' in string:
    		string = string.replace('/image', '')
    		update.message.reply_text(scrap.main(string))
    		
    	elif '/help' in string:
    		update.message.reply_text('''Hey, I am a Bot. I was created by Mr. SparX. He is my Owner. You can do these following things with me:''')
    	elif '/ping' in string:
    		if update.message.from_user['username'] == 'MrSp4rX':
    			update.message.reply_text('Pong Daddy!')
    		else:
    			update.message.reply_text('Pong!')
    	
    	elif '/ispammer' in string:
    			string = string.replace('/ispammer', '')
    			string = string.replace('-t', '')
    			string = string.replace('-m','')
    			msgs,number = map(str, string.split())
    			if int(msgs)>500:
    				update.message.reply_text('You cannot send messages More than 500 at a Time!!!')
    			elif int(msgs)<=500 and len(number) == 10:
    				update.message.reply_text('Bombing Started Successfully...')
    				Api.infinite(str(number), '',msgs)
    				update.message.reply_text(str(msgs)+ ' Bombed Successfully!!!')
    			
    			else:
    				update.message.reply_text('Something Went Wrong!!! and Report this issue on https://github.com/MrSp4rX/TelegramBot/issues/new and you will get reply in 6 Hours maximum...')
    		
    		


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(environ['TOKEN_HERE'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))

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


if __name__ == '__main__':
    main()
