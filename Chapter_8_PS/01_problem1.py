# Q1: Write a program using functions to find greatest of three numbers.

def compare():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a>b and a>c:
        print(f"Greatest number is {a}")
    elif b>a and b>c:
        print(f"Greatest number is {b}")
    else:
        print(f"Greatest number is {c}")

compare()