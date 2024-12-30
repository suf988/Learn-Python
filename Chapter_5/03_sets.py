# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  SETS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# sets are also a collection, denoted by {}
# sets have collection of unique values, means that no value is repeated in sets.

# to create empty set:
emptySet = set()
print(type(emptySet))

sets = {32, 41, 15, "Arif", False, 32, False, 20, 15}
print(sets) # {32, False, 20, 'Arif', 15, 41}       repeated values are not stored.
# sets are unordered, python does not maintain the sequence of the data entered. it is stored in random order

# length of sets:
print(len(sets))