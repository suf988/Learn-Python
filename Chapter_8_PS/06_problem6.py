# Q6: Write a python function which converts inches to cms.

def conversion(n):
    convert = n * 2.54
    return convert

inp = float(input("Enter value in inches: "))
print(f"{inp} inches are equal to {conversion(inp):.2f} cms.")