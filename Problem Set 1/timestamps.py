hour1 = int(input("What hour did it start? "))
minute1 = int(input("What minute in the hour did it start? "))
second1 = int(input("What second in the minute did it start? "))
hour2 = int(input("What hour did it end? "))
minute2 = int(input("What minute in the hour did it end? "))
second2 = int(input("What second in the minute did it end? "))
timestamp1 = (3600 * hour1) + (60 * minute1) + second1
timestamp2 = (3600 * hour2) + (60 * minute2) + second2

print("There were " + str(timestamp2 - timestamp1) + " second(s) during it.")