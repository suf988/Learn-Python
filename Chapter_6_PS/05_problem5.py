# Q5: Write a program which finds out whether a given name is present in a list or not.

name_list = ["harry", "hermione", "jane", "ron", "draco", "longbottom"]

name = input("Enter your name: ").lower()

if(name in name_list):
    print("Your name is present in the list.")
else:
    print("Sorry, your name is not present.")