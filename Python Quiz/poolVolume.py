import math

name = input("What is your name? ")
pool = input("What shape is your pool, " + name + "? (Use RP for rectangular prism, C for cube, or CY for a cylindrical pool) ")

if pool == "RP":
    length = float(input("What is the length of the pool in feet? "))
    width = float(input("What is the width of the pool in feet? "))
    depth = float(input("What is the depth of the pool in feet? "))
    volume = length * depth * width * 7.5
    print("The volume of your pool, " + name + ", is " + str(volume) + " gallons.")
elif pool == "C":
    length = float(input("What is the side length of the pool? "))
    volume = (length ** 3) * 7.5
    print("The volume of your pool, " + name + ", is " + str(volume) + " gallons.")
elif pool == "CY":
    radius = float(input("What is the radius of the pool? "))
    depth = float(input("What is the depth of the pool in feet? "))
    volume = (((((math.pi * (radius ** 2)) * depth * 7.5) * 100) // 1) / 100)
    print("The volume of your pool, " + name + ", is ~" + str(volume) + " gallons.")
else:
    print(name + ", you didn't give me a valid pool shape.")