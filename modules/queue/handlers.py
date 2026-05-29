from pyrogram import filters
from config.app import app
from config.config import chat_id, bot_username, admin_user_id

queues = {}


def save_queues():
    pass


def load_queues():
    pass


def get_queue_text(name):
    if name not in queues:
        return None
    lines = [f"<b>Очередь: {name}</b>"]
    for i, user_id in enumerate(queues[name], 1):
        lines.append(f"{i}. <code>{user_id}</code>")
    return "\n".join(lines) if len(lines) > 1 else f"<b>{name}</b> - очередь пуста"


@app.on_message(filters.group & filters.command(["create", f"create@{bot_username}"]) & filters.chat([chat_id]))
def create_queue(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        message.reply_text("Использование: /create <название очереди>")
        return
    name = args[1]
    if name in queues:
        message.reply_text(f"Очередь <b>{name}</b> уже существует")
        return
    queues[name] = []
    message.reply_text(f"Очередь <b>{name}</b> создана")


@app.on_message(filters.group & filters.command(["delete", f"delete@{bot_username}"]) & filters.chat([chat_id]))
def delete_queue(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        message.reply_text("Использование: /delete <название очереди>")
        return
    name = args[1]
    if name not in queues:
        message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = message.from_user.id
    if user_id != admin_user_id and queues[name]:
        first = queues[name][0]
        if user_id != first:
            message.reply_text("Вы не можете удалить эту очередь")
            return
    del queues[name]
    message.reply_text(f"Очередь <b>{name}</b> удалена")


@app.on_message(filters.group & filters.command(["join", f"join@{bot_username}"]) & filters.chat([chat_id]))
def join_queue(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        message.reply_text("Использование: /join <название очереди>")
        return
    name = args[1]
    if name not in queues:
        message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = message.from_user.id
    if user_id in queues[name]:
        message.reply_text("Вы уже в этой очереди")
        return
    queues[name].append(user_id)
    text = get_queue_text(name)
    message.reply_text(f"Вы записались в очередь <b>{name}</b>\n\n{text}")


@app.on_message(filters.group & filters.command(["leave", f"leave@{bot_username}"]) & filters.chat([chat_id]))
def leave_queue(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        message.reply_text("Использование: /leave <название очереди>")
        return
    name = args[1]
    if name not in queues:
        message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = message.from_user.id
    if user_id not in queues[name]:
        message.reply_text("Вас нет в этой очереди")
        return
    queues[name].remove(user_id)
    text = get_queue_text(name)
    message.reply_text(f"Вы вышли из очереди <b>{name}</b>\n\n{text}")


@app.on_message(filters.group & filters.command(["check", f"check@{bot_username}"]) & filters.chat([chat_id]))
def check_queues(client, message):
    if not queues:
        message.reply_text("Очередей нет")
        return
    lines = ["<b>Все очереди:</b>"]
    for name, users in queues.items():
        lines.append(f"\n<b>{name}</b> — {len(users)} чел.")
    message.reply_text("\n".join(lines))


@app.on_message(filters.group & filters.command(["pass", f"pass@{bot_username}"]) & filters.chat([chat_id]))
def pass_queue(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        message.reply_text("Использование: /pass <количество> <название очереди>")
        return
    try:
        count = int(args[1])
    except ValueError:
        message.reply_text("Количество должно быть числом")
        return
    name = args[2]
    if name not in queues or not queues[name]:
        message.reply_text(f"Очередь <b>{name}</b> пуста или не существует")
        return
    user_id = message.from_user.id
    if queues[name][0] != user_id and user_id != admin_user_id:
        message.reply_text("Вы не первый в очереди")
        return
    removed = queues[name][:count]
    queues[name] = queues[name][count:]
    lines = [f"Пропущено {len(removed)} чел. из очереди <b>{name}</b>"]
    for u in removed:
        lines.append(f"— <code>{u}</code>")
    text = get_queue_text(name)
    if text:
        lines.append(f"\n{text}")
    message.reply_text("\n".join(lines))


@app.on_message(filters.group & filters.command(["reset", f"reset@{bot_username}"]) & filters.chat([chat_id]))
def reset_queue(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        message.reply_text("Использование: /reset <название очереди>")
        return
    name = args[1]
    if name not in queues:
        message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = message.from_user.id
    if queues[name][0] != user_id and user_id != admin_user_id:
        message.reply_text("Вы не можете сбросить эту очередь")
        return
    queues[name] = []
    message.reply_text(f"Очередь <b>{name}</b> сброшена")
