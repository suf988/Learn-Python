# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  WHILE LOOP 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# in while loop, we give a condition first as it is checked first. If the condition is true the operation inside the loop will execute until it is true.
# Once the condition is false, the operation execution will stop.

# Syntax: while(condition):
#            operation

i = 1

while(i<6):
    print(i)
    i += 1

print("============================================")
# ===============================================================

# Quick Quiz: Write a program to print 1 to 50 using a while loop.

val = 1
while(val<=50):
    print(val)
    val += 1

print("============================================")
# ===============================================================

# Quick Quiz: Write a program to print the content of a list using while loops.

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes", "Melon", "Kiwi"]

ind = 0
while(ind < len(fruits)):
    print(fruits[ind])
    ind += 1