# Q5: Repeat program 4 for a list of such words to be censored.

censor_words = ["crap", "sucks", "annoying", "stupid", "cheap content"]

with open("censored_text.txt", "r") as f:
    data = f.read()
    if censor_words in data:
        updated_data = data.replace(censor_words, "#####")

with open("censored_text.txt", "w") as f:
    f.write(updated_data)


