from telegram import Update
from telegram.ext import ContextTypes
from config.config import chat_id


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    await update.message.reply_text("Pong!")


async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Chat ID: <code>{update.effective_chat.id}</code>")


async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        target = update.message.reply_to_message.from_user
        await update.message.reply_text(
            f"Пользователь: {target.first_name}\nID: <code>{target.id}</code>"
        )
    else:
        await update.message.reply_text(
            f"Ваш ID: <code>{update.effective_user.id}</code>"
        )
