# Q4: Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

numbers = [4, 15, 23, 20, 150, 54, 17, 89, 100, 65]

maximum = reduce(lambda x,y: x if x>y else y, numbers)

print(maximum)