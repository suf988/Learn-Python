# Q2: Write a program to input eight numbers from the user and display all the unique numbers (once).

numbers = set()

addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)
addNum = int(input("Enter a number: "))
numbers.add(addNum)

print(f"Set with unique values: {numbers}")