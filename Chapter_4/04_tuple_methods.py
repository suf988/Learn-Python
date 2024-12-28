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

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  IN METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: value in tupleName
# will return "true" if the seached value is present in the tuple, otherwise "false" shall be returned.
print(f"\"Harry\" is present in the tuple? {'Harry' in tup1}")  #true
print(f"\"65\" is present in the tuple? {65 in tup1}")  #true

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MIN MAX METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: min(tupleName)
# syntax: max(tupleName)
# will return smallest and the largest value of the tuple.

tup2 = (43, 21, 98, 45, 55, 49)
print(f"Minimum value of tuple: {min(tup2)}")
print(f"Maximum value of tuple: {max(tup2)}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  LEN METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: len(tupleName)
# will return the length of the tuple.

print(f"Length of the tuple \"tup1\" is {len(tup1)}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UNPACKING OF TUPLES
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# tuples can be unpacked into individual variables.

tup3 = ("Jon", False, "Wick", 32)
a, b, c, d = tup3
print(f"\"a\" = {a}\n\"b\" = {b}\n\"c\" = {c}\n\"d\" = {d}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  SLICING IN TUPLES 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: tupleName[startIndex : endIndex]
# will slice the tuple and return a new tuple with the sliced value.

print(f"Original Tuple: {tup3}")
print(f"Sliced Tuple: {tup3[1:len(tup3)]}")
