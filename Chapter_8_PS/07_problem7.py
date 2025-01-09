# Q7: Write a python function to remove a given word from a list ad strip it at the same time.

def modify(arr, word):
    new_list = []

    for item in arr:
        if item != word:
            new_list.append(item.strip(word))
    return new_list

old_list = ["Rohan", "Suresh", "Rohit", "Aman", "an"]

print(modify(old_list, "an"))