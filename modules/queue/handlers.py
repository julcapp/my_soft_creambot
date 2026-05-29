from telegram import Update
from telegram.ext import ContextTypes
from config.config import chat_id, admin_user_id

queues = {}


def get_queue_text_html(name):
    if name not in queues:
        return None
    lines = [f"<b>Очередь: {name}</b>"]
    entries = queues[name]
    if not entries:
        return f"<b>{name}</b> - очередь пуста"
    for i, uid in enumerate(entries, 1):
        lines.append(f"{i}. <code>{uid}</code>")
    return "\n".join(lines)


async def create_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if not args:
        await update.message.reply_text("Использование: /create <название очереди>")
        return
    name = " ".join(args)
    if name in queues:
        await update.message.reply_text(f"Очередь <b>{name}</b> уже существует")
        return
    queues[name] = []
    await update.message.reply_text(f"Очередь <b>{name}</b> создана")


async def delete_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if not args:
        await update.message.reply_text("Использование: /delete <название очереди>")
        return
    name = " ".join(args)
    if name not in queues:
        await update.message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = update.effective_user.id
    if user_id != admin_user_id and queues[name]:
        if queues[name][0] != user_id:
            await update.message.reply_text("Вы не можете удалить эту очередь")
            return
    del queues[name]
    await update.message.reply_text(f"Очередь <b>{name}</b> удалена")


async def join_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if not args:
        await update.message.reply_text("Использование: /join <название очереди>")
        return
    name = " ".join(args)
    if name not in queues:
        await update.message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = update.effective_user.id
    if user_id in queues[name]:
        await update.message.reply_text("Вы уже в этой очереди")
        return
    queues[name].append(user_id)
    text = get_queue_text_html(name)
    await update.message.reply_text(f"Вы записались в очередь <b>{name}</b>\n\n{text}")


async def leave_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if not args:
        await update.message.reply_text("Использование: /leave <название очереди>")
        return
    name = " ".join(args)
    if name not in queues:
        await update.message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = update.effective_user.id
    if user_id not in queues[name]:
        await update.message.reply_text("Вас нет в этой очереди")
        return
    queues[name].remove(user_id)
    text = get_queue_text_html(name)
    await update.message.reply_text(f"Вы вышли из очереди <b>{name}</b>\n\n{text}")


async def check_queues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    if not queues:
        await update.message.reply_text("Очередей нет")
        return
    lines = ["<b>Все очереди:</b>"]
    for name, users in queues.items():
        lines.append(f"\n<b>{name}</b> — {len(users)} чел.")
    await update.message.reply_text("\n".join(lines))


async def pass_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Использование: /pass <количество> <название очереди>")
        return
    try:
        count = int(args[0])
    except ValueError:
        await update.message.reply_text("Количество должно быть числом")
        return
    name = " ".join(args[1:])
    if name not in queues or not queues[name]:
        await update.message.reply_text(f"Очередь <b>{name}</b> пуста или не существует")
        return
    user_id = update.effective_user.id
    if queues[name][0] != user_id and user_id != admin_user_id:
        await update.message.reply_text("Вы не первый в очереди")
        return
    removed = queues[name][:count]
    queues[name] = queues[name][count:]
    lines = [f"Пропущено {len(removed)} чел. из очереди <b>{name}</b>"]
    for u in removed:
        lines.append(f"— <code>{u}</code>")
    text = get_queue_text_html(name)
    if text:
        lines.append(f"\n{text}")
    await update.message.reply_text("\n".join(lines))


async def reset_queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != chat_id:
        return
    args = context.args
    if not args:
        await update.message.reply_text("Использование: /reset <название очереди>")
        return
    name = " ".join(args)
    if name not in queues:
        await update.message.reply_text(f"Очереди <b>{name}</b> не существует")
        return
    user_id = update.effective_user.id
    if queues[name][0] != user_id and user_id != admin_user_id:
        await update.message.reply_text("Вы не можете сбросить эту очередь")
        return
    queues[name] = []
    await update.message.reply_text(f"Очередь <b>{name}</b> сброшена")
