# Q8: If languages of two friends are same; what will happen to the program in problem 6?


# both the languages will be stored in dictionary as multiple same values can be stored in dictionary.

languages = {
    "Harry": "Python",
    "Hermione": "JavaScript",
    "Ron": "Java",
    "Draco": "Python", #value is repeating
}

print(languages)    #{'Harry': 'Python', 'Hermione': 'JavaScript', 'Ron': 'Java', 'Draco': 'Python'}