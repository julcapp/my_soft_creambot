from pyrogram import filters
from config.app import app
from config.config import chat_id, bot_username
from modules.timetable.functions.schedule_fetcher import (
    get_week_schedule,
    get_next_week_schedule,
    get_today_schedule,
    get_tomorrow_schedule,
)


@app.on_message(filters.group & filters.command(["week", f"week@{bot_username}"]) & filters.chat([chat_id]))
def week_schedule(client, message):
    text = get_week_schedule()
    message.reply_text(text)


@app.on_message(filters.group & filters.command(["nextweek", f"nextweek@{bot_username}"]) & filters.chat([chat_id]))
def nextweek_schedule(client, message):
    text = get_next_week_schedule()
    message.reply_text(text)


@app.on_message(filters.group & filters.command(["today", f"today@{bot_username}"]) & filters.chat([chat_id]))
def today_schedule(client, message):
    text = get_today_schedule()
    message.reply_text(text)


@app.on_message(filters.group & filters.command(["tomorrow", f"tomorrow@{bot_username}"]) & filters.chat([chat_id]))
def tomorrow_schedule(client, message):
    text = get_tomorrow_schedule()
    message.reply_text(text)
