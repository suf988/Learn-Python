# Q2: Write a program to print third, fifth and seventh element from a list using enumerate function.

fruits = ['apple', 'banana', 'grapes', 'mango', 'blueberry', 'orange', 'strawberry', 'pear', 'pineapple']

for index, item in enumerate(fruits, start=1):
    if index == 3 or index == 5 or index == 7:
        print(f"Item number{index}: {item}")
