# Q7: If the names of 2 friends are same; what will happen to the program in problem 6?

# the new key-value pair will update the older one.

languages = {
    "Harry": "Python",
    "Hermione": "JavaScript",
    "Ron": "Java",
    "Harry": "C++", #key is repeating
}

print(languages)    # {'Harry': 'C++', 'Hermione': 'JavaScript', 'Ron': 'Java'}