from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

from Controllers.TodoController import TodoController

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.args)
    await update.message.reply_text( context.args[0])
    
application.add_handler(CommandHandler("start" , say_hello ))
application.add_handler(CommandHandler("search" , search ))

application.run_polling(allowed_updates=Update.ALL_TYPES)
