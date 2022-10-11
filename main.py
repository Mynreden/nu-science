import logging
from typing import List, Any
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telethon import TelegramClient, sync, events

api_id = 17820169
api_hash = '256014d33cf1a1f7d749050478df24c3'
client = TelegramClient('nu_science', api_id=api_id, api_hash=api_hash)
input_array = ['@asdcxzasdcxza', "@mynreden"]

def log_info():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )
# 1.1  opinion 1.2 fact
# 2.1 opinion 2.2 fact
# 3.1 fact 3.2 opinion
# 4.1 fact 4.2 opinion
# 5.1 fact 5.2 opinion


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    list1 = update.message.text.split()
    if "add" == list1[0] :
        input_array.append(list1[1])

@client.on(events.NewMessage(chats=input_array))
async def normal_handler(event):

    await client.send_message('@nu_science', event.message)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("1596944937:AAHDpnFZmLolunh_a11b5THEOrQAFZDbcys").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    client.start()
    client.run_until_disconnected()
    application.run_polling()



if __name__ == "__main__":
    log_info()
    main()
