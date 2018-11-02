import math

a = float(input("Pick a number. "))

print("The digit in the tenths place is " + str(int(math.floor((a % 1) * 10))) + ".")