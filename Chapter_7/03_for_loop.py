# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  FOR LOOP 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

for i in range(4):  #this 4 will automatically goes like range(0:4), where 0 will be counted but 3 instead of 4.
    print(i)

print("======================================")

# ==============================================================

# we can also specify skipping steps in for loop:

for j in range(0, 100, 4):  #will loop from 0 to 100, while taking every 4th step only.
    print(j)

print("======================================")

# ==============================================================

# for loop in list:

greeting = ["Buongiorno", "Buona Giornata", "Buon Pomoreggio", "Buona Sera", "Buona Serata", "Buono Notte"]

for val in greeting:   #will iterate over whole list automatically
    print(val)

print("======================================")

# ==============================================================

# for loop in tuple:

italiano = ("Ciao", "Come stai", "Come va", "Come ti chiami", "Di dove sei", "Sei fame", "Dove vai")

for newVal in italiano: #will iterate over whole tuple
    print(newVal)

print("======================================")

# ==============================================================

# for loop in string:

name = "Constantinople"

for k in name:  #will iterate over whole string
    print(k)