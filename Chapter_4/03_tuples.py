# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TUPLES 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# tuples are just like array/list but they are immutable. they are defined by ()

tup1 = ()
print(type(tup1))

#tup2 = (1)  #this is the wrong way to enter one item in tuples, it will be read as 'int'
tup2 = (1,) #tuple with only one value needs a comma

tup3 = (32, 43.2, False, "Harry", "Hermione")
print(f"tup3 is a {type(tup3)}, and its values are: {tup3}")