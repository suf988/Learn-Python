# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  JOIN METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The join() method in Python is used to join elements of an iterable (like a list or tuple) into a single string, using a specified separator.

words = ["Harry", "Potter", "and", "the", "Chamber", "of", "Secrets"]
joined = " ".join(words)
print(joined)   # Harry Potter and the Chamber of Secrets


# another example:

fruits = ["Mango", "Banana", "Cherry"]
mixed_fruits = ", ".join(fruits)
print(mixed_fruits)   # Mango, Banana, Cherry

# another example:

word = "HELLO"
letters = "-".join(word)
print(letters)   # H-E-L-L-O