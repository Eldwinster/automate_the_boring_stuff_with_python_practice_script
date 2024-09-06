#!/usr/bin/env python
# https://realpython.com/python-sleep/
# TODO ajoute une fonction de comptage pour trouver la solution.
# TODO Ajoute une limitation pour trouver genre en 10 essaie ou 5 ou 3 etc. on peut meme donner le choix au joueur.
import random, sys, time

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
          "We repeat the process until you find the right number!",
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

# Game loop
def main():
    gameState = input("Would you like to play guess the number? [y|n] ")
    if gameState.lower() == "n":
        print(f"That fine, I hope you have a nice day {playerName} !")
        sys.exit()
    elif gameState.lower() == "y":
        pass
    rules()
    while True:
        print("Ok let's play then.")
        print("Let met guess")
        guessNumber = guess_number()
        while gameState.lower() == "y":
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
                        continue
                    elif playerGuess > guessNumber:
                        print(f"{playerGuess} is too high.")
                        continue
                    elif playerGuess == guessNumber:
                        print("Congratulation, you've guessed the right number!",
                              f"{playerGuess} = {guessNumber}",
                              sep='\n')
                        break
            gameState = input("Would you like to play again? [y|n] ")
            if gameState.lower() == "y":
                continue
            elif gameState.lower() == "n":
                print(f"Have a nice day {playerName}")
                sys.exit()


print("Hi there! What's your name? ")
playerName = input().capitalize()
aiName = "0x0"
print(f"Nice to meet you {playerName}, I'm {aiName}.")
main()
    # for i in range(4):
    #     print("hmm", "m" * i, sep='')
    #     time.sleep(0.5)
        # guessNumber = random.choice(range(1,101))
