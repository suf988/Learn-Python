# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTRO TO STRINGS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

string1 = "Harry Potter"

print(string1[6])   #slicing a character by "stringName[indexOfCharacter]"

print(string1[0:7]) #slicing a string by "stringName[startingIndex:endingIndex]" where ending index wont be counted

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEGATIVE SLICING
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# normal length (positive length) 0 se start hoti hai LEFT TO RIGHT
# negative length -1 se start hoti hai from RIGHT TO LEFT



name = "Hermione Granger"

print(name[-13:-5]) #-13 length se start hui slicing aur -5 se phle wali length tk slicing ki