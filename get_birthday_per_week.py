#!/usr/bin/env python3

"""
get_birthdays_per_week виводить іменинників у форматі:

Monday: Bill, Jill
Friday: Kim, Jan

Користувачів, у яких день народження був на вихідних, потрібно привітати у понеділок.

Для відладки зручно створити тестовий список users та заповнити його самостійно.

Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.

Тиждень починається з понеділка.
"""

from datetime import datetime, timedelta

def on(when: str):
    return datetime.strptime(when, "%d.%m.%Y")

users = [
  { "name": "Bill, Jill", "birthday": on("19.03.1985")}
, { "name": "Rica, Costa", "birthday": on("20.03.2001")}
, { "name": "Aires, Buenos", "birthday": on("14.03.1991")}
, { "name": "Frankivsk, Ivano", "birthday": on("16.03.1977")}
, { "name": "Zaspa, Koncha", "birthday": on("13.12.2010")}
, { "name": "Podilskij, Kamianec", "birthday": on("13.12.2007")}
, { "name": "Puscha, Vodycia", "birthday": on("17.03.1997")}
, { "name": "Vegas, Las", "birthday": on("18.03.1998")}
, { "name": "Angeles, Los", "birthday": on("21.03.2000")}
, { "name": "Diego, San", "birthday": on("16.12.1989")}
, { "name": "Francisco, San", "birthday": on("11.12.2001")}
, { "name": "Menlo, Park", "birthday": on("29.12.1999")}
, { "name": "Lauderdale, Fort", "birthday": on("26.12.1999")}
, { "name": "Jose, San", "birthday": on("27.12.2003")}
, { "name": "Buayar, Fort", "birthday": on("28.12.2007")}
, { "name": "Berach, Long", "birthday": on("19.12.2000")}
, { "name": "Fe, Santa", "birthday": on("20.12.2001")}
, { "name": "Rose, Santa", "birthday": on("21.12.2002")}
, { "name": "El, Paso", "birthday": on("21.12.1979")}
, { "name": "Orleans, New", "birthday": on("28.12.1970")}
, { "name": "Rock, Little", "birthday": on("31.12.1973")}
, { "name": "Arbor, Ann", "birthday": on("29.12.1986")}
, { "name": "Haven, New", "birthday": on("03.12.1993")}
, { "name": "Bowling, Green", "birthday": on("15.12.2009")}
]

def get_birthday_per_week(users: list):

    today = datetime.today()
    # today = on("27.12.2023")

    date_shift = timedelta(0)

    today_over_week = today + timedelta(days=7)
    # If today_over_week ends on weekend day, the period must be shortened
    if today_over_week.weekday() == 6:
        # Over week day is Sunday: exclude Sunday and Saturday
        today_over_week -= timedelta(days=2)
    elif today_over_week.weekday() == 5:
        # Over week day is Saturday: exclude Saturday
        today_over_week -= timedelta(days=1)

    # Period must be in the same year. Otherwise shift dates on 2 weeks
    if today.year < today_over_week.year:
        # The years in both dates must be the same
        date_shift = timedelta(days=14)
        today -= date_shift
        today_over_week -= date_shift

    # Searching appropriate birthdays
    week_birthdays = []
    for user in users:
        bday = user["birthday"] - date_shift
        bday = bday.replace(year=today.year)
        if today <= bday < today_over_week:
            # If birthday is assigned to weekend - inform on Monday.
            # Period is not ends with weekends, so Monday exists
            # in period
            if bday.weekday() == 6:
                bday += timedelta(days=1) # Sunday -> Monday
            elif bday.weekday() == 5:
                bday += timedelta(days=2) # Saturday -> Monday
            user["dummy"] = bday # save this time to use below
            week_birthdays.append(user)

    # Sorting by epoch time
    week_birthdays.sort(key=lambda user: user["dummy"].timestamp())

    # Printing result
    for user in week_birthdays:
        print("{:>9}: {:s}".format(
                  user["dummy"].strftime("%A")
                , user["name"]))

get_birthday_per_week(users)
