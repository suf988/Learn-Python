# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD (sorting in ascending order) 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Syntax: sort()
# sort the list of numbers in ascending order.

l1 = [1, 8, 7, 2, 21, 15]
l1.sort()
print(l1)

# ------------------------------------------------------

# strings are sorted in lexographical order.
l2 = ["banana", "apple", "cherry", "date"]
l2.sort()
print(l2)   #['apple', 'banana', 'cherry', 'date']


# Uppercase words will be preferred over lowercase words.
l3 = ["Banana", "apple", "Cherry", "date"]
l3.sort()
print(l3)   #['Banana', 'Cherry', 'apple', 'date']

l3.sort(key=str.lower)  # "key=str.lower" ignores the case sensitivity
print(l3)   #['apple', 'Banana', 'Cherry', 'date']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD (sorting in descending order)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: list.sort(reverse=True)
# using "reverse=True" inside the sort method will sort the list in descending order

numbers = [5, 2, 9, 1, 7]
numbers.sort(reverse=True)
print(numbers) #[9, 7, 5, 2, 1]

l4 = ["Banana", "apple", "Cherry", ]
l4.sort(key=str.lower, reverse=True)
print(l4)   #['date', 'Cherry', 'Banana', 'apple']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++