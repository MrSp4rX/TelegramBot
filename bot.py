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

abuse = ['lavda','bhosadike','madarchod','bsdk', 'bhsdk', 'chod',  'lund', 'gand ', 'jerk', 'lode', 'loda', 'madar', 'chut', 'bc', 'mkchut', 'mc','mkc','jhat','suwar','kutte','randi','bhosadi','ch0d','m4d4rch0d','mdrch0d','b#05adik3','bh05adik3','bh0sadike','bh0sad!ke','bho5adike','bh0sadike','bh0sad!ke','ch0d','m4d4rch0d','land','m@d@rc#0d','m@d@rch0d','m@d@rchod','l4nd','.bhosadike','.madarchod','.bsdk', '.bhsdk', '.betichod', '.chod', '.gand ', '.jerk', '.lode', '.loda', '.madarchod', '.mdrchod', '.madar', '.chut', '.bc', '.mkchut', '.mc','.mkc', '.jhat','.suwar','.kutte','.randi','.bhosadi','.m4drch0d','.m4d4rch0d','.mdrch0d','.b#05adik3','.bh05adik3','.bh0sadike','.bh0sad!ke','.bho5adike','.bh0sadike','.bh0sad!ke','.ch0d','.m4d4rch0d','.land','.m@d@rc#0d','.m@d@rch0d','.m@d@rchod','.l4nd','bhosadike.','madarchod.','bsdk.', 'bhsdk.', 'betichod.', 'chod.', 'gand ', 'jerk.', 'lode.', 'loda.', 'madarchod.', 'mdrchod.', 'madar.', 'chut.', 'bc.', 'mkchut.', 'mc.','mkc.','lund','jhat.','suwar.','kutte.','randi.','bhosadi.','m4drch0d.','m4d4rch0d.','mdrch0d.','b#05adik3.','bh05adik3.','bh0sadike.','bh0sad!ke.','bho5adike.','bh0sadike.','bh0sad!ke.','ch0d.','m4d4rch0d.','land.','m@d@rc#0d.','m@d@rch0d.','m@d@rchod.','l4nd.']

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
	'Your Dady can only Abuse Samjha  Bhosadike',
    'Jada Shanpatti nahi warna, Shahtoot ki Patli dandi maar maar ke Chutad pr Rockstart likh dunga',
    'Yahi Patak ke chod denge, ab nikal madarchod'
]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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
                update.message.reply_text('Pong Bappu!')

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

        elif '/ispammer' in string:
            update.message.reply_text('This Command is Temporarily Banned by the Creator. @MrSp4rX')

        elif '/tbomb' in string:
                update.message.reply_text('This Command is Temporarily Banned by the Creator. @MrSp4rX')
            
    else:
        update.message.reply_text('I didn\'t get you')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(environ['token'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__=="__main__":
    main()
