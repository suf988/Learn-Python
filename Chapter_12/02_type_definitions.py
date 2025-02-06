# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TYPE DEFINITIONS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# type-definitions or type-hints is a way to make the code more documented by defining their types at the time of the declaration of variables or functions.

'''
SYNTAX:

FOR VARIABLES:      a : datatype = value
FOR FUNCTIONS:      def func(a: datatype ,b: datatype) -> returnDatatype:

'''

a = 15         # normal way to write
a: int = 15    # using type definition

name = "harry"       # normal way to write
name: str = "harry"  # using type definition

def func1(a: int, b: int)-> int:
    return a+b

result = func1(5,2)
print(result)

# ============================================================

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid