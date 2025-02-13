# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  LIST COMPREHENSION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# list comprehension is a concise and elegant way to create a list based on an existing list from a single line of code.

# SYNTAX:   new_list = ['expression' for 'item' in 'iterable' if 'condition']

# expression              →  The value to be added to the new list
# item                    →  The variable representing each element in the iterable
# iterable                →  A collection (like a list, tuple, range, etc.)
# if condition (optional) →  Filters elements before adding them to the list


''' WITHOUT LIST COMPREHENSION '''

list = [3, 5, 7, 9, 4]
squared_list = []

for i in list:
    squared_list.append(i**2)

print(f"Original list: {list}")
print(f"Squared list: {squared_list}")

''' WITH LIST COMPREHENSION '''


squared_list2 = [i**2 for i in list]
print(f"Squared list 2: {squared_list2}")

# =======================================================

# another example   (filtering even numbers):

numbers = [1, 4, 45, 2, 76, 89, 66, 74, 80]

even_numbers = [i for i in numbers if i % 2 == 0]
print(f"Even numbers: {even_numbers}")

# =======================================================

# another example   (converting words to upper case):

words = ["hello", "world", "python", "harry potter"]

uppercase = [i.upper() for i in words]
print(f"Upper case words: {uppercase}")