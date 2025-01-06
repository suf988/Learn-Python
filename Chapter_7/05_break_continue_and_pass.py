# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  BREAK IN FOR LOOP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# "break" stops the loop there the condition is matched and exits the loop.

for i in range(9):
    if(i==6):
        break   #when i == 6, the loop will break, leaving out all the further iteration.
    print(i)

print("====================================")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  CONTINUE IN FOR LOOP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# "continue" will skip only that iteration in which the condition is matched.

for j in range(9):
    if(j == 4):
        continue    #when j == 6, the loop will skip only that iteration and will move on to next iteration.
    print(j)

print("====================================")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  PASS IN FOR LOOP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# "pass" is a null statement, which means to do nothing.
# when you delare  a loop and want to do nothing in it and continue to work further, we use "pass" in that loop.

for k in range(5):
    pass    #this "pass" will nullify this loop and allow the further code to execute without error.

val = 0
while(val<3):
    print(val)
    val += 1