# ASSIGNMENT OPERATOR
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
a = 1
b = 2
c = a+b

print (c)

# ------------------------------------------------------

initialValue = 5
initialValue += 4   #increment of 4 in the initial value
initialValue -= 4   #decrement of 4 in the initial value

print(initialValue)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# COMPARISON OPERATOR
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

num_1 = 15
num_2 = 19

print(num_1 > num_2)  #False
print(num_1 < num_2)  #True
print(num_1 >= num_2)  #False
print(num_1 <= num_2)  #True
print(num_1 != num_2)  #True
print(num_1 == num_2)  #False

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LOGICAL OPERATOR ('and', 'or' & 'not')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Truth table of 'or' (Ek bhi true hoga tou answer "True" ayega)
print("True or True is: ", True or True)
print("True or False is: ", True or False)
print("False or True is: ", False or True)
print("False or False is: ", False or False)

# Truth table of 'and' (Sarey options true hongy tou hi "True" return krega warna "False")
print("True and True is: ", True and True)
print("True and False is: ", True and False)
print("False and True is: ", False and True)
print("False and False : ", False and False)

# 'not' operator works on a single boolean operands and inverses it (False ko True & True ko False)

print(not(True)) #False
print(not(False)) #True