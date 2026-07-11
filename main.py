from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes , MessageHandler , filters , ConversationHandler
from dotenv import load_dotenv
from telegram import Update
import os

from Controllers.TodoController import TodoController

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler( CommandHandler("add" , TodoController.add_todo ) )
application.add_handler( CommandHandler("list" , TodoController.list_todo ) )
application.add_handler( CommandHandler("start" , TodoController.say_hello ) )
application.add_handler( CommandHandler("check" , TodoController.check_todo ) )
application.add_handler( CommandHandler("clear" , TodoController.clear_todos ) )

info_conversation_handler = ConversationHandler(
    entry_points=[ CommandHandler("data" , TodoController.ask_name)],
    states={
        TodoController.GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.get_name)],
        TodoController.GET_LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND , TodoController.get_last_name)]
    },
    fallbacks=[ CommandHandler("cancel" , TodoController.cancel_conversation)]
)

application.add_handler(info_conversation_handler)

application.add_handler( MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.send_message))

application.run_polling(allowed_updates=Update.ALL_TYPES)