# Q3: Write a list comprehension to print a list which contains the multiplication table of a user entered number.

number = int(input("Enter a number: "))

table = [number*i for i in range(1,11)]
print(table)
