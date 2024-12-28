# Q3: Check that a tuple type cannot be changed in python.

tuple1 = ("Taimoor", 23, True, 33.31, False, "Alex")
print(tuple1)

tuple1[2] = 33
print(tuple1)   #ERROR: tuple does not support item assignment.