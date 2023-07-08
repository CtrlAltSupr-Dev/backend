from copy import copy


DEFAULT_SCHEDULE = {}
for day in "lmwjvs":
    for mod in "12345678":
        DEFAULT_SCHEDULE[day + mod] = "'FREE'"


def process_schedule(text_sc):
    data = text_sc.split("\nROW: ")[1:]
    schedule = copy(DEFAULT_SCHEDULE)
    for row in data:
        row = row.split("<>")[:2]
        horario = row[0].split(":")
        days = horario[0].split("-")
        modules = horario[1].split(",")
        for day in days:
            for mod in modules:
                if len(day) and len(mod):
                    schedule[day.lower() + mod] = "'" + row[1] + "'"

    full_sc_query = schedule

    schedule_info = {"total": 0}
    for type in ["AYU", "CLAS", "LAB", "PRA", "SUP", "TAL", "TER", "TES"]:
        schedule_info[type] = list(schedule.values()).count("'" + type + "'")
        schedule_info["total"] += schedule_info[type]
        schedule_info[type] = str(schedule_info[type])
    schedule_info["total"] = str(schedule_info["total"])

    info_sc_query = schedule_info

    return [full_sc_query, info_sc_query]