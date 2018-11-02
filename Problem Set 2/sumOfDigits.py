a = str(input("Pick a number. "))
sum = 0

for n in range(0, len(a)):
    sum = sum + ((int(a) // (10 ** n)) % 10)

print("The sum of all digits is " + str(sum) + ".")