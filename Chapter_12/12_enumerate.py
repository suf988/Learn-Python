# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ENUMERATE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# the 'enumerate' function adds a counter to an iterable and returns it.

''' WITHOUT ENUMERATE '''

list1 = [14, 24, "Harry", True, 34.2]
index = 0

for item in list1:
    print(f"The item on index {index} is: {item}")
    index += 1


''' WITH ENUMERATE FUNCTION '''

for index2, item in enumerate(list1):
    print(f"The item on index {index2} is: {item}")