def addition (a,b):
    t=a+b
    print(t)
    
def subtraction(a,b):
    s=a-b
    print(s)

def multiplication(a,b):
    m=a*b
    print(m)

def division(a,b):
    d=a/b
    print(d)

def floordivision(a,b):
    f=a//b
    print(f)

def modulus(a,b):
    k=a%b
    print(k)

def exponent(a,b):
    e=a**b
    print(e)

print(" 1.Addition\n 2.Subtraction \n 3.Multiplication\n 4.Division \n 5.Floordivision\n 6.Modulus\n 7.Exponent")

choice= int(input("enter your choice:"))

if choice==1:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    addition(a,b)

elif choice==2:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    subtraction(a,b)

elif choice==3:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    multiplication(a,b)

elif choice==4:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    division(a,b)

elif choice==5:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    floordivision(a,b)

elif choice==6:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    modulus(a,b)

else:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    exponent(a,b)