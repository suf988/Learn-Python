# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  WRITE FILE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# write() method is used to write some text into a file.
# using "w" mode will create a new fiel adn write the given text into that file.

f = open("written_file.txt", "w")   #2nd parameter is given to specify the purpose for which the file is opened.

f.write("This is a text file written by using f.write() function")

f.close()