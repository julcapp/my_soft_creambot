from datetime import datetime, time
from apscheduler.schedulers.background import BackgroundScheduler
from config.app import app
from config.config import chat_id
from modules.reminder.database.db import get_lessons
from modules.reminder.functions.helpers import LESSON_TIMES

scheduler = BackgroundScheduler()


def send_reminder(lesson_number, start_time, end_time):
    lessons = get_lessons()
    lesson_data = lessons.get(str(lesson_number))
    link = lesson_data.get("link", "") if lesson_data else ""

    text = f"<b>Напоминание</b>\n\n"
    text += f"Через 5 минут начинается пара #{lesson_number} ({start_time} — {end_time})"
    if link:
        text += f"\n\nСсылка на пару: {link}"

    app.send_message(chat_id=chat_id, text=text)


def add_scheduled_tasks():
    for lesson_number, (start_str, end_str) in enumerate(LESSON_TIMES, 1):
        start_parts = start_str.split(":")
        hour, minute = int(start_parts[0]), int(start_parts[1])

        reminder_minute = minute - 5
        reminder_hour = hour
        if reminder_minute < 0:
            reminder_minute += 60
            reminder_hour -= 1

        if reminder_hour < 0:
            continue

        scheduler.add_job(
            send_reminder,
            "cron",
            day_of_week="mon-fri",
            hour=reminder_hour,
            minute=reminder_minute,
            args=[lesson_number, start_str, end_str],
            id=f"reminder_{lesson_number}",
            replace_existing=True,
        )
