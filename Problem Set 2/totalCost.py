import math

a = float(input("How many dollars does the item cost? Round down. "))
b = float(input("How many cents more does the item cost? ")) / 100
c = float(input("How many items do you want to buy? "))

print("The total cost is $" + str(int((a + b) * c)) + "." + str(int((((a + b) * c) % 1) * 100)) + ".")