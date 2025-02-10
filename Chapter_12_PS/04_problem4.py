# Q4: Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a dividend: "))
    b = int(input("Enter a divisor: "))

    if b == 0:
        raise ZeroDivisionError("INFINITE!")
    else:
        print(f"Division of {a}/{b} is: {a/b:.2f}")
except ZeroDivisionError as e:
    print(e)