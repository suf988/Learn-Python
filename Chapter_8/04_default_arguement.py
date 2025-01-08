# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  DEFAULT ARGUMENT IN FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# we can provide any default argument in a function. it will be used in the function if no value is given to the function for that argument.

def greet(name, greeting = "Hello"):    #we have given "hello" as a default value in greeting argument
    print(f"{greeting} {name}, how are you?")

greet("Harry", "Good morning")
greet("Hermione")   # we have not given any value to the second argument so the function will use default value.