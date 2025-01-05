# Q3: A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

spam_key1 = "make a lot of money"
spam_key2 = "buy now"
spam_key3 = "subscribe this"
spam_key4 = "click this"

user_input = input("Comment here: ")
str_to_lower = user_input.lower()

if((spam_key1 in str_to_lower) or (spam_key2 in str_to_lower) or (spam_key3 in str_to_lower) or (spam_key4 in str_to_lower)):
    print(f"Spam comment detected.")
else:
    print(f"Your comment: {user_input}")