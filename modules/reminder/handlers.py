from pyrogram import filters
from config.app import app
from config.config import chat_id, bot_username, admin_user_id
from modules.reminder.database.db import get_lessons, set_lesson, reset_db


@app.on_message(filters.group & filters.command(["setup_db", f"setup_db@{bot_username}"]) & filters.chat([chat_id]))
def setup_database(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("Только админ может настраивать БД")
        return
    message.reply_text("База данных готова к работе")


@app.on_message(filters.group & filters.command(["show_db", f"show_db@{bot_username}"]) & filters.chat([chat_id]))
def show_database(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("Только админ может просматривать БД")
        return
    lessons = get_lessons()
    if not lessons:
        message.reply_text("База данных пуста")
        return
    lines = ["<b>Содержимое базы данных:</b>"]
    for lesson_id, data in lessons.items():
        link = data.get("link", "—")
        lines.append(f"\nID: {lesson_id}")
        lines.append(f"Ссылка: {link}")
    message.reply_text("\n".join(lines))


@app.on_message(filters.group & filters.command(["reset_db", f"reset_db@{bot_username}"]) & filters.chat([chat_id]))
def reset_database(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("Только админ может очищать БД")
        return
    reset_db()
    message.reply_text("База данных очищена")


@app.on_message(filters.group & filters.command(["editlink", f"editlink@{bot_username}"]) & filters.chat([chat_id]))
def edit_link(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("Только админ может изменять ссылки")
        return
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        message.reply_text("Использование: /editlink <ID пары> <ссылка>")
        return
    lesson_id = args[1]
    link = args[2]
    set_lesson(lesson_id, link)
    message.reply_text(f"Ссылка для пары #{lesson_id} обновлена")


@app.on_message(filters.group & filters.command(["ids", f"ids@{bot_username}"]) & filters.chat([chat_id]))
def get_ids(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("Только админ может просматривать ID")
        return
    lessons = get_lessons()
    if not lessons:
        message.reply_text("Нет сохраненных пар")
        return
    ids = [f"ID: {lid}" for lid in lessons]
    message.reply_text("ID всех пар:\n" + "\n".join(ids))
