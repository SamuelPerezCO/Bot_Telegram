from telegram.ext import ContextTypes , ConversationHandler , CommandHandler , MessageHandler , filters
from telegram import Update

USERNAME, INFO, PHOTO = range(3)

class UserProfileController:
    
    @staticmethod
    async def start_getting_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Sign Up , Write your username: ")
        return USERNAME
    
    @staticmethod
    async def get_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["username"] = update.message.text
        await update.message.reply_text("Perfect , Write your info")
        return INFO
    
    @staticmethod
    async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["user_info"] = update.message.text
        await update.message.reply_text("Thank you! , can you send the profile picture?")
        return PHOTO
    
    @staticmethod
    async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["user_photo"] = update.message.text
        
        return ConversationHandler.END
    
    @staticmethod
    async def cancel_operation(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Operation Cancelled")
        return ConversationHandler.END
    
user_profile_controller_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("profile" , UserProfileController.start_getting_info)],
    states={
        USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND , UserProfileController.get_username)],
        INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND , UserProfileController.get_info)],
        PHOTO: [MessageHandler(filters.TEXT & ~filters.COMMAND , UserProfileController.get_photo)]
    },
    fallbacks=[MessageHandler(filters.COMMAND , UserProfileController.cancel_operation)]
)