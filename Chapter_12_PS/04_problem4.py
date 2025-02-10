# Q4: Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a dividend: "))
    b = int(input("Enter a divisor: "))

    print(f"Division of {a}/{b} is: {a/b:.2f}")
except ZeroDivisionError:
    print("INFINITE!")