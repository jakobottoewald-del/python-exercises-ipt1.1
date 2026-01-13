#!/usr/bin/env python3
import sys
import random

computer_num = random.randint(0,2)
player = sys.argv[1]

if computer_num == 0:
	computer = "rock"
elif computer_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print("Spieler:", player)
print("Computer:", computer)

if player == computer:
	print("Unentschieden!")

elif(player == "scissors" and computer == "paper") or \
    (player == "paper" and computer == "rock") or \
    (player == "rock" and computer == "scissors"):
	print("Der Spieler gewinnt!")

else:
	print("Der Cumputer gewinnt!")

