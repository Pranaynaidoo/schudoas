import random

play = ["rock", "paper", "scissors"]

computer = play[random.randint(0, 2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")  # Ask the player for their choice

    if player == computer:
        print("Tie!")  # Player's choice matches the computer's choice
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)  # Computer wins with paper
        else:
            print("You win!", player, "smashes", computer)  # Player wins with rock
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)  # Computer wins with scissors
        else:
            print("You win!", player, "covers", computer)  # Player wins with paper
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)  # Computer wins with rock
        else:
            print("You win!", player, "cuts", computer)  # Player wins with scissors
    else:
        print("That's not a valid play. Check the spelling!")  # Player's choice is invalid

    player = False
    computer = play[random.randint(0, 2)]  # Assign a new random choice for the computer
