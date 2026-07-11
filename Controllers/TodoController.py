from telegram import Update
from telegram.ext import ContextTypes , ConversationHandler

from Models.Todo import Todo
from Models.TodoList import todo_list

class TodoController:

    GET_NAME , GET_LAST_NAME = range(2)

    @staticmethod
    async def add_todo(update: Update , context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        todo_list.append( Todo(title) )
        await update.message.reply_text("Nota agregada!")

    @staticmethod
    async def list_todo(update: Update , context: ContextTypes.DEFAULT_TYPE):
        if (len(todo_list) == 0):
            await update.message.reply_text("No hay tareas todavia")
            return
        answer = ""
        for i , todo in enumerate(todo_list):
            answer = answer + f"{i + 1} - {'O' if todo.is_completed else 'X'} {todo.title} \n"
        await update.message.reply_text(answer)

    @staticmethod
    async def check_todo(update: Update , context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if(index > len(todo_list) or index <= 0):
            await update.message.reply_text("ERROR: that task doesnt exist")
            return
        todo_list[index - 1].set_completed()
        await update.message.reply_text(f"The task {index} has been completed")
        await TodoController.list_todo(update , context)

    @staticmethod
    async def clear_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        todo_list.clear()
        await update.message.reply_text("Clear")

    @staticmethod
    async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Conversation Iniatiated")

    @staticmethod
    async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("You write a message")

    @staticmethod
    async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Tell me your name: ")
        return TodoController.GET_NAME

    @staticmethod
    async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["name"] = update.message.text
        await update.message.reply_text("Tell me your last name: ")
        return TodoController.GET_LAST_NAME

    @staticmethod
    async def get_last_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["last_name"] = update.message.text
        await update.message.reply_text(f"Thank your data is name: {context.user_data['name']} \nAnd your last name is: {context.user_data['last_name']}")
        return ConversationHandler.END
    
    @staticmethod
    async def cancel_conversation(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Operacion Cancelada")
        return ConversationHandler.END