# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  LAMBDA FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# A lambda function is just another way to write a function.

# Simple function:
def sum(a,b):
    return a+b

print(f"Sum of two numbers using Simple function: {sum(5,17)}")


# lambda function:

# SYNTAX:  variable = lambda arg1,arg2.... : return code
multiply = lambda a,b: a*b

print(f"Product of two numbers using Lambda function: {multiply(5,17)}")