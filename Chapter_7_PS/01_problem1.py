# Q1: Write a program to print multiplication table of a given number using for loop.

n = int(input("Write a number to get multiplication table: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")