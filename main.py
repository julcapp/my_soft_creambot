import asyncio
from telegram.ext import CommandHandler, CallbackQueryHandler
from config.app import application
from handlers.help_handler import help_main
from handlers.keyboard_handler import keyboard_handler
from modules.queue.handlers import (
    create_queue, delete_queue, join_queue, leave_queue,
    check_queues, pass_queue, reset_queue,
)
from modules.timetable.handlers import (
    week_schedule, nextweek_schedule, today_schedule, tomorrow_schedule,
)
from modules.reminder.handlers import (
    setup_database, show_database, reset_database, edit_link, get_ids,
)
from modules.tools.handlers import ping, get_chat_id, get_user_id
from modules.reminder.lessons_parser import add_scheduled_tasks, scheduler


def main():
    application.add_handler(CommandHandler("start", help_main))
    application.add_handler(CommandHandler("help", help_main))
    application.add_handler(CommandHandler("create", create_queue))
    application.add_handler(CommandHandler("delete", delete_queue))
    application.add_handler(CommandHandler("join", join_queue))
    application.add_handler(CommandHandler("leave", leave_queue))
    application.add_handler(CommandHandler("check", check_queues))
    application.add_handler(CommandHandler("pass", pass_queue))
    application.add_handler(CommandHandler("reset", reset_queue))
    application.add_handler(CommandHandler("week", week_schedule))
    application.add_handler(CommandHandler("nextweek", nextweek_schedule))
    application.add_handler(CommandHandler("today", today_schedule))
    application.add_handler(CommandHandler("tomorrow", tomorrow_schedule))
    application.add_handler(CommandHandler("setup_db", setup_database))
    application.add_handler(CommandHandler("show_db", show_database))
    application.add_handler(CommandHandler("reset_db", reset_database))
    application.add_handler(CommandHandler("editlink", edit_link))
    application.add_handler(CommandHandler("ids", get_ids))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("chat_id", get_chat_id))
    application.add_handler(CommandHandler("user_id", get_user_id))
    application.add_handler(CallbackQueryHandler(keyboard_handler))

    add_scheduled_tasks(application)
    scheduler.start()

    application.run_polling()


if __name__ == "__main__":
    main()
