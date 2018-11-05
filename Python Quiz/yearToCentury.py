year = int(input("Pick a year. "))
century = ((year - 1) // 100) + 1

if century % 10 == 1 and century != 11:
    print("That year lies in the " + str(century) + "st century.")
elif century % 10 == 2 and century != 12:
    print("That year lies in the " + str(century) + "nd century.")
elif century % 10 == 3 and century != 13:
    print("That year lies in the " + str(century) + "rd century.")
else:
    print("That year lies in the " + str(century) + "th century.")