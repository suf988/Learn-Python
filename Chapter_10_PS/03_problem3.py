# Q3: Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Experiment:
    a = None

obj = Experiment()
print(obj.a)    # prints the class attribute bcoz instance attribute was not present

obj.a = 0   # instance attribute is set

print(obj.a)    # now prints the instance attribute

print(Experiment.a) # prints the class attribute bcoz it does not change.

# So, the answer is No, modifying from the instance attribute from will NOT change the class attribute.