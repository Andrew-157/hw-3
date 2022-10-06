from datetime import date, datetime


def get_birthdays_per_week(users):
    week_days = {"Monday": [], "Tuesday": [],
                 "Wednesday": [], "Thursday": [], "Friday": []}

    for info in users:
        if info["birthday"].day not in range(datetime.now().day, datetime.now().day + 7):
            continue
        if info["birthday"].isoweekday() <= 5:
            week_days[info["birthday"].strftime("%A")].append(info["name"])
        else:
            week_days["Monday"].append(info["name"])

    for key, value in week_days.items():
        if value:
            print(f"{key}: {', '.join(value)}")


users = [{"name": "Jill", "birthday": datetime(2022, 10, 7)},
         {"name": "Karen", "birthday": datetime(2022, 10, 11)},
         {"name": "Simon", "birthday": datetime(2022, 10, 12)},
         {"name": "Luis", "birthday": datetime(2022, 10, 9)},
         {"name": "Grew", "birthday": datetime(2022, 10, 10)},
         {"name": "James", "birthday": datetime(2022, 10, 29)},
         {"name": "Lu", "birthday": datetime(2022, 10, 3)},
         {"name": "Lisa", "birthday": datetime(2022, 10, 8)},
         {"name": "Ronald", "birthday": datetime(2022, 10, 30)},
         {"name": "Kerry", "birthday": datetime(2022, 10, 23)}]


get_birthdays_per_week(users)
