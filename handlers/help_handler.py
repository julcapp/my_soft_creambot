from telegram import Update
from telegram.ext import ContextTypes
from config.config import chat_id
from handlers.help.main_page_help_handler import build_main_keyboard


async def help_main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if chat_id and update.effective_chat.id != chat_id:
        return
    keyboard = build_main_keyboard()
    await update.message.reply_text(
        text='<b>Помощь</b>\n\nНажимай на кнопки внизу, чтобы получить информацию.',
        reply_markup=keyboard,
    )
