a = int(input("How far does the snail travel during the day? (In feet) "))
b = int(input("How far does the snail fall during the night? (In feet) "))
h = int(input("How far does the snail need to travel? (In feet) "))
total = 0
day = 0
night = 0

while total < h:
    total += a
    day += 1
    if total < h:
        total -= b
        night += 1
    else:
        break

if day != 1:
    if night != 1:
        print("The snail will need " + str(day) + " days and " + str(night) + " nights to travel " + str(h) + " feet.")
    else:
        print("The snail will need " + str(day) + " days and " + str(night) + " night to travel " + str(h) + " feet.")
else:
    print("The snail will need " + str(day) + " day and " + str(night) + " nights to travel " + str(h) + " feet.")