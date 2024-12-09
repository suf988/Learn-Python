# DATA TYPES
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a = 31
print(type(a))  #class <int>

b = 31.32
print(type(b))  #class <float>

c = "Harry Potter"
print(type(c))  #class <str>

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  TYPE CASTING (CONVERSION OF TYPE)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#String to Integer:
str1 = "32"
str_to_int = int(str1)
print("Type before conversion: ", type(str1))
print("Type after conversion: ", type(str_to_int))

#String to Float:
str_to_float = float(str1)
print("Type before conversion: ", type(str1))
print("Type after conversion: ", type(str_to_float))

#Integer to Float:
int1 = 32
int_to_float = float(int1)
print("Type before conversion: ", type(int1))
print("Type after conversion: ", type(int_to_float))

#Integer to String:
int_to_str = str(int1)
print("Type before conversion: ", type(int1))
print("Type after conversion: ", type(int_to_str))

#Float to Integer:
float1 = 76.49
float_to_int = int(float1)
print("Type before conversion: ", type(float1))
print("Type after conversion: ", type(float_to_int))

#Float to String:
float_to_str = str(float1)
print("Type before conversion: ", type(float1))
print("Type after conversion: ", type(float_to_str))