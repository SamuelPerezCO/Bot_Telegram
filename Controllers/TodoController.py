from telegram import Update
from telegram.ext import ContextTypes

class TodoController:

    @staticmethod
    def add_todo(update: Update , context: ContextTypes.DEFAULT_TYPE):
        text_splitted = update.message.text.split()
        command = update.message.text.split()[0]
        print()