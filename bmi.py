#!/usr/bin/env python3

groesse = float(input("Körpergrösse in m: "))
gewicht = float(input("Körpergewicht in kg: "))

bmi = gewicht / (groesse * groesse)

print("Dein Body-Mass-Index:", round(bmi, 2))

