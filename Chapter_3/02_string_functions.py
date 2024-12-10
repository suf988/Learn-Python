# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LEN FUNCION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: len(stringName)
# calculates the length of the string.
str1 = "Harry Potter"
print(f"Length of string: {len(str1)}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ENDSWITH FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.endswith("endingLettersOfString")
# checks whether the string ends with given ending or not. (The checking is case-sensitive)
str2 = "Stupify"
print(str2.endswith("fy"))  #True
print(str2.endswith("sy"))  #False

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# STARTSWITH FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.startswith("startingLettersOfString")
# checks whether the string starts with given starting or not. (The checking is case-sensitive)
print(str2.startswith("St")) #True
print(str2.startswith("st")) #False

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# COUNT FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.count("anyCharacter")
# counts the total number of occurances of a character in a string

str3 = "banana"
print("Count of 'a' in banana:", str3.count("a"))