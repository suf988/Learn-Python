# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UPDATE FILE (r+)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# used to read and update an existing file.
# will throw an error if the file doesn't exist.
# can update the file, but all the content of the file is not deleted when you open it to update.
# can not add new content at the end, because it will be appending then.

f = open("written_file.txt", "r+")
content = f.read()
print(f"Original content: {content}")
f.write("This line is written using update mode (r+) ")

f.close()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  UPDATE FILE (w+)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# used to read and update an existing file.
# will create a new file if the file doesn't exist
# all the existing content will be deleted and the updated content you entered will be stored in the file.

f = open("written_file.txt", "w+")

f.write("The file is updated with the new content and all the previous existing content is deleted because we have used update method (w+).")

f.close()