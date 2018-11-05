name1 = input("What is the first person's name? ")
gpa1 = float(input("What is the first person's GPA? "))
name2 = input("What is the second person's name? ")
gpa2 = float(input("What is the second person's GPA? "))
name3 = input("What is the third person's name? ")
gpa3 = float(input("What is the third person's GPA? "))
name4 = input("What is the fourth person's name? ")
gpa4 = float(input("What is the fourth person's GPA? "))
averageGPA = (gpa1 + gpa2 + gpa3 + gpa4) / 4

print("The average GPA of " + name1 + ", " + name2 + ", " + name3 + ", and " + name4 + " is " + str(averageGPA) + ".")