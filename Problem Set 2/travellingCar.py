import math

a = float(input("How far can the car travel in a day? "))
b = float(input("How far does the car need to travel? "))

print("The car will need at least " + str(int(math.ceil(b / a))) + " days.")