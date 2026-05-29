from pyrogram import filters
from config.app import app
from config.config import chat_id, bot_username


@app.on_message(filters.group & filters.command(["ping", f"ping@{bot_username}"]) & filters.chat([chat_id]))
def ping(client, message):
    message.reply_text("Pong!")


@app.on_message(filters.group & filters.command(["chat_id", f"chat_id@{bot_username}"]) & filters.chat([chat_id]))
def get_chat_id(client, message):
    message.reply_text(f"Chat ID: <code>{message.chat.id}</code>")


@app.on_message(filters.group & filters.command(["user_id", f"user_id@{bot_username}"]) & filters.chat([chat_id]))
def get_user_id(client, message):
    if message.reply_to_message:
        target = message.reply_to_message.from_user
        message.reply_text(
            f"Пользователь: {target.first_name}\nID: <code>{target.id}</code>"
        )
    else:
        message.reply_text(
            f"Ваш ID: <code>{message.from_user.id}</code>"
        )
