from telegram import InlineKeyboardMarkup, InlineKeyboardButton


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


async def answer_timetable(query):
    data = query.data
    text = help_texts.get(data, help_texts["timetable"])
    await query.edit_message_text(text=text, reply_markup=timetable_keyboard)
