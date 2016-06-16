#!/usr/bin/python
# -*- coding: utf-8 -*-
import telegram, logging, random
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

_TOKEN = '183804544:AAF6bdGCb3q7e8sSAjPhn9SSh-FsfpAJ8OA'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token=_TOKEN)
updater = Updater(token=_TOKEN)
print(bot.getMe())

# Mensaje de bienvenida. Cuando inicias una conversacion con ValentitoBot
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text='Hola, soy tito y me gustan los gatos :)')

# Handler para el comando /start
start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)

def echo(bot, update):
	text = update.message.text.lower()
	user = update.message.from_user

	print user.first_name + ': ' + text
	
	if text.find('hola') >= 0:
		bot.sendMessage(chat_id=update.message.chat_id, text='Hola :)')
	if text.find('como estas') >= 0 or text.find('cómo estás') >= 0 or text.find('cómo estas') >= 0:
		bot.sendMessage(chat_id=update.message.chat_id, text='Bien y tu?')

	if text.find('linux') >= 0 or text.find('ubuntu') >= 0 or text.find('manjaro') >= 0 or text.find('unix') >= 0:
		n = random.randint(1,2)
		if n == 1:
			bot.sendMessage(chat_id=update.message.chat_id, text='Eso pasa por usar software penca')
		elif n == 2:
			bot.sendMessage(chat_id=update.message.chat_id, text='Probaste instalando Windows?')
	elif text.find('arvoleda') >= 0 or text.find('vegan') >= 0 or text.find('vegeta') >= 0:
		bot.sendMessage(chat_id=update.message.chat_id, text='Y donde está mi carne?!')
	elif user.username.lower() == 'ommirandap' and random.randint(1,16) == 8:
		bot.sendMessage(chat_id=update.message.chat_id, text='Ven? por eso el otro Omar era el buen Omar')
	elif user.username.lower() == 'thebestaround' and random.randint(1,16) == 8:
		bot.sendMessage(chat_id=update.message.chat_id, text='@thebestaround Te amo Boris <3')
	elif text.find('lucha') >= 0:
		bot.sendMessage(chat_id=update.message.chat_id, text='Yo quiero ser Diva')
	else:
		n = random.randint(1,30)
		if n == 10:
			bot.sendMessage(chat_id=update.message.chat_id, text='Sabías que los gatos anulan las malas vibras del WiFi?')
		elif n == 15:
			bot.sendMessage(chat_id=update.message.chat_id, text='Cuando va a estar Egreen para android 4.1.2?')
		elif n == 5:
			bot.sendMessage(chat_id=update.message.chat_id, text='@' + user.nickname + ' tienes mi sello de aprobación')
		elif n == 29:
			bot.sendMessage(chat_id=update.message.chat_id, text='Sabías que los gatos anulan las malas vibras del WiFi?')
		elif n == 13:
			bot.sendMessage(chat_id=update.message.chat_id, text='Y cuándo va a estar Egreen para android 4.1.2?')

# Esto filtra si el usuario envia un mensaje
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

# Esto empieza a hacer funcionar el Bot
updater.start_polling()

# Permite detener el bot usando ctrl+C 
updater.idle()
