# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  EXCEPTION HANDLING
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a code must not crash even if there is an error in the input.
# instead the error should be handled to keep the code running.

try:
    a = int(input("Enter a value: "))
    print(a)
except Exception as e:
    print(e)

# ================================================

# we can also specify to catch certain type of errors as:

try:
    b = int(input("Enter a number: "))
    print(b)
except ZeroDivisionError as z:      # for handling zero division error
    print(z)
except TypeError as t:              # for handling type error
    print(t)
except ValueError as v:             # for handling value error
    print(v)
except Exception as e:              # for handling all the other exceptions
    print(e)