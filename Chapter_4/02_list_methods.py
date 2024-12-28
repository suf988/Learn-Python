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

l4 = ["Banana", "apple", "Cherry", "date"]
l4.sort(key=str.lower, reverse=True)
print(l4)   #['date', 'Cherry', 'Banana', 'apple']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# REVERSE METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.reverse()
# will return the list in reverse order (won't sort the list in descending order, will just reverse it).

l5 = [57,11,65,98,1,32]
print(f"Before reversing the list: {l5}")
l5.reverse()
print(f"After reversing the list: {l5}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INDEX METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.index(valueToBeSearched)
# returns the first occurance of the value searched in the list.
# will raise an error if does not find any matching value in the list.

print(l5.index(11))
#print(l5.index(10)) #ERROR: 10 is not in the list


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# APPEND METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.append(valueToBeAdded)
# will add the given value at the end of the list.

l6 = ["Harry", "Hermione", "Ron", "Ginny"]
print(f"List before appending: {l6}")
l6.append("Luna")
print(f"List before appending: {l6}")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INSERT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.insert(index, value)
# will add the given value at the specified index of the list.

print(f"Original List: {l6}")
l6.insert(3,"Draco")
print(f"List after inserting: {l6}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# POP METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.pop(index)
# remove the value at the specified index of the list and returns it

# l6.pop(3)
print(f"Value popped at index 3 {l6.pop(3)}")   #initial list length was 6, popped one value from it
print(l6)   #now the length of list is 5

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# REMOVE METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: listName.remove(value)
# will find the given value in list and remove the first occurance from the list.
# will raise an error if the given value is not present in the list.

print(f"Original Array: {l5}")
l5.remove(98)   #value is present in the list
print(f"Original Array: {l5}")
# l5.remove(33)   #ERROR: value is not present in the list