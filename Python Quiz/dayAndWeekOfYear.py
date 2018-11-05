number = int(input("Pick a number from 1-365. "))
week = ((number + 4) // 7) + 1
day = (number + 3) % 7
ending = ''

if day % 10 == 1 and day != 11:
    ending = 'st'
elif day % 10 == 2 and day != 12:
    ending = 'nd'
elif day % 10 == 3 and day != 13:
    ending = 'rd'
else:
    ending = 'th'

if week % 10 == 1 and week != 11:
    print("That day on the year 2019 was during the " + str(week) + "st week of the year and " + str(day) + ending + " day of the week.")
elif week % 10 == 2 and week != 12:
    print("That day on the year 2019 was during the " + str(week) + "nd week of the year and " + str(day) + ending + " day of the week.")
elif week % 10 == 3 and week != 13:
    print("That day on the year 2019 was during the " + str(week) + "rd week of the year and " + str(day) + ending + " day of the week.")
else:
    print("That day on the year 2019 was during the " + str(week) + "th week of the year and " + str(day) + ending + " day of the week.")