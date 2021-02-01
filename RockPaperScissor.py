import random

computer = random.randint(1,4)
player_choice = input("Choose either Rock, Paper, or Scissors:  ")

if computer ==1:
    computer = "rock"
elif computer == 2:
    computer = "paper"
else:
    computer = "scissors"


if player_choice.lower().startswith("r") and computer=="rock":
    print("Draw")
elif player_choice.lower().startswith("r") and computer=="paper":
    print("sorry, the computer chose paper, you lose.")
elif player_choice.lower().startswith("r") and computer=="scissors":
    print("You win!  The computer chose scissors!")
elif player_choice.lower().startswith("p") and computer=="rock":
    print("Congrats!  You win, the computer chose rock.")
elif player_choice.lower().startswith("p") and computer=="paper":
    print("Draw!")
elif player_choice.lower().startswith("p") and computer=="scissors":
    print("sorry, you lose.  The computer chose scissors.")
elif player_choice.lower().startswith("s") and computer=="rock":
    print("Sorry, you lose.  The computer's rock crushes your scissors.")
elif player_choice.lower().startswith("s") and computer=="paper":
    print("Congrats!  Your scissors cut straight through the computer's paper.")
elif player_choice.lower().startswith("s") and computer=="scissors":
    print("Draw")

