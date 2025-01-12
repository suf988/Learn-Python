# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  READ FILE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

f = open("file.txt")    #open() is a built-in python function to tell that is file is opened for some work.

data = f.read()         # read() function can read the material in the file.

print(data)

f.close()               #close() function is used to specify that the work has been done and the file is closed.