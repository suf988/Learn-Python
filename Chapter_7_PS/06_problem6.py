# Q6: Write a program to calculate the factorial of a given number using for loop.

# factorial of 5 = 5 x 4 x 3 x 2 x 1

num = int(input("Enter a number: "))
fac = 1

for i in range(1,num+1):
    fac*=i

print(f"Factorial of the number {num} is {fac}")
