# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  WALRUS OPERATOR :=
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# walrus operator was introduced in python 3.8
# it allows you to assign values to the variable as a part of expression.

# it can assign a value to a variable and can use it in an expression such as condition/loop etc at the same time

# For example:

n = [1, 3, 5, 7, 9]

if len(n) > 3:
    print(f"List is too long, {len(n)} elements. Expected <= 3.")

# ====================================================================

# the above mentioned code can be written using walrus operator as:

if (i:= len([2, 4, 6, 8, 10])) > 4:
    print(f"The length is {i}, which is too long. Should be atleast 3")

#i is assigned the value of len([1, 2, 3, 4, 5]) and then used in the comparison within the if statement.

# ====================================================================

# another example:

