from telegram import Update
from telegram.ext import ContextTypes
from config.config import chat_id
from modules.timetable.functions.schedule_fetcher import (
    get_week_schedule,
    get_next_week_schedule,
    get_today_schedule,
    get_tomorrow_schedule,
)


async def week_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    text = get_week_schedule()
    await update.message.reply_text(text)


async def nextweek_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    text = get_next_week_schedule()
    await update.message.reply_text(text)


async def today_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    text = get_today_schedule()
    await update.message.reply_text(text)


async def tomorrow_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    text = get_tomorrow_schedule()
    await update.message.reply_text(text)
