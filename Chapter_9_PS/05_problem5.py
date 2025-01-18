# Q5: Repeat program 4 for a list of such words to be censored.

censor_words = ["crap", "sucks", "annoying", "stupid", "cheap content"]

with open("censored_text.txt") as f:
    data = f.read()
    
for i in censor_words:
    if i in data:
        data = data.replace(i, "#####")

with open("censored_text.txt", "w") as f:
    f.write(data)


