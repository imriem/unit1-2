a = float(input("How many degrees has the hour hand turned passed midnight? "))

print("The minute hand has turned " + str(int(((a % 30) / 30) * 360)) + " degrees.")