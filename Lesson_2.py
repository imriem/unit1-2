def problem1():
    a = int(input())%10

def problem2():
    a = int(input())
    print((a%100 - a%10)/10)

def problem3():
    a = int(input())
    print(str(a//100 + ((a%100)//10) + a%10))
    
def problem4():
    a = float(input())
    print(str(a%1))
    
def problem5():
    a = float(input())
    print(str((a%1)*100 //10))

def problem6():
    import math
    n = float(input())
    m = float(input())
    print(str(math.ceil(m/n)))

def problem7():
    n = int(input())
    print(str((n//60)),str(n%60))

def problem8():
    a = int(input())
    b = int(input())
    n = int(input())
    a = a*n + (b*n)//100
    b = (b*n)%100
    print(a, b)

def problem9():
    h = int(input())
    m = int(input())
    s = int(input())
    print(str(30*h+.5*m+s*.5*(1/60)))

def problem10():
    a = float(input())
    print(str((a%30)*12))
    
