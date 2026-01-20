#!/usr/bin/env python3
import sys

if len(sys.argv) != 2 or len(sys.argv[1]) != 2:
    sys.exit(1)

card = sys.argv[1]

color = card[0]
value = card[1]

match color:
    case "C":
        color_name = "Clubs"
    case "D":
        color_name = "Diamonds"
    case "H":
        color_name = "Hearts"
    case "S":
        color_name = "Spades"
    case _:
        sys.exit(1)

match value:
    case "A":
        value_name = "Ace"
    case "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
        value_name = value
    case "X":
        value_name = "10"
    case "J":
        value_name = "Jack"
    case "Q":
        value_name = "Queen"
    case "K":
        value_name = "King"
    case _:
        sys.exit(1)

print(f"{color_name} {value_name}")
