# Name: Michael Lochner
# Section: CIS 115 Spring 2020
# Project: Pickup Sticks Game
# Description: Pickup Sticks game with 2 modes: PvP, or PvAI. 
import random
import time

#Prints the sticks to the terminal
def printSticks(n):
    stick = "|  "
    num_of_sticks_iterator = 1

    print("\n")

    i = 1
    while i <= 4:
        for x in range(n):
            if x < 9:
                print(stick, end='')
            elif x >= 9:
                hold_stick = stick + " "
                print(hold_stick, end='')
        print("")
        i += 1
    for x in range(n):
        hold_num = str(num_of_sticks_iterator) + "  "
        print(hold_num, end='')
        num_of_sticks_iterator += 1
    print("")

# Checks to see if a player has won, if not, then next turn
# if so, prints a congrats and ends game
def CheckIfWon(sticks, players_turn, players_choice):
    if sticks == 1:
        print(players_turn + " has won the game!")
        return True
    elif sticks < 1:
        print(players_turn + " has lost the game!")
        return True
    else:
        return False

# Prompt the player with the option to chose a number of sticks (1-3)
def ChooseSticks(players_turn):
    players_choice = int(input("\n" + players_turn + "'s turn. Choose to remove 1, 2, or 3 sticks: "))
    while players_choice < 1 or players_choice > 3:
        players_choice = int(input("Incorrect number. Please choose 1, 2, or 3 sticks: "))
    return players_choice

# How to game runs through when called
def SticksGame(mode):
    sticks = 20
    printSticks(sticks)

    player_1 = "Player 1"
    player_2 = "Player 2"
    player_AI = "Player AI"
    players_turn = player_1
    game_over = False
    while game_over != True:

        # PvP mode
        if mode == 1:
            players_choice = ChooseSticks(players_turn)
            sticks -= players_choice
            printSticks(sticks)

            print("\n" + players_turn +" took " + str(players_choice) + " sticks. There are " + str(sticks) + " sticks left\n")
            game_over = CheckIfWon(sticks, players_turn, players_choice)

            if players_turn == player_1:
                players_turn = player_2
            elif players_turn == player_2:
                players_turn = player_1

        # PvAI mode
        # AI just chooses a random number between 1 and 3.. 
        # so it's really not an AI..
        elif mode == 2:
            if players_turn == "Player 1":
                players_choice = ChooseSticks(players_turn)
                
            elif players_turn == "Player AI":
                time.sleep(1) #----------------------- makes it seem like AI is thinking
                players_choice = random.randint(1, 3)
                
            
            sticks -= players_choice
            printSticks(sticks)

            print("\n" + players_turn +" took " + str(players_choice) + " sticks. There are " + str(sticks) + " sticks left\n")
            game_over = CheckIfWon(sticks, players_turn, players_choice)

            if players_turn == player_1:
                players_turn = player_AI
            elif players_turn == player_AI:
                players_turn = player_1

# Initial prompt to Start the game
def StartGame():
    opt_1 = "1. Player vs Player"
    opt_2 = "2. Player vs AI"
    mode = int(input("\nHow would you like to play? \n" + opt_1 + " \n" +opt_2 +  "\n(Enter the number): "))

    SticksGame(mode)


StartGame()