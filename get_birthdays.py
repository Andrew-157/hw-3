from datetime import datetime


def get_birthdays_per_week(users):

    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []

    for i in users:

        if i["birthday"].day not in range(datetime.now().day, datetime.now().day + 7):
            continue

        else:

            if i["birthday"].weekday() == 0:
                monday.append(i["name"])

            elif i["birthday"].weekday() == 1:
                tuesday.append(i["name"])

            elif i["birthday"].weekday() == 2:
                wednesday.append(i["name"])

            elif i["birthday"].weekday() == 3:
                thursday.append(i["name"])

            elif i["birthday"].weekday() == 4:
                friday.append(i["name"])

            else:
                monday.append(i["name"])

    if len(monday) > 1:
        a = ", ".join(monday[:-1])
        print("Monday: " + a + ", " + monday[-1])
    elif len(monday) == 1:
        a = "".join(monday[0])
        print("Monday: " + a)

    if len(tuesday) > 1:
        a = ", ".join(tuesday[:-1])
        print("Tuesday: " + a + ", " + tuesday[-1])
    elif len(tuesday) == 1:
        a = "".join(tuesday[0])
        print("Tuesday: " + a)

    if len(wednesday) > 1:
        a = ", ".join(wednesday[:-1])
        print("Wednesday: " + a + ", " + wednesday[-1])
    elif len(wednesday) == 1:
        a = "".join(wednesday[0])
        print("Wednesday: " + a)

    if len(thursday) > 1:
        a = ", ".join(thursday[:-1])
        print("Thursday: " + a + ", " + thursday[-1])
    elif len(thursday) == 1:
        a = "".join(thursday[0])
        print("Thursday: " + a)

    if len(friday) > 1:
        a = ", ".join(friday[:-1])
        print("Friday: " + a + ", " + friday[-1])
    elif len(friday) == 1:
        a = "".join(friday[0])
        print("Friday: " + a)


users = [{"name": "Jill", "birthday": datetime(2022, 10, 7)},
         {"name": "Karen", "birthday": datetime(2022, 10, 11)},
         {"name": "Simon", "birthday": datetime(2022, 10, 12)},
         {"name": "Luis", "birthday": datetime(2022, 10, 9)},
         {"name": "Grew", "birthday": datetime(2022, 10, 10)},
         {"name": "James", "birthday": datetime(2022, 10, 13)},
         {"name": "Lu", "birthday": datetime(2022, 10, 3)},
         {"name": "Lisa", "birthday": datetime(2022, 10, 8)},
         {"name": "Ronald", "birthday": datetime(2022, 10, 6)},
         {"name": "Kerry", "birthday": datetime(2022, 10, 23)}]


get_birthdays_per_week(users)
