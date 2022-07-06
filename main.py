import logging
from get_tweet import main
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Updater
import os

BOTAPIKEY = os.getenv('BOTAPIKEY')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def checker(context: ContextTypes):
    msg, tweet_time = main()
    # logging.info(context)
    job=context.job.context
    if msg is not None:
        context.bot.send_message(chat_id=job, text=msg)
    else:
        context.bot.send_message(chat_id=job, text="Aw :(")


def start(update: Update, context: ContextTypes):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Welcome here UJUNGS or casual fans! This is a bot to notify you all about the latest UZZU videos or out of the blue VLIVE shows")
    updater.job_queue.run_repeating(checker, interval=60, first=10, context=chat_id)

if __name__ == '__main__':
    updater = Updater(token=BOTAPIKEY, use_context= True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)
    
    PORT = int(os.environ.get('PORT', '443'))
    HOOK_URL = 'YOUR-CODECAPSULES-URL-HERE' + '/' + BOTAPIKEY
    updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=BOTAPIKEY, webhook_url=HOOK_URL)
    updater.idle()

    updater.idle()
    logging.info('bot started')
