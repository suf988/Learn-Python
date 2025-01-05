# Q4: Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter username: ")

if(len(name)<10):
    print("Username saved!")
else:
    print("Error! Username must be less than 10 characters.")