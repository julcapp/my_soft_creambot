from telegram import InlineKeyboardMarkup, InlineKeyboardButton


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


async def answer_tools(query):
    data = query.data
    text = help_texts.get(data, help_texts["tools"])
    await query.edit_message_text(text=text, reply_markup=tools_keyboard)
