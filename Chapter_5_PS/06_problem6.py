# Q6: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

languages = {}

languages.update({input("Enter your name: "): input("Enter your favourite language: ")})
languages.update({input("Enter your name: "): input("Enter your favourite language: ")})
languages.update({input("Enter your name: "): input("Enter your favourite language: ")})
languages.update({input("Enter your name: "): input("Enter your favourite language: ")})

print(languages)