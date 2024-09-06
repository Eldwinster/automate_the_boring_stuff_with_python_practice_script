#!/usr/bin/env python
import random, sys
COMPUTER_NAME = "0x0"
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
QUIT = "q"

def basicAi():
    symbols = ("r", "p", "s")
    return random.choice(symbols)

def main():
    PLAYER_NAME = input("What is your name? ").capitalize()
    win = 0
    loss = 0
    tie = 0
    gameTurns = 0
    RESULT_VALUE = 100
    while True:
        gameTurns += 1
        print(f"ROCK, PAPER, SCISSORS: ROUND {gameTurns}",
              f"{win} Wins, {loss} Losses, {tie} Ties",
              f"Enter your move: ({ROCK})ock ({PAPER})aper ({SCISSORS})cissors or ({QUIT})uit",
              sep="\n")
        playerChoice = input()
        computerChoice = basicAi()
        winMessage = f"{PLAYER_NAME}: {playerChoice} vs {computerChoice} :{COMPUTER_NAME} " + f"{PLAYER_NAME} wins!"
        lossMessage = f"{PLAYER_NAME}: {playerChoice} vs {computerChoice} :{COMPUTER_NAME}" + f"{COMPUTER_NAME} wins!"
        tieMessage = f"{PLAYER_NAME}: {playerChoice} vs {computerChoice} :{COMPUTER_NAME}" + f"{PLAYER_NAME} and {COMPUTER_NAME} have tied!"
        if playerChoice == ROCK:
            if playerChoice == computerChoice:
                tie += 1
                RESULT_VALUE = 0
            elif computerChoice == PAPER:
                loss += 1
                RESULT_VALUE = -1
            elif computerChoice == SCISSORS:
                win += 1
                RESULT_VALUE = 1
        elif playerChoice == PAPER:
            if playerChoice == computerChoice:
                tie += 1
                RESULT_VALUE = 0
            elif computerChoice == SCISSORS:
                loss += 1
                RESULT_VALUE = -1
            elif computerChoice == ROCK:
                win += 1
                RESULT_VALUE = 1
        elif playerChoice == SCISSORS:
            if playerChoice == computerChoice:
                tie += 1
                RESULT_VALUE = 0
            elif computerChoice == ROCK:
                loss += 1
                RESULT_VALUE = -1
            elif computerChoice == PAPER:
                win += 1
                RESULT_VALUE = 1
        elif playerChoice == QUIT:
            sys.exit()
        else:
            print(f"You have to input either {ROCK}, {PAPER}, {SCISSORS}, or {QUIT}",
                  "Otherwise we can't play.",
                  sep='\n')
        if RESULT_VALUE == 1:
            print(winMessage, sep="\n")
        elif RESULT_VALUE == -1:
            print(lossMessage, sep='\n')
        elif RESULT_VALUE == 0:
            print(tieMessage, sep='\n')
        else:
            pass
try:
    main()
except KeyboardInterrupt:
    sys.exit()
