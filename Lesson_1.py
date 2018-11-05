def problem1():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a+b+c)

def problem2():
    a = input()
    print("Hi", a)


def problem3():
    a = float(input())
    print(a*a)

def problem4():
    b = int(input())
    h = int(input())
    print((b*h*.5))


def problem5():
    name = input()
    print('Hello, ' + name + "!")


def problem6():
    n = int(input())
    k = int(input())
    print(k // n)
    print(k % n)


def problem7():
    a = int(input())
    print("The next number for the number " + str(a) +  " is " + str(a+1) + ".")
    print("The previous number for the number " + str(a) + " is " + str(a-1) + ".")

def problem8():
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())
    h2 = int(input())
    m2 = int(input())
    s2 = int(input())
    print(str(3600 * (h2 - h1) + 60 * (m2 - m1) + (s2 - s1)))


def problem9():
    a = int(input())
    b = int(input())
    c = int(input())
    if(a%2 == 1):
        a+=1

    if(b%2 == 1):
        b+=1

    if(c%2 == 1):
        c+=1

    print(str((a+b+c)/2))

