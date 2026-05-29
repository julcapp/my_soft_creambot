from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.app import app


timetable_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("Week", callback_data="timetable_week"),
     InlineKeyboardButton("Next Week", callback_data="timetable_nextweek")],
    [InlineKeyboardButton("Today", callback_data="timetable_today"),
     InlineKeyboardButton("Tomorrow", callback_data="timetable_tomorrow")],
    [InlineKeyboardButton("Main", callback_data="main")],
])

help_texts = {
    "timetable": (
        "<b>Timetable — Расписание</b>\n\n"
        "Модуль для просмотра расписания с schedule.kpi.ua."
    ),
    "timetable_week": "<b>/week</b> — расписание на текущую неделю",
    "timetable_nextweek": "<b>/nextweek</b> — расписание на следующую неделю",
    "timetable_today": "<b>/today</b> — расписание на сегодня",
    "timetable_tomorrow": "<b>/tomorrow</b> — расписание на завтра",
}


def answer_timetable(client, callback_query):
    data = callback_query.data
    text = help_texts.get(data, help_texts["timetable"])
    app.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.id,
        text=text,
        reply_markup=timetable_keyboard,
    )
