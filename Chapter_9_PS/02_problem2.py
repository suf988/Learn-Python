# Q2: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing a game...")
    score = random.randint(1,99)    #random.randint() generates a random integer b/w the given range in parameters.
    print(f"Your Score: {score}")

    with open("high-score.txt") as f:
        high_score = f.read()

        if(high_score == ""):
            high_score = 0
        else:
            high_score = int(high_score)
    
    if score > high_score:
        with open("high-score.txt", 'w') as f:
            f.write(str(score))

game()