# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  BREAK IN FOR LOOP
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# "break" stops the loop there the condition is matched and exits the loop.

for i in range(9):
    if(i==6):
        break   #when i == 6, the loop will break, leaving out all the further iteration
    print(i)