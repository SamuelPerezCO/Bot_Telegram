from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start" , say_hello ))
application.add_handler(CommandHandler("echo" , echo))
application.run_polling(allowed_updates=Update.ALL_TYPES)
