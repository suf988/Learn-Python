# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READ FILE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

f = open("file.txt")    #open() is a built-in python function to tell that is file is opened for some work.

data = f.read()         # read() function can read the material in the file.

print(data)

f.close()               #close() function is used to specify that the work has been done and the file is closed.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READLINES
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# readlines will read all the lines individually and return a list of each line in that file.

f = open("file.txt")

data = f.readlines()

print(data, type(data))

f.close()

# OUTPUT:

# ['Twinkle twinkle little star\n', '\n', 'How I wonder what you are\n', '\n', 'Up, above the world so high\n', '\n', 'Like a diamond in the sky'] <class 'list'>