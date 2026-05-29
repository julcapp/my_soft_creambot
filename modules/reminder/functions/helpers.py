from datetime import datetime, timedelta


LESSON_TIMES = [
    ("08:30", "10:00"),
    ("10:15", "11:45"),
    ("12:00", "13:30"),
    ("13:45", "15:15"),
    ("15:30", "17:00"),
    ("17:05", "18:35"),
    ("18:40", "20:10"),
    ("20:15", "21:45"),
]


def get_lesson_time(lesson_number):
    if 1 <= lesson_number <= len(LESSON_TIMES):
        return LESSON_TIMES[lesson_number - 1]
    return None


def get_current_lesson_number():
    now = datetime.now()
    for i, (start, end) in enumerate(LESSON_TIMES, 1):
        start_time = datetime.strptime(start, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        end_time = datetime.strptime(end, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        if start_time <= now <= end_time:
            return i
    return None


def get_next_lesson_number():
    now = datetime.now()
    current = get_current_lesson_number()
    if current:
        return current + 1
    for i, (start, _) in enumerate(LESSON_TIMES, 1):
        start_time = datetime.strptime(start, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        if now < start_time:
            return i
    return None


def get_reminder_time(lesson_number, minutes_before=5):
    times = get_lesson_time(lesson_number)
    if not times:
        return None
    start = datetime.strptime(times[0], "%H:%M")
    reminder = start - timedelta(minutes=minutes_before)
    return reminder.strftime("%H:%M")
