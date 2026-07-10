from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

from Controllers.TodoController import TodoController

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler( CommandHandler("add" , TodoController.add_todo ) )
application.add_handler( CommandHandler("list" , TodoController.list_todo ) )
application.add_handler( CommandHandler("check" , TodoController.check_todo ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)