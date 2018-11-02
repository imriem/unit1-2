n = int(input("How many students are there? "))
k = int(input("How many apples are there? "))

print("Each student gets " + str(k // n) + " apples.")
print("There are " + str(k % n) + " apple(s) left.")