from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Queue", callback_data="queue"),
         InlineKeyboardButton("Timetable", callback_data="timetable")],
        [InlineKeyboardButton("Database", callback_data="db"),
         InlineKeyboardButton("Tools", callback_data="tools")],
    ])


async def answer_main(query):
    keyboard = build_main_keyboard()
    await query.edit_message_text(
        text='<b>Помощь</b>\n\nНажимай на кнопки внизу, чтобы получить информацию.',
        reply_markup=keyboard,
    )
