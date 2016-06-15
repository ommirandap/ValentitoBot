import telegram, logging
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

_TOKEN = '183804544:AAF6bdGCb3q7e8sSAjPhn9SSh-FsfpAJ8OA'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token=_TOKEN)
updater = Updater(token=_TOKEN)
print(bot.getMe())

# Mensaje de bienvenida. Cuando inicias una conversacion con ValentitoBot
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text='Hola, soy tito y amo windows!')
# Handler para el comando /start
start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)

def echo(bot, update):
        if (update.message.text).find('linux') > 0:
                bot.sendMessage(chat_id=update.message.chat_id, text='Eso pasa por usar software penca')
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
# Esto fiitra si el usuario envia un mensaje
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

# Esto empieza a hacer funcionar el Bot
updater.start_polling()

