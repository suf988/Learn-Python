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