from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.app import app


db_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("setup_db", callback_data="setup_db"),
     InlineKeyboardButton("show_db", callback_data="show_db")],
    [InlineKeyboardButton("reset_db", callback_data="reset_db"),
     InlineKeyboardButton("editlink", callback_data="editlink")],
    [InlineKeyboardButton("ids", callback_data="ids")],
    [InlineKeyboardButton("Main", callback_data="main")],
])

help_texts = {
    "db": (
        "<b>Database — База данных</b>\n\n"
        "Модуль для управления локальной базой данных пар и ссылок."
    ),
    "setup_db": "<b>/setup_db</b> — настроить базу данных",
    "show_db": "<b>/show_db</b> — показать содержимое базы данных",
    "reset_db": "<b>/reset_db</b> — очистить базу данных",
    "editlink": "<b>/editlink &lt;ID&gt; &lt;ссылка&gt;</b> — изменить ссылку на пару",
    "ids": "<b>/ids</b> — получить ID всех пар",
}


def answer_db(client, callback_query):
    data = callback_query.data
    text = help_texts.get(data, help_texts["db"])
    app.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
        text=text,
        reply_markup=db_keyboard,
    )
