# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  DICTIONARY MERGE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# now you can merge the dictionary with new and more readible syntax.
# it returns a new dictionary with merged values from both dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2) # old way
print(dict1)

merged_dict = dict1 | dict2 # new way
print(merged_dict)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  DICTIONARY UPDATE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# now you can update the dictionary with new and more readible syntax.
# it just updates the dictionary without creating a new one.

dict1 |= dict2
print(dict1)