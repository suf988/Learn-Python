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

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CAPITALIZE FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.capitalize()
# capitalize only the first letter of a string

str4 = "michelle ali"
print(str4.capitalize())    #Michelle ali

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TITLE FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.title()
# capitalize all the starting letters of a string

print(str4.title()) #Michelle Ali

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# UPPER FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.upper()
# converts all the string to upper case.

str5 = "this is a lowercase sentence."
print(str5.upper()) #THIS IS A LOWERCASE SENTENCE.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LOWER FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.upper()
# converts all the string to lower case.

str5 = "THIS IS AN UPPERCASE SENTENCE."
print(str5.lower()) #this is an uppercase sentence.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FIND FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.find("word")
# returns the index of the first occurance of that word in a string.

str5 = "I don't live in Pakistan now, I live in Italy."
print(str5.find("live")) #8

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# REPLACE FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.replace("old_word", "new_word")
# finds the old word in the string and replace it with the new one.

str6 = "I live in Pakistan."
print(str6.replace("Pakistan", "Italy")) #8

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# STRIP FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.strip()
# removes the whitespaces from starting and ending of a string.

str7 = "    Hello     "
print(str7.strip()) #Hello

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LSTRIP FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.lstrip()
# removes the whitespaces from starting of a string.

print(str7.strip()) #Hello

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# RSTRIP FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Syntax: stringName.rstrip()
# removes the whitespaces from ending of a string.

str7 = "    Hello     "
print(str7.rstrip()) #    Hello