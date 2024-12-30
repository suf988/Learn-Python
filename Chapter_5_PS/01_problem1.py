# Q1: Write a program to create a dictionary of Italian words with values as their English translation. Provide user with an option to look it up!

words = {
    "Sedia": "Chair",
    "Tavolo": "Table",
    "Cucchiaio": "Spoon",
    "Forchetta": "Fork",
    "Coltello": "Knife",
    "Piatto": "Plate",
    "Bicchiere": "Glass",
    "Tazza": "Cup"
}

search = input("Enter the word you want to know meaning of: ")
print(f"Meaning of '{search}' is: {words[search]}")