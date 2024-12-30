# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  DICTIONARY 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a collection of key-value pair in python.
# just like objects in javascript, but the keys are written like json, with ""

# it is mutable, unordered, and there can't be any duplicate keys
# we can use "Strings" and "Integers" as keys

marks = {
    "Harry": 87,
    "Hermione": 95,
    "Ron": 76,
    "Draco": 81,
    "Movie Parts": [1,2,3,4,5,6,7,8],
    "Movie Name": "Harry Potter"
}

print(marks)
print(type(marks))  #dict

# for getting single value out of the dictionary:

print(marks["Harry"])   #most common
print(marks.get("Hermione"))    #another way, but not that straightforward


# length of dictionary:
print(len(marks))