# Q4: Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n==1:
        return 1
    return n + sum(n-1)

n = int(input("Enter a number: "))
print(f"Sum of the numbers is: {sum(n)}")