from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.app import app


queue_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("create", callback_data="create"),
     InlineKeyboardButton("delete", callback_data="delete")],
    [InlineKeyboardButton("join", callback_data="join"),
     InlineKeyboardButton("leave", callback_data="leave")],
    [InlineKeyboardButton("check", callback_data="check"),
     InlineKeyboardButton("pass", callback_data="pass")],
    [InlineKeyboardButton("reset", callback_data="reset")],
    [InlineKeyboardButton("Main", callback_data="main")],
])

help_texts = {
    "queue": (
        "<b>Queue — Очереди</b>\n\n"
        "Модуль для создания и управления очередями."
    ),
    "create": "<b>/create &lt;название&gt;</b> — создать новую очередь",
    "delete": "<b>/delete &lt;название&gt;</b> — удалить очередь",
    "join": "<b>/join &lt;название&gt;</b> — записаться в очередь",
    "leave": "<b>/leave &lt;название&gt;</b> — выйти из очереди",
    "check": "<b>/check</b> — проверить все очереди",
    "pass": "<b>/pass &lt;количество&gt; &lt;название&gt;</b> — пропустить людей",
    "reset": "<b>/reset &lt;название&gt;</b> — сбросить очередь",
}


def answer_queue(client, callback_query):
    data = callback_query.data
    text = help_texts.get(data, help_texts["queue"])
    app.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
        text=text,
        reply_markup=queue_keyboard,
    )
