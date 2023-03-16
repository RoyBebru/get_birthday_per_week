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

from datetime import date, timedelta

users = [
  { "name": "Bill, Jill", "birthday": date(1985,3,19)}
, { "name": "Wesly, Jone", "birthday": date(2004,2,29)}
, { "name": "Kristi, Agata", "birthday": date(2004,3,1)}
, { "name": "White, Barbara", "birthday": date(2001,3,2)}
, { "name": "Aires, Buenos", "birthday": date(1991,3,14)}
, { "name": "Frankivsk, Ivano", "birthday": date(1977,3,16)}
, { "name": "Zaspa, Koncha", "birthday": date(2010,12,13)}
, { "name": "Podilskij, Kamianec", "birthday": date(2007,12,13)}
, { "name": "Puscha, Vodycia", "birthday": date(1997,3,17)}
, { "name": "Vegas, Las", "birthday": date(1998,3,18)}
, { "name": "Angeles, Los", "birthday": date(2000,3,21)}
, { "name": "Diego, San", "birthday": date(1989,12,16)}
, { "name": "Francisco, San", "birthday": date(2001,12,11)}
, { "name": "Menlo, Park", "birthday": date(1999,12,29)}
, { "name": "Lauderdale, Fort", "birthday": date(1999,12,26)}
, { "name": "Jose, San", "birthday": date(2003,12,27)}
, { "name": "Buayar, Fort", "birthday": date(2007,12,28)}
, { "name": "Berach, Long", "birthday": date(2000,12,19)}
, { "name": "Fe, Santa", "birthday": date(2001,12,20)}
, { "name": "Rose, Santa", "birthday": date(2002,12,21)}
, { "name": "El, Paso", "birthday": date(1979,12,21)}
, { "name": "Orleans, New", "birthday": date(1970,12,28)}
, { "name": "Rock, Little", "birthday": date(1973,12,31)}
, { "name": "Arbor, Ann", "birthday": date(1986,12,29)}
, { "name": "Haven, New", "birthday": date(1986,12,29)}
, { "name": "Bowling, Green", "birthday": date(2009,12,15)}
]

def get_birthday_per_week(users: list):

    today = date.today()
    # today = date(2023,2,28)

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

        try:
            bday = bday.replace(year=today.year)
        except ValueError:
            # Maybe shifted birthday on February, 29 -> March, 1
            bday += timedelta(days=1)
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
    week_birthdays.sort(key=lambda user: user["dummy"].toordinal())

    # Printing result
    for user in week_birthdays:
        print("{:>9}: {:s}".format(
                  user["dummy"].strftime("%A")
                , user["name"]))

get_birthday_per_week(users)
