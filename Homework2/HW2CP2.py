# Alvin Nguyen 2055636
from datetime import datetime
from datetime import date

timeFormat = "%B %d, %Y"

# list of month names

month_list = ['January', 'February', 'March',

              'April', 'May', 'June', 'July',

              'August', 'September', 'October',

              'November', 'December']

# begin loop
while True:
    # get user input

    dateUser = input()

    # if input is -1, break the loop

    if dateUser == "-1":
        break

    try:

        # checking if timeFormat matches the dateUser

        res = bool(datetime.strptime(dateUser, timeFormat))

    except ValueError:

        res = False

    # if dateUser matches with dateFormat

    if res:

        for i in range(0, 12):

            # find the month

            if dateUser.find(month_list[i]) != -1:

                # find the index of comma from dateUser

                commaIndex = dateUser.find(",")

                # fetching month, day, and year

                m = i + 1

                d = int(dateUser[commaIndex - 2:commaIndex].strip())

                y = int(dateUser[-4:])

                # form the a date with month, day, year

                newDate = date(y, m, d)

                # getting today

                today = date.today()

                if newDate <= today:
                    newDateFormat = str(m) + "/" + str(d) + "/" + str(y)

                    # printing date in new format

                    print(newDateFormat)

