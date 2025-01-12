# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READ FILE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# read() will read the whole txt file as a single string

f = open("file.txt")    #open() is a built-in python function to tell that is file is opened for some work.

data = f.read()         # read() function can read the material in the file.

print(data)

f.close()               #close() function is used to specify that the work has been done and the file is closed.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READLINES FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# readlines will read all the lines individually and return a list of each line in that file.

f = open("file.txt")

data = f.readlines()

print(data, type(data))

f.close()

# OUTPUT:

# ['Twinkle twinkle little star\n', '\n', 'How I wonder what you are\n', '\n', 'Up, above the world so high\n', '\n', 'Like a diamond in the sky'] <class 'list'>

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READLINE FUNCTION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# readline() reads the text line-by-line, means one line at a time. and then moves to the next line and read it.

f = open("file.txt")

data = f.readline() # will read only a single line from the file

print(data) #twinkle twinkle little star

f.close()