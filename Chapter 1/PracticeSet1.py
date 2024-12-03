# Q1: Write a program to print Twinkle twinkle little star poem in python

print('''Twinkle Twinkle Little Star
      How I wonder what you are
      Up above the world so high
      Like a diamond in the sky''')

# --------------------------------------------------------------------------------

# Q2: Use REPL and print the table of 5 using it. 

print("5 * 1 = ", 5*1)
print("5 * 2 = ", 5*2)
print("5 * 3 = ", 5*3)
print("5 * 4 = ", 5*4)
print("5 * 5 = ", 5*5)
print("5 * 6 = ", 5*6)
print("5 * 7 = ", 5*7)
print("5 * 8 = ", 5*8)
print("5 * 9 = ", 5*9)
print("5 * 10 = ", 5*10)

# --------------------------------------------------------------------------------

# Q3: Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.
 
import os

directory_path = '/' #file directory you want to check

contents = os.listdir(directory_path)

for items in contents:
    print(items)

