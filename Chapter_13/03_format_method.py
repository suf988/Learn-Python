# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FORMAT METHOD
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# The format() method is used to insert values into a string in a structured way. It allows for dynamic string formatting without using concatenation (+).

a = "My name is {} and I am {} years old.".format("Harry", 30)
print(a)    # My name is Harry and I am 30 years old.

b = "I have a {1} and a {0}.".format("cat", "dog")
print(b)    # I have a dog and a cat.

# this format method was used in previous versions but its not commonly used now due to the frequent use of "f-string"