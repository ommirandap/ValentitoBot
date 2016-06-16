#!/usr/bin/python
# -*- coding: utf-8 -*-
import telegram, logging, random, codecs
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
	respuesta = ''

	with open('valentitobot.log','a') as f:
		f.write(user.first_name.encode('utf-8') + ': ' + text.encode('utf-8') + '\n')
	
	if text.find('hola') >= 0:
		respuesta = 'Hola :)'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	if text.find('como estas') >= 0:
		respuesta = 'Bien y tu?'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)

	if text.find('linux') >= 0 or text.find('ubuntu') >= 0 or text.find('manjaro') >= 0 or text.find('unix') >= 0:
		n = random.randint(1,2)
		if n == 1:
			respuesta = 'Eso pasa por usar software penca'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
		elif n == 2:
			respuesta = 'Probaste instalando Windows?'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	elif text.find('windows') >= 0 or text.find('microsoft') >= 0:
		respuesta = 'Recuerda que Microsoft me auspicia <3'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	elif text.find('arvoleda') >= 0 or text.find('vegan') >= 0 or text.find('vegeta') >= 0:
		respuesta = 'Y donde está mi carne?!'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	elif user.username.lower() == 'ommirandap' and random.randint(1,11) == 4:
		respuesta = 'Ven? por eso el otro Omar era el buen Omar'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	elif user.username.lower() == 'thebestaround' and random.randint(1,11) == 6:
		respuesta = '@thebestaround Te amo Boris <3'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	elif text.find('lucha') >= 0:
		respuesta = 'Yo quiero ser Diva'
		bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
	else:
		n = random.randint(1,15)
		if n == 10:
			respuesta = 'Sabías que los gatos anulan las malas vibras del WiFi?'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
		elif n == 15:
			respuesta = 'Cuando va a estar Egreen para android 4.1.2?'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
		elif n == 5:
			respuesta = 'Tienes mi sello de aprobación'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)
		elif n == 13:
			respuesta = 'Y cuándo va a estar Egreen para android 4.1.2?'
			bot.sendMessage(chat_id=update.message.chat_id, text=respuesta)

	with open('valentitobot.log','a') as f:
                f.write('Respuesta ValentitoBot: ' + respuesta.encode('utf-8') + '\n\n')

# Esto filtra si el usuario envia un mensaje
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

# Esto empieza a hacer funcionar el Bot
updater.start_polling()

# Permite detener el bot usando ctrl+C 
updater.idle()
