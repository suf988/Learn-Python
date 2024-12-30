# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ITEMS METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.items()
# will return the list of all the key value pairs in the dictionary in tuples form.

dictionary = {
    "Name": "John",
    "Age": 31,
    "Nationalities": ["Italian", "American"],
    10: "Key can also be an integer"
}

print(dictionary.items())

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  KEYS METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.keys()
# will return the list of all the keys in the dictionary.

print(dictionary.keys())

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  VALUES METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.values()
# will return the list of all the values in the dictionary.

print(dictionary.values())

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UPDATE METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.update({"keyToUpdate": "newValue"})
# will update the existing key with a new value.
# if existing key is not found, then adds a new key-value pair

dictionary.update({"Name": "Bobby"})       #"Name" key exists, so it will be updated
dictionary.update({"Game": "Quiddich"})    #"Game" key doesn't exist, so new key-value pair will be added.
print(dictionary)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  GET METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.get("key")
# will return the value of specified key.

print(dictionary.get("Name"))


print(dictionary.get("Country"))   #this method will return "none" if the value is not found.
#print(dictionary["Country"])       #this method will return a key error if the value is not found.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  POP METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.pop("key")
# will remove the specified key form dictionary and returns the corresponding value of that key.
# if the key is not found then will raise an error, otherwise will return the default value if given.

print(dictionary.pop("Game"))
print(dictionary)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  POP ITEMS METHOD 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# syntax: dictionary_name.popitem()
# will remove the last key-value pair from the key and return it

print(dictionary.popitem())
print(dictionary)