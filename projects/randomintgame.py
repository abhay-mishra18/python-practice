# This program will select a random integer from 1 to 100 and wil make it highscore
# Then it will select a random integer for you if you no. id greater than highscore it will automatically feed it 
# as a highscore in "opp.txt" file

# before running this program, please make a txt file named ("opp.txt")


import random 
def game():
    print("You are playing the game :")
    score = random.randint(1,100)
    with open ("opp.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        
        else:
            highscore==0

    print(f"Your score is {score}")
    if(score<highscore):
        print(f"You need {highscore-score} more points to get highscore")
    else:
        print("You got the highscore")

    if(score>highscore):
        with open ("opp.txt","w") as file:
            file.write(str(score))   
            
    return score 

game()