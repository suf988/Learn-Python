# Q7: Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write a sentence: ").lower()

if(post.find("harry") != -1):
    print("Your post is talking about Harry.")
else:
    print("Your post is not talking about Harry.")