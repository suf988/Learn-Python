# Q4: A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = 'donkey'

with open("donkey_text.txt", "r") as f:
    data = f.read()
    if word in data:
        updated_data = data.replace(word, "#####")

with open("donkey_text.txt", "w") as f:
    f.write(updated_data)