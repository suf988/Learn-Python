# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# COUNT METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: tupleName.count(value)
# will return the number of times the given value is present in a tuple.

tup1 = (32, 43.2, False, "Harry", "Hermione", False)
print(tup1.count(False))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  INDEX METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: tupleName.indexh(value)
# will return the index of first occurance of searched value in the tuple
# will raise an error if the value is not found in the tuple

print(tup1.index("Hermione"))