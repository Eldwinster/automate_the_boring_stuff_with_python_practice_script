#!/usr/bin/env python
# https://realpython.com/python-sleep/
# TODO ajoute une fonction de comptage pour trouver la solution.
# TODO Ajoute une limitation pour trouver genre en 10 essaie ou 5 ou 3 etc. on peut meme donner le choix au joueur.
# TODO Ajoute une memoire de scores
import random, sys, time
ATTEMPT_COUNT = 0
ATTEMPT_LIMIT = 10

def guess_number():
    # return random.choice(range(1, 101))
    return random.randint(1, 101)

# Give the rules of the game
def rules_description():
    guessNumber = guess_number()
    print(f"Fine {playerName}, let me explain you how to play.",
          "I will first choose a number between 1 and 100.",
          f"For example, let say I choose {guessNumber}. Of course, you don't know it.",
          f"Once I choose my number, {guessNumber} in this case, it's your turn to play.",
          "You would give me a number between 1 and 100.",
          "Based on your number I can only say whether my number is higher or lower.",
          f"You will be given only {ATTEMPT_LIMIT} chances to guess the right number"
          "We repeat the process until you find the right number or fail!",
          sep='\n')

# Check if player knows the rules
def rules():
    ruleState = input("Do you know how to play? [y|n] ")
    while True:
        if ruleState.lower() == "y":
            break
        elif ruleState.lower() == "n":
            rules_description()
            ruleUnderstanding = input("Have you understand how to play? [y|n] ")
            if ruleUnderstanding.lower() == "y":
                break
            elif ruleUnderstanding.lower() == "n":
                continue
def count_attempt():
    global ATTEMPT_COUNT
    ATTEMPT_COUNT+= 1
    if ATTEMPT_COUNT <= ATTEMPT_LIMIT:
        print(f"Wrong guess / chance given : {ATTEMPT_COUNT} / {ATTEMPT_LIMIT}")
    elif ATTEMPT_COUNT > ATTEMPT_LIMIT:
        print(f" Sorry you've made {ATTEMPT_LIMIT} wrong guess.")
    else:
        pass

def game_loop():
    global gameState
    global ATTEMPT_COUNT
    while True:
        print("Ok let's play then.")
        print("Let met guess")
        guessNumber = guess_number()
        while gameState.lower() == "y":
            if ATTEMPT_COUNT > ATTEMPT_LIMIT:
                break
            else:
                print("I got a number, so what's your guess?")
                playerGuess = input("Give me a number between 1 and 100 ")
                if not playerGuess.isdigit():
                    print("Oy, that's not a number!")
                    continue
                elif playerGuess.isdigit():
                    playerGuess = int(playerGuess)
                    if playerGuess < 1:
                        print("This less than 1, remember I choose a number between 1 and 100.")
                        continue
                    elif playerGuess > 100:
                        print("This more than 100, remember I choose a number between 1 and 100.")
                        continue
                    elif playerGuess >= 1 and playerGuess <= 100:
                        if playerGuess < guessNumber:
                            print(f"{playerGuess} is too low.")
                            count_attempt()
                            continue
                        elif playerGuess > guessNumber:
                            print(f"{playerGuess} is too high.")
                            count_attempt()
                            continue
                        elif playerGuess == guessNumber:
                            print("Congratulation, you've guessed the right number!",
                                    f"{playerGuess} = {guessNumber}",
                                    sep='\n')
                            ATTEMPT_COUNT = 0
                            break
        gameState = input("Would you like to play again? [y|n] ")
        if gameState.lower() == "y":
            continue
        elif gameState.lower() == "n":
            print(f"Have a nice day {playerName}")
            sys.exit()


# Game loop
def main():
    global gameState
    gameState = input("Would you like to play guess the number? [y|n] ")
    if gameState.lower() == "n":
        print(f"That fine, I hope you have a nice day {playerName} !")
        sys.exit()
    elif gameState.lower() == "y":
        pass
    rules()
    game_loop()

print("Hi there! What's your name? ")
playerName = input().capitalize()
aiName = "0x0"
print(f"Nice to meet you {playerName}, I'm {aiName}.")
main()
    # for i in range(4):
    #     print("hmm", "m" * i, sep='')
    #     time.sleep(0.5)
        # guessNumber = random.choice(range(1,101))
