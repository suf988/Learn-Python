# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LISTS 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# list is just an array in python languge in which you can store data in different dataypes

data = ["Harry", 5, 354.98, "Potter", False]
print(data)
print(data[4])

data[4] = True  #unlike strings, lists are mutable
print(data[4])


# lists can be sliced, just like strings.
print(data[1:4])