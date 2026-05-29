from telegram import Update
from telegram.ext import ContextTypes
from config.config import chat_id, admin_user_id
from modules.reminder.database.db import get_lessons, set_lesson, reset_db


async def setup_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if update.effective_user.id != admin_user_id:
        await update.message.reply_text("Только админ может настраивать БД")
        return
    await update.message.reply_text("База данных готова к работе")


async def show_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if update.effective_user.id != admin_user_id:
        await update.message.reply_text("Только админ может просматривать БД")
        return
    lessons = get_lessons()
    if not lessons:
        await update.message.reply_text("База данных пуста")
        return
    lines = ["<b>Содержимое базы данных:</b>"]
    for lesson_id, data in lessons.items():
        link = data.get("link", "—")
        lines.append(f"\nID: {lesson_id}")
        lines.append(f"Ссылка: {link}")
    await update.message.reply_text("\n".join(lines))


async def reset_database(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if update.effective_user.id != admin_user_id:
        await update.message.reply_text("Только админ может очищать БД")
        return
    reset_db()
    await update.message.reply_text("База данных очищена")


async def edit_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if update.effective_user.id != admin_user_id:
        await update.message.reply_text("Только админ может изменять ссылки")
        return
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Использование: /editlink <ID пары> <ссылка>")
        return
    lesson_id = args[0]
    link = " ".join(args[1:])
    set_lesson(lesson_id, link)
    await update.message.reply_text(f"Ссылка для пары #{lesson_id} обновлена")


async def get_ids(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if update.effective_user.id != admin_user_id:
        await update.message.reply_text("Только админ может просматривать ID")
        return
    lessons = get_lessons()
    if not lessons:
        await update.message.reply_text("Нет сохраненных пар")
        return
    ids = [f"ID: {lid}" for lid in lessons]
    await update.message.reply_text("ID всех пар:\n" + "\n".join(ids))
