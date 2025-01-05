# Q7: Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write a sentence: ").lower()

print("*****METHOD 1*****")
if(post.find("harry") != -1):
    print("Your post is talking about Harry.")
else:
    print("Your post is not talking about Harry.")

# OR

print("*****METHOD 2*****")

if("harry" in post):
    print("Your post is talking about Harry.")
else:
    print("Your post is not talking about Harry.")
    
