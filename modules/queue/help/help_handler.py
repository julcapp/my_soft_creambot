from telegram import InlineKeyboardMarkup, InlineKeyboardButton


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


async def answer_queue(query):
    data = query.data
    text = help_texts.get(data, help_texts["queue"])
    await query.edit_message_text(text=text, reply_markup=queue_keyboard)
