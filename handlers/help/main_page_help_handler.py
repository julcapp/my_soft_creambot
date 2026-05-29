from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.app import app
from config.config import chat_id


def build_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Queue", callback_data="queue"),
         InlineKeyboardButton("Timetable", callback_data="timetable")],
        [InlineKeyboardButton("Database", callback_data="db"),
         InlineKeyboardButton("Tools", callback_data="tools")],
    ])


def answer_main(callback_query):
    keyboard = build_main_keyboard()
    app.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
        text='<b>Помощь</b>\n\nНажимай на кнопки внизу, чтобы получить информацию.',
        reply_markup=keyboard,
    )
