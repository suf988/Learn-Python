# Q3: Attempt problem 1 using while loop.

# problem 1: Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number to get multiplication table: "))
i = 1

while(i<=10):
    print(f"{num} x  {i} = {num*i}")
    i +=1