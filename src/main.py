from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from telegram import Update
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN)