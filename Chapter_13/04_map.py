# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MAP FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The map() function applies a given function to each item in an iterable (like a list or tuple) and returns a new iterable (a map object).

# SYNTAX: map(function, iterable)

numbers = [12, 14, 5, 8, 7]
sqr = lambda x: x**2

print(list(map(sqr, numbers)))

# another example:

words = ["hello", "world", "python"]
uppercase = lambda x: x.upper()
print(list(map(uppercase, words)))

# another example:

a = [1, 2, 3]
b = [4, 5, 6]

sum = lambda x,y: x+y

print(list(map(sum, a,b)))