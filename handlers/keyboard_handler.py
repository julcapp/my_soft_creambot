from telegram import Update
from telegram.ext import ContextTypes
from handlers.help.main_page_help_handler import answer_main
from modules.queue.help.help_handler import answer_queue
from modules.reminder.help.help_handler import answer_db
from modules.timetable.help.help_handler import answer_timetable
from modules.tools.help.help_handler import answer_tools


async def keyboard_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    main_callbacks = ['main']
    queue_callbacks = ['queue', 'create', 'delete', 'join', 'leave', 'check', 'pass', 'reset']
    db_callbacks = ['db', 'setup_db', 'show_db', 'reset_db', 'editlink', 'ids']
    timetable_callbacks = ['timetable', 'timetable_week', 'timetable_nextweek', 'timetable_today', 'timetable_tomorrow']
    tools_callbacks = ['tools', 'ping', 'chat_id', 'user_id']

    if query.data in main_callbacks:
        await answer_main(query)
    elif query.data in queue_callbacks:
        await answer_queue(query)
    elif query.data in db_callbacks:
        await answer_db(query)
    elif query.data in timetable_callbacks:
        await answer_timetable(query)
    elif query.data in tools_callbacks:
        await answer_tools(query)
