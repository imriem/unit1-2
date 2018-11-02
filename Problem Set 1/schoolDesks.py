a = int(input("How many students are in the first class? "))
b = int(input("How many students are in the second class? "))
c = int(input("How many students are in the third class? "))

print("There need to be " + str(((a // 2) + (a % 2)) + ((b // 2) + (b % 2)) + ((c // 2) + (c % 2))) + " desks.")