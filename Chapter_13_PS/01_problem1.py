# Q1: Write a program to input name, marks and phone number of a student and format it using the format function like below:

# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter name: ")
marks = input("Enter marks: ")
number = input("Enter phone number: ")

string = "The name of the student is {}, his marks are {} and phone number is {}"

print(string.format(name, marks, number))