# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  LENGTH OF SET
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: len(setName)
# calculates the length of the set.

sets = {32, 41, 15, "Arif", False, 32, False, 20, 15}
print(f"Length of the set is: {len(sets)}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  REMOVE METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: setName.remove(valueToBeRemoved)
# removes the value from the set.
# will return an error if the value is not present in the set.

sets.remove(41)
print(f"Set after removal of an element: {sets}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  POP METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: setName.pop()
# removes the a random value from the set.

sets.pop()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UNION METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: setName1.union(setName2)
# combine the two sets and returns as single set.

set1 = {51, 22, 30, 76, 1, 27, 33, 50}
set2 = {11, 88, 27, 34, 29, 50, 33, 65}
print(set1.union(set2))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  INTERSECTION METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: setName1.intersection(setName2)
# returns a set with common values of both sets.

print(set1.intersection(set2))