# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  REDUCE FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The reduce() function is used to apply a function cumulatively to the elements of an iterable, reducing it to a single value.

# SYNTAX: reduce(function, iterable)

''' IMPORTANT ''' # reduce() is not a built-in function in Python 3. It must be imported from "functools"


from functools import reduce

numbers = [3, 7, 2, 9, 5]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)

# another example: (product of a list)
product = reduce(lambda x,y: x*y, numbers)
print(product)


# another example: (maximum number from a list)
maximum = reduce(lambda x,y: x if x > y else y, numbers)
print(maximum)