import requests
from datetime import date, timedelta
from config.config import group_name

API_URL = "https://schedule.kpi.ua/api/schedule/lectures?groupName={}"


def get_group_id():
    try:
        r = requests.get(f"https://schedule.kpi.ua/api/schedule/lectures?groupName={group_name}", timeout=10)
        data = r.json()
        return data.get("group_id")
    except Exception:
        return None


def fetch_schedule(week_offset=0):
    try:
        group_id = get_group_id()
        if not group_id:
            return "Не удалось получить расписание"

        today = date.today()
        monday = today - timedelta(days=today.weekday())
        target_monday = monday + timedelta(weeks=week_offset)
        week_num = target_monday.isocalendar()[1]

        r = requests.get(
            f"https://schedule.kpi.ua/api/schedule/lectures?groupId={group_id}",
            timeout=10,
        )
        data = r.json()
        schedule = data.get("schedule", {})

        days_map = {
            0: "Понедельник", 1: "Вторник", 2: "Среда",
            3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье",
        }

        result = []
        for day_num, day_name in days_map.items():
            day_date = target_monday + timedelta(days=day_num)
            day_schedule = schedule.get(str(day_num), [])
            lessons = [l for l in day_schedule if week_num in l.get("weeks", [])]

            if not lessons:
                continue

            result.append(f"\n<b>{day_name} ({day_date.strftime('%d.%m')})</b>")
            for lesson in lessons:
                time = lesson.get("time", "")
                name = lesson.get("name", "")
                teacher = lesson.get("teacher", "")
                room = lesson.get("room", "")
                result.append(f"  {time} — {name}")
                if teacher:
                    result.append(f"    Преподаватель: {teacher}")
                if room:
                    result.append(f"    Аудитория: {room}")

        if not result:
            return "Расписание на этот период отсутствует"

        return "\n".join(result)
    except Exception as e:
        return f"Ошибка получения расписания: {e}"


def get_week_schedule():
    return fetch_schedule(0)


def get_next_week_schedule():
    return fetch_schedule(1)


def get_today_schedule():
    try:
        group_id = get_group_id()
        if not group_id:
            return "Не удалось получить расписание"

        today = date.today()
        week_num = today.isocalendar()[1]
        day_num = today.weekday()

        r = requests.get(
            f"https://schedule.kpi.ua/api/schedule/lectures?groupId={group_id}",
            timeout=10,
        )
        data = r.json()
        schedule = data.get("schedule", {})

        day_schedule = schedule.get(str(day_num), [])
        lessons = [l for l in day_schedule if week_num in l.get("weeks", [])]

        if not lessons:
            return "Сегодня пар нет"

        result = [f"<b>Расписание на сегодня ({today.strftime('%d.%m')})</b>"]
        for lesson in lessons:
            time = lesson.get("time", "")
            name = lesson.get("name", "")
            teacher = lesson.get("teacher", "")
            room = lesson.get("room", "")
            result.append(f"\n{time} — {name}")
            if teacher:
                result.append(f"  Преподаватель: {teacher}")
            if room:
                result.append(f"  Аудитория: {room}")

        return "\n".join(result)
    except Exception as e:
        return f"Ошибка получения расписания: {e}"


def get_tomorrow_schedule():
    tomorrow = date.today() + timedelta(days=1)
    try:
        group_id = get_group_id()
        if not group_id:
            return "Не удалось получить расписание"

        week_num = tomorrow.isocalendar()[1]
        day_num = tomorrow.weekday()

        r = requests.get(
            f"https://schedule.kpi.ua/api/schedule/lectures?groupId={group_id}",
            timeout=10,
        )
        data = r.json()
        schedule = data.get("schedule", {})

        day_schedule = schedule.get(str(day_num), [])
        lessons = [l for l in day_schedule if week_num in l.get("weeks", [])]

        if not lessons:
            return "Завтра пар нет"

        result = [f"<b>Расписание на завтра ({tomorrow.strftime('%d.%m')})</b>"]
        for lesson in lessons:
            time = lesson.get("time", "")
            name = lesson.get("name", "")
            teacher = lesson.get("teacher", "")
            room = lesson.get("room", "")
            result.append(f"\n{time} — {name}")
            if teacher:
                result.append(f"  Преподаватель: {teacher}")
            if room:
                result.append(f"  Аудитория: {room}")

        return "\n".join(result)
    except Exception as e:
        return f"Ошибка получения расписания: {e}"
