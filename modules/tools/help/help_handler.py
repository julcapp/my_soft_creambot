from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.app import app


tools_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("ping", callback_data="ping")],
    [InlineKeyboardButton("chat_id", callback_data="chat_id"),
     InlineKeyboardButton("user_id", callback_data="user_id")],
    [InlineKeyboardButton("Main", callback_data="main")],
])

help_texts = {
    "tools": (
        "<b>Tools — Инструменты</b>\n\n"
        "Дополнительные утилиты бота."
    ),
    "ping": "<b>/ping</b> — проверить работу бота",
    "chat_id": "<b>/chat_id</b> — получить ID текущего чата",
    "user_id": "<b>/user_id</b> — показать ID пользователя (или в ответ на сообщение)",
}


def answer_tools(client, callback_query):
    data = callback_query.data
    text = help_texts.get(data, help_texts["tools"])
    app.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
        text=text,
        reply_markup=tools_keyboard,
    )
