# Q9: Write a program to find out whether a file is identical & matches the content of another file.

file_1 = "poems.txt"    #file_1 and file_2 have identical content but censored_text doesn't.
file_2 = "this.txt"

with open(file_1) as f:
    content_1 = f.read()

with open(file_2) as f:
    content_2 = f.read()

if content_1 == content_2:
    print(f"'{file_1}' and '{file_2}' have identical content")
else:
    print(f"'{file_1}' and '{file_2}' don't have identical content")

# ========================================================================

# (OPTIONAL / EXTRA) checking the failure case:

file_3 = "censored_text.txt"

with open(file_3) as f:
    content_3 = f.read()

if content_1 == content_3:
    print(f"'{file_1}' and '{file_3}' have identical content")
else:
    print(f"'{file_1}' and '{file_3}' don't have identical content")