#!/usr/bin/env python3

import sys

card = sys.argv[1]

color = card[0]
value = card[1]

if color == "C":
    color_name = "Clubs"
elif color == "D":
    color_name = "Diamonds"
elif color == "H":
    color_name = "Hearts"
elif color == "S":
    color_name = "Spades"
else:
    color_name = "Unbekannte Farbe"

if value == "A":
    value_name = "Ace"
elif value == "X":
    value_name = "10"
elif value == "J":
    value_name = "Jack"
elif value == "Q":
    value_name = "Queen"
elif value == "K":
    value_name = "King"
else:
    value_name = value

print(color_name, value_name)
