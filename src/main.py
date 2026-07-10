from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")
    
application.add_handler(CommandHandler("start" , say_hello ))

application.run_polling(allowed_updates=Update.ALL_TYPES)
