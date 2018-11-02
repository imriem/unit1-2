a = float(input("How many hours have passed? "))
b = float(input("How many more minutes have passed? "))
c = float(input("How many more seconds have passed? "))

print("The hour hand has turned " + str(float(float(a * 30) + float(b * 0.5) + float(c * 0.0083333333333333))) + " degrees.")