import random
def guessing(guess,tries):
    print(f"You have {tries} to guess the number.\n")
    over = False
    while not over :
        player_guess = int(input("Make a guess : "))
        if player_guess == guess :
            print(f"You got it. The answer is {guess}.\n")
            over = True
            break
        elif (player_guess > guess) :
            if (player_guess - guess) <= 10 :
                print("Wrong but close.\nGuess lower.\n")
            else :
                print("Too High.\nGuess lower.\n")
            tries-=1

        elif (player_guess < guess) :
            if (guess - player_guess) <= 10 :
                print("Wrong but close.\nGuess higher.\n")
            else :
                print("Too Low.\nGuess higher.\n")
            tries-=1
        if(tries == 0):
            print("You have run out of guesses.\n")
            over = True
            break
        print(f"You have {tries} attempts remaining to guess the number.\n")


ART="""
                                                                                                                                                                  

  ____  __ __    ___  _____ _____ ____  ____    ____               ____   ____  ___ ___    ___ 
 /    ||  |  |  /  _]/ ___// ___/|    ||    \  /    |             /    | /    ||   |   |  /  _]
|   __||  |  | /  [_(   \_(   \_  |  | |  _  ||   __|            |   __||  o  || _   _ | /  [_ 
|  |  ||  |  ||    _]\__  |\__  | |  | |  |  ||  |  |            |  |  ||     ||  \_/  ||    _]
|  |_ ||  :  ||   [_ /  \ |/  \ | |  | |  |  ||  |_ |            |  |_ ||  _  ||   |   ||   [_ 
|     ||     ||     |\    |\    | |  | |  |  ||     |            |     ||  |  ||   |   ||     |
|___,_| \__,_||_____| \___| \___||____||__|__||___,_|            |___,_||__|__||___|___||_____|
                                                                                               

                                                                                                                      
"""
print(ART)
print("Welcome to the number guessing game.\n")
print("I am thinking of number between 1 and 100.\n")
game_mode = input("Choose a difficulty. Type 'easy' or 'hard':  ")
if game_mode == "easy" :
    num_of_tries = 10
elif game_mode == "hard" :
    num_of_tries = 5
else :
    print("Enter an valid input.\n")
computer_guess = random.randint(1,100)
guessing(computer_guess,num_of_tries)
