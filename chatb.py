import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your own bot token from BotFather
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update: Update, context: CallbackContext):
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text('Welcome to the chatbot!')

def echo(update: Update, context: CallbackContext):
    """Echo the user's message."""
    update.message.reply_text(update.message.text)

def error(update: Update, context: CallbackContext):
    """Log any errors."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Run the bot."""
    updater = Updater(TOKEN)

    # Register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()