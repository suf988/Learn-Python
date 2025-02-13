# Q3:  Write a program to filter a list of numbers which are divisible by 5.

numbers = [4, 15, 23, 20, 150, 54, 17, 89, 100, 65]
filtered = list(filter(lambda x: x % 5 == 0, numbers))

print(filtered)