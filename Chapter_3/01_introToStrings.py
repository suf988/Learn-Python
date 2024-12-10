# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTRO TO STRINGS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

string1 = "Harry Potter"

print("Slicing a character: ",string1[6])   #slicing a character by "stringName[indexOfCharacter]"

print("Slicing a string: ",string1[0:7]) #slicing a string by "stringName[startingIndex:endingIndex]" where ending index wont be counted

print("Slicing without giving first parameter: ",string1[:9])  #pehla parameter khali hai mtlb 0 se start ho rha hai

print("Slicing without giving last parameter: ",string1[2:])  #ankhri parameter khali hai mtlb length-1 tk slice hoga

print("Slicing without giving both parameters: ",string1[:])  #dono parameter khali hai mtlb 0 se start ho rha hai aur length-1 tk slice hoga

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEGATIVE SLICING
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# normal length (positive length) 0 se start hoti hai LEFT TO RIGHT
# negative length -1 se start hoti hai from RIGHT TO LEFT

name = "Hermione Granger"

print("Negative Slicing: ",name[-13:-5]) #-13 length se start hui slicing aur -5 se phle wali length tk slicing ki

print(name[-5:-13]) #this would be wrong because starting index should be less than ending index